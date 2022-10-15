[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/
[arduino]: https://www.arduino.cc/

[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen
[renpy-shield]: https://img.shields.io/badge/Motor%20Gráfico-Ren'Py-red
[arduino-shield]: https://img.shields.io/badge/Hardware-Arduino-blue
[build-shield]: https://img.shields.io/badge/Build-Passing-green

<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/195935170-0eca162f-a566-4459-9316-24509700dead.png">
</p>

<h1 align = "center"> The Watchdog Project </h1>

[![cc-by-sa-shield]][cc-by-sa] [![renpy-shield]][renpy] [![arduino-shield]][arduino] ![build-shield]

Repositorio del proyecto _**<ins>"Watchdog Alarm"</ins>**_ para asignatura HITO en _Inacap Concepción - Talcahuano_.

![ic_help](https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png)
**Área de Descargas:** Obtén el software Presionando Aquí!

---

### ¿En qué consiste "Watchdog Alarm"?
_**<ins>Watchdog Alarm</ins>**_ es un sistema básico de alarmas de seguridad basada en la popular placa de desarrollo de Arduino UNO, solicitado para un certámen en la carrera de Electrónica para _Inacap Concepción - Talcahuano_

En este proyecto se hace uso de hardware y de software para la supervisión de los perímetros cubiertos por los distintos sensores que se pueden conectar hacia la placa Arduino, tales como sensores PIR (detección de movimiento), sensores infrarrojos (barrera delimitadora de perímetro) o reed switchs (apertura de puertas).

El objetivo de este proyecto a nivel de evaluación, es crear un dispositivo que pueda realizar operaciones de I/O, que en teoría significa tomar una o más señales de entrada, y obtener ciertos resultados de salida mediante un programa cargado previamente al microcontrolador.
Para acompañar al hardware, se implementó un programa cliente con el que el Arduino (mediante la conexión serial) puede enviar y recibir datos via USB.

---

### ¿Cómo utilizar el sistema?

Para entender cómo implementar el circuito y hacerlo funcionar, ¡mira la documentación!

* **Información útil para ensamblaje y programación:** [Presiona para abrir](https://github.com/CharlieFuu69/The_Watchdog_Project/blob/main/Docs/INSTRUCCIONES_ENSAMBLAJE.md)
* **Conociendo la Interfaz Gráfica:** [Presiona para abrir](https://github.com/CharlieFuu69/The_Watchdog_Project/blob/main/Docs/INTERFAZ_GRAFICA.md)

---

### Código fuente
El código fuente de este proyecto se encuentra dividido en las siguientes 2 carpetas:
|Ruta del repositorio|Detalles|
|---|---|
|`The_Watchdog_Project/RenPy_Client_GUI/`|Contiene el código fuente del cliente/programa GUI y las librerías utilizadas.|
|`The_Watchdog_Project/Arduino_Sketch/`|Contiene el código fuente que hace funcionar la Arduino.|

* **LIBRERÍAS DE TERCEROS UTILIZADAS:**
  - **LiquidCrystal I2C:** [Referencia en Arduino.cc](https://www.arduino.cc/reference/en/libraries/liquidcrystal-i2c/).
  - **pySerial:** [Documentación en Read The Docs (Python)](https://pyserial.readthedocs.io/en/latest/).

---

### Licencia
[![cc-by-sa-image]][cc-by-sa]

Este software se distribuye bajo la licencia **Creative Commons CC-BY-SA v4.0**.

Si quieres usar este proyecto para algún video o para adjuntarlo en algún sitio web, te agradecería que me dieras crédito adjuntando la URL de este repositorio :3
