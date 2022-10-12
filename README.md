[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/
[arduino]: https://www.arduino.cc/

[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen
[renpy-shield]: https://img.shields.io/badge/Motor%20Gráfico-Ren'Py-red
[arduino-shield]: https://img.shields.io/badge/Hardware-Arduino-blue
[build-shield]: https://img.shields.io/badge/Build-Not%20available-yellow

<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/193131412-71156534-2981-4b9b-bc94-21015538ff8c.png">
</p>

<h1 align = "center"> The Watchdog Project </h1>

[![cc-by-sa-shield]][cc-by-sa] [![renpy-shield]][renpy] [![arduino-shield]][arduino] ![build-shield]

Repositorio del proyecto _**<ins>"Watchdog Alarm"</ins>**_ para asignatura HITO en _Inacap Concepción - Talcahuano_.

---

### ¿En qué consiste "Watchdog Alarm"?
_**<ins>Watchdog Alarm</ins>**_ es un sistema básico de alarmas de seguridad basada en la popular placa de desarrollo de Arduino UNO, solicitado para un certámen en la carrera de Electrónica para _Inacap Concepción - Talcahuano_

En este proyecto se hace uso de hardware y de software para la supervisión de los perímetros cubiertos por los distintos sensores que se pueden conectar hacia la placa Arduino, tales como sensores PIR (detección de movimiento), sensores infrarrojos (barrera delimitadora de perímetro) o reed switchs (apertura de puertas).

El objetivo de este proyecto a nivel de evaluación, es crear un dispositivo que pueda realizar operaciones de I/O, que en teoría significa tomar una o más señales de entrada, y obtener ciertos resultados de salida mediante un programa cargado previamente al microcontrolador.
Para acompañar al hardware, se implementó un programa cliente con el que el Arduino (mediante la conexión serial) puede enviar y recibir datos via USB.

---

### Sensores y componentes utilizados

* **Arduino UNO R3:**
<img width="150" height="150" src="https://arduino.cl/wp-content/uploads/2019/09/Arduino-Uno.jpg">

* **Módulo sensor PIR HC-SR501 (2):**
<img width="150" height="125" src="https://www.seekpng.com/png/detail/356-3562233_pir-motion-sensor-module-pir-motion-sensor.png">

* **Módulo Reed Switch (1):**
<img width="150" height="125" src="https://www.seekpng.com/png/detail/277-2771854_reed-switch.png">

* **Diodos LED (Rojo y verde) (2):**
<img width="150" height="150" src="https://atlas-content-cdn.pixelsquid.com/assets_v2/283/2830791147733914962/jpeg-600/G03.jpg">

* **Buzzer piezoeléctrico (1):**
<img width="150" height="125" src="https://http2.mlstatic.com/D_NQ_NP_894633-MLC48098689757_112021-O.webp">

* **Display LCD 16x2 + Interfaz I2C (1):**
<img width="150" height="125" src="https://www.winstar.com.tw/uploads/photos/character-lcd-display-modules/WH1602W-TDI-2.jpg">

---

### Instalación / Esquema del circuito





### Código fuente
El código fuente de este proyecto se encuentra dividido en las siguientes 2 carpetas:
_[Pendiente de subir]_

### Licencia
[![cc-by-sa-image]][cc-by-sa]
Este software se distribuye bajo la licencia **Creative Commons BY-SA v4.0**
