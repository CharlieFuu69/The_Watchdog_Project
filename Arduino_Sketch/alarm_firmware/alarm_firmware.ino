// CharlieFuu69
// (2022) The Watchdog Project

// Script: Arduino UNO R3 - Firmware de centralita.

/* ---------------------------------------------------------------------------------------------------------------- */

/* DISTRIBUCIÓN DE PINES

Display LCD
- A4: Datos (SDA).
- A5: Clock (SCL).

Pilotos LED
- D12: LED armado.
- D11: LED alarma disparada.

Sensores
- D2: Switch armado/desarmado.
- D3: Zona 1.
- D4: Zona 2.
- D5: Zona 3.
- D6: Zona 4.
*/

// Librerías
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

/*----------------------------------------------------------------------------------------------------------------- */
// Ajustes generales

// Status de alarma, zonas y buzzer de alerta.
String alarm_status = "DISARMED";
String z01 = "WAIT";
String z02 = "WAIT";
String z03 = "WAIT";
bool buzzer_alert = false;


// Distribución de pines y pantalla LCD
int i2c_adress = 0x27;
int pilot_armed = 12;
int pilot_danger = 11;
int pin_set = 2;

int pin_z01 = 3;
int pin_z02 = 4;
int pin_z03 = 5;


/* ---------------------------------------------------------------------------------------------------------------- */
// Pantalla LCD

// Instancia
LiquidCrystal_I2C lcd(i2c_adress, 16, 2);

// Símbolos
byte sym_alarm_disarmed[8] {0x0E, 0x08, 0x08, 0x1F, 0x1F, 0x1B, 0x1B, 0x1F};
byte sym_alarm_armed[8] {0x0E, 0x0A, 0x0A, 0x1F, 0x1F, 0x1B, 0x1B, 0x1F};
byte sym_alarm_intruder[8] {0x00, 0x0E, 0x18, 0x1E, 0x1E, 0x0E, 0x0A, 0x0A};


/*----------------------------------------------------------------------------------------------------------------- */
// Funciones de actividad

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
    pinMode(pin_z01, INPUT); // Zona 1
    pinMode(pin_z02, INPUT); // Zona 2
    pinMode(pin_z03, INPUT); // Zona 3

    // Registro de símbolos
    lcd.createChar(0, sym_alarm_disarmed);
    lcd.createChar(1, sym_alarm_armed);
    lcd.createChar(2, sym_alarm_intruder);

    lcd.setCursor(0,0);
    lcd.print("Watchdog Alarm");
}


void buzzer_trigger() {
    digitalWrite(pilot_danger, HIGH);
    delay(250);
    digitalWrite(pilot_danger, LOW);
    delay(150);
}


void activity_listener() {
    /* Esta función busca actividad no permitida en las zonas instaladas. */

    String status_array[4] = {z01, z02, z03};

    lcd.setCursor(0,1);

    if (alarm_status == "ARMED") {
        for (int i = 0; i < 4; i++) {
            if (status_array[i] == "UNLOCKED") {
                buzzer_alert = true;
                break;
            }
        }

        if (buzzer_alert) {
            lcd.write(2);
            lcd.print(" BRUH          ");
            buzzer_trigger();
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

    if (!buzzer_alert){
        Serial.print(data_strip);
    }
}


String zone(int zone_pin) {
    /* Esta función devuelve "LOCKED" en caso de que el sensor de la zona "zone_pin" no
    tenga actividad de intrusos. */

    return (zone_pin == 0) ? "LOCKED":"UNLOCKED";
}


/*----------------------------------------------------------------------------------------------------------------- */
// Ejecución (Bucle)

void loop() {
    // Lectura de botón de armado/desarmado
    int alarm_set = digitalRead(pin_set);
    String stream_read = "NULL";

    if (Serial.available() > 0) {
        stream_read = Serial.readString();
    }

    z01 = zone(digitalRead(pin_z01));
    z02 = zone(digitalRead(pin_z02));
    z03 = zone(digitalRead(pin_z03));

    // Ajuste de armado/desarmado
    if ((alarm_set == 1 || stream_read == "1") && alarm_status == "DISARMED"){
        alarm_status = "ARMED";
        digitalWrite(pilot_armed, HIGH);

        digitalWrite(pilot_danger, LOW);
        delay(50);
        digitalWrite(pilot_danger, HIGH);
        delay(50);
        digitalWrite(pilot_danger, LOW);
        delay(50);
        digitalWrite(pilot_danger, HIGH);
        delay(50);
        digitalWrite(pilot_danger, LOW);
        delay(50);
        digitalWrite(pilot_danger, HIGH);
        delay(50);
        digitalWrite(pilot_danger, LOW);
        delay(950);
    }
    else if ((alarm_set == 1 || stream_read == "0") && alarm_status == "ARMED") {
        alarm_status = "DISARMED";
        buzzer_alert = false;
        digitalWrite(pilot_armed, LOW);
        digitalWrite(pilot_danger, LOW);
        delay(1000);
    }

    stream_data(alarm_status, z01, z02, z03); // Procesado y entrega de datos
    activity_listener();

    delay(100);
}
