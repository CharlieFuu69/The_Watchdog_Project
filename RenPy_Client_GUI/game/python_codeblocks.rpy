## CharlieFuu69
## (2022) The Watchdog Project

## Script: Código principal de comunicación y actividad (Python).

#############################################################

init python:
    import serial, serial.tools.list_ports, time, threading, json, os, platform
    from datetime import datetime

    persistent.debug_log = [] ## almacena la actividad.

    def system_log(level, msg):
        """Esta función crea el formato para registrar una línea de actividad."""

        current_log = "[%s] %s" % (level, msg)
        persistent.debug_log.append(current_log)

        print(current_log)


    class ArduinoSerial:
        """Esta clase ejecuta las operaciones de conexión y lectura de los datos que transitan
        en los puertos serie."""

        def __init__(self):
            super(ArduinoSerial, self).__init__()

            self.arduino = None
            self.port = None
            self.device = None
            self.running = True

            self.stream = {"alarm_status" : "WAIT",
                                "z01" : "WAIT",
                                "z02" : "WAIT",
                                "z03" : "WAIT"}

            self.clock_speed = 0.1
            self.baudrate = 38400


        def serial_connection(self):
            """Este método comprueba si la conexión a un determinado puerto está activa en un
            intervalo de 1 segundo. Si no hay ninguna conexión activa, buscará 'Arduino' en todos
            los puertos disponibles e intentará establecer comunicación con la placa.

            En el arranque del programa:
                Buscará y conectará en algún puerto que tenga conectada una Arduino.

            Durante la ejecución:
                Estará atento a la actividad de los puertos por si ocurre una eventual desconexión.
            """

            listed_ports = []

            system_msg("No hay dispositivos conectados.", 1)

            while self.running:
                listed_ports = [i for i in list(serial.tools.list_ports.grep("Arduino|CH340"))]

                if listed_ports and not self.port:
                    try:
                        self.port = listed_ports[0][0]
                        self.device = listed_ports[0][1]

                        system_log("Stream", "Preparando transmision...\n|   > Dispositivo: %s.\n|   > Puerto: %s.\n|   > Baudrate: %s.\n|   > Clock: %sms." % (self.device, self.port, self.baudrate, self.clock_speed * 1000))
                        self.arduino = serial.Serial(port = self.port, baudrate = self.baudrate, timeout = self.clock_speed)

                    except Exception as connect_error:
                        system_log("Warning", "Error de conexion: %s." % connect_error)

                    finally:
                        if self.port and self.device:
                            system_msg("%s conectada en %s." % (self.device, self.port), 0)
                            system_log("Stream", "Transmision en curso en %s..." % self.port)

                elif not listed_ports:
                    if self.device:
                        system_log("Stream", "%s se ha desconectado." % self.device)
                        system_msg("%s se ha desconectado." % self.device, 1)
                    self.port = self.device = self.arduino = None

                time.sleep(self.clock_speed)
                renpy.restart_interaction()


        def serial_stream(self):
            """Este método lee los bytes que transitan por el puerto serie y los formatea como un
            diccionario."""

            system_log("Stream", "Esperando transmision de datos...")

            while self.running:
                try:
                    readserial = self.arduino.readline().decode()

                    if readserial:
                        self.stream = json.loads(readserial.replace("\n", ""))

                except Exception as pad_error:
                    self.stream = {"alarm_status" : "WAIT", "z01" : "WAIT", "z02" : "WAIT", "z03": "WAIT"}

                finally:
                    time.sleep(self.clock_speed)
                    renpy.restart_interaction()


        def write_to_stream(self, data):
            """Esta función transmite datos mediante el stream hacia la Arduino."""

            try:
                self.arduino.write(data = data)
            except Exception as stream_error:
                system_log("Warning", "Error al transmitir comando: %s." % stream_error)
            finally:
                renpy.restart_interaction()


    def wallclock(st, at):
        """Esta función crea y muestra un displayable de reloj en tiempo real (Local)"""

        now = datetime.now()
        current_datetime = now.strftime("%d/%m/%Y - %H:%M:%S (GMT -3)")
        return Text(str(current_datetime),
        color = "#FFF", font = gui.interface_text_font, size = 19, outlines = [(2, "#000", 0, 0)]), 0.1


    def system_msg(msg = "", status = 0):
        """Esta función muestra mensajes pop-up al usuario."""

        if renpy.get_screen("notify"):
            renpy.hide_screen("notify")
        renpy.show_screen("notify", message = msg, status = status)


    def streamkey(key):
        """Esta función se encarga de buscar y representar los datos transmitidos en el stream
        de la Arduino. Recibe como argumento la key extraída línea a línea del stream."""

        ## Palabras clave de transmisión
        keywords = {
                            "ARMED" : "{color=7F7}Armado y operando.{/color}",
                            "DISARMED" : "Desarmado.",
                            "IDLE" : "{color=8C8C8C}No disponible.{/color}",
                            "WAIT" : "{color=FF7}Esperando...{/color}",
                            "LOCKED" : "{color=8F7}Seguro.{/color}",
                            "UNLOCKED" : "{color=F77}Perímetro vulnerado.{/color}"}

        if key in keywords:
            return keywords[key]
        else:
            return "{color=FF0}Esperando...{/color}"


    def run_wizard(filename):
        """Ejecuta la apertura de instaladores de Windows en la marcha."""

        try:
            os.startfile(config.basedir + "\\Arduino Drivers\\" + filename)
        except Exception as start_error:
            system_log("Warning", "No se pudo ejecutar el instalador: %s." % start_error)

    ## ----------------------------------------------------------------------------------------------------------- ##
    ## Canales de audio
    renpy.music.register_channel("ui_01", mixer = "voice", loop = False, stop_on_mute = True, tight = True, buffer_queue = True)
    renpy.music.register_channel("ui_02", mixer = "voice", loop = False, stop_on_mute = True, tight = True, buffer_queue = True)

    ## ----------------------------------------------------------------------------------------------------------- ##
    ## Instancia de la clase ArduinoSerial
    inst = ArduinoSerial()
