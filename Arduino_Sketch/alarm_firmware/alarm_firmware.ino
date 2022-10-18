// CharlieFuu69
// (2022) The Watchdog Project

// Script: Arduino UNO R3 - Firmware de centralita.

/* ---------------------------------------------------------------------------------------------------------------- */

/* DISTRIBUCIÓN DE PINES

Display LCD
- A4: Datos (SDA).
- A5: Clock (SCL).

Pilotos LED
- D11: LED alarma disparada.
- D12: LED armado.

Sensores
- D2: Switch armado/desarmado.
- D3: Zona 1.
- D4: Zona 2.
- D5: Zona 3.
*/

// Librerías
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

/*----------------------------------------------------------------------------------------------------------------- */
// Ajustes generales

// Status de alarma, zonas y buzzer de alerta.
String alarm_status = "DISARMED";
String zone_status[3] = {"WAIT", "WAIT", "WAIT"};
bool alarm_activated = false;


// Distribución de pines y pantalla LCD
int i2c_adress = 0x27;

int pilot_armed = 12;
int pilot_danger = 11;

int pin_set = 2; // Botón armado/desarmadsso

int pin_zone01 = 3;
int pin_zone02 = 4;
int pin_zone03 = 5;


/* ---------------------------------------------------------------------------------------------------------------- */
// Pantalla LCD

// Instancia
LiquidCrystal_I2C lcd(i2c_adress, 16, 2);

// Símbolos
byte sym_alarm_disarmed[8] {0x0E, 0x08, 0x08, 0x1F, 0x1F, 0x1B, 0x1B, 0x1F};
byte sym_alarm_armed[8] {0x0E, 0x0A, 0x0A, 0x1F, 0x1F, 0x1B, 0x1B, 0x1F};
byte sym_alarm_intruder[8] {0x00, 0x0E, 0x18, 0x1E, 0x1E, 0x0E, 0x0A, 0x0A};


/*----------------------------------------------------------------------------------------------------------------- */
// Funciones de preparación

// Inicialización (Secuencia única)
void setup() {
    Serial.begin(38400);

    lcd.init();
    lcd.backlight();

    // Status de alarma (General)
    pinMode(pilot_armed, OUTPUT); // Piloto armado/desarmado
    pinMode(pilot_danger, OUTPUT); // Piloto de zona vulnerada
    pinMode(pin_set, INPUT); // Botón de set.

    // Sensores (Zonas)
    pinMode(pin_zone01, INPUT); // Zona 1
    pinMode(pin_zone02, INPUT); // Zona 2
    pinMode(pin_zone03, INPUT); // Zona 3

    // Registro de símbolos
    lcd.createChar(0, sym_alarm_disarmed);
    lcd.createChar(1, sym_alarm_armed);
    lcd.createChar(2, sym_alarm_intruder);

    lcd.setCursor(0,0);
    lcd.print("Watchdog Alarm");
}

/*----------------------------------------------------------------------------------------------------------------- */
// Funciones de secuencias simples

void buzzer_alarm_armed() {
    /* Secuencia de beeps para alarma armada */
    int beep_counter = 0;

    while (beep_counter < 4){
        digitalWrite(pilot_danger, HIGH);
        delay(50);
        digitalWrite(pilot_danger, LOW);
        delay(50);

        beep_counter += 1;
    }
}


void buzzer_alarm_activated() {
    /* Secuencia de beeps de alarma activada (vulnerada) */
    digitalWrite(pilot_danger, HIGH);
    delay(250);
    digitalWrite(pilot_danger, LOW);
    delay(150);
}


/*----------------------------------------------------------------------------------------------------------------- */
// Funciones de procesamiento de datos y actividad

void activity_listener() {
    /* Esta función busca actividad no permitida en las zonas instaladas. */

    lcd.setCursor(0,1);

    if (alarm_status == "ARMED") {
        for (int i = 0; i < 3; i++) {
            if (zone_status[i] == "UNLOCKED") {
                alarm_activated = true;
                break;
            }
        }

        if (alarm_activated) {
            lcd.write(2);
            lcd.print(" SUS          ");
            buzzer_alarm_activated();
        }
        else {
            lcd.write(1);
            lcd.print(" Armado.       ");
        }
    }
    else {
        lcd.write(0);
        lcd.print(" Desarmado.    ");
    }
}


void stream_data(String status, String z1, String z2, String z3) {
    /* Esta función crea el formato de los datos principales de actividad con estilo JSON
    y los imprime para la posterior lectura del cliente. */

    String data_strip = "{\"alarm_status\" : \"" + status + "\", \"z01\" : \"" + z1 + "\", \"z02\" : \"" + z2 + "\" , \"z03\" : \"" + z3 + "\"}\n";

    if (!alarm_activated){
        Serial.print(data_strip);
    }
}


String zone(int zone_pin) {
    /* Esta función devuelve "LOCKED" en caso de que el sensor de la zona "zone_pin" no
    tenga actividad de intrusos. */

    return (zone_pin == 0) ? "LOCKED":"UNLOCKED";
}


/*----------------------------------------------------------------------------------------------------------------- */
// Ejecución constante (Bucle)

void loop() {
    // Recepción de datos (puerto serie)
    String stream_read = "NULL";

    if (Serial.available() > 0) {
        stream_read = Serial.readString();
    }

    // Entradas digitales
    int alarm_set = digitalRead(pin_set);

    zone_status[0] = zone(digitalRead(pin_zone01));
    zone_status[1] = zone(digitalRead(pin_zone02));
    zone_status[2] = zone(digitalRead(pin_zone03));

    // Ajuste de armado/desarmado
    if ((alarm_set == 1 || stream_read == "1") && alarm_status == "DISARMED"){
        alarm_status = "ARMED";
        digitalWrite(pilot_armed, HIGH);

        buzzer_alarm_armed();
        delay(950);
    }
    else if ((alarm_set == 1 || stream_read == "0") && alarm_status == "ARMED") {
        alarm_status = "DISARMED";
        alarm_activated = false;
        digitalWrite(pilot_armed, LOW);
        digitalWrite(pilot_danger, LOW);
        delay(1000);
    }

    // Procesado, entrega de datos y escucha de actividad
    stream_data(alarm_status, zone_status[0], zone_status[1], zone_status[2]);
    activity_listener();

    delay(100);
}
