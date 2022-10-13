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

### ¿Cómo utilizar el sistema?

* **¿Cómo se utiliza una vez implementado el circuito?:**
**VISUALIZACIÓN DE ACTIVIDAD**
> 1) Descarga el último paquete lanzado en este repositorio. Este paquete incluye un instalador del programa GUI (Windows 7, 8, 8.1, 10 y 11) y la carpeta con el Sketch INO que debes subir a tu placa con [Arduino IDE (Software oficial)](https://www.arduino.cc/en/software). El IDE posee los drivers necesarios, pero si no has instalado los drivers de la Arduino, el programa GUI trae también los instaladores para Arduino UNO/CH340.
> 2) Compila y sube el programa a la placa Arduino UNO. Cuando hayas subido el programa, tu placa podrá trabajar sin problemas.
> 3) Al finalizar la subida debes cerrar el monitor serial de Arduino IDE, para que el programa GUI no tenga problemas para reconocer tu Arduino.
> 4) Abre el programa GUI. No te preocupes por los puertos COM, pues el programa buscará automáticamente si algún puerto tiene conectada alguna placa Arduino.
> 5) No te preocupes si tienes una Arduino no oficial. El programa GUI está preparado para reconocer réplicas genéricas de Arduino con el chip CH340.

**PUESTA EN MARCHA**
> 1) Cuando la Arduino haya recibido el programa o haya sido conectada al PC, iniciará en modo <ins>**Desarmado**</ins>, es decir, estará detectando la actividad de los sensores pero no emitirá alertas de ningún tipo.
> 2) Puedes armar el sistema de dos formas: físicamente manteniendo pulsado brevemente el botón, y desde el programa GUI (si es que tienes conectada la Arduino al PC). Sonarán 2 beeps, se encenderá el LED verde y se mostrará en el display que la alarma ya está armada.
> 3) En el caso hipotético de que una de las zonas haya sido vulnerada, el buzzer emitirá secuencias de beeps largos señalando que una zona (o más) han sido vulneradas por intrusos. En el display aparecerá un ícono de Among Us xd.
> 4) Para desactivar el ruido, puedes desarmar el sistema volviendo a presionar brevemente el botón o desactivando el sistema desde el programa GUI.

---

### Zona de ensamblaje

* **Lista de componentes necesarios:**
  |Nombre del componente|Imagen de referencia|Cantidad|
  |---|---|---|
  |**Arduino UNO R3**|<img width="150" height="150" src="https://arduino.cl/wp-content/uploads/2019/09/Arduino-Uno.jpg">|1|
  |**Módulo sensor PIR HC-SR501**|<img width="150" height="125" src="https://www.seekpng.com/png/detail/356-3562233_pir-motion-sensor-module-pir-motion-sensor.png">|3|
  |**Diodos LED (Rojo y Verde)**|<img width="150" height="150" src="https://atlas-content-cdn.pixelsquid.com/assets_v2/283/2830791147733914962/jpeg-600/G03.jpg">|2|
  |**Buzzer piezoeléctrico**|<img width="150" height="125" src="https://http2.mlstatic.com/D_NQ_NP_894633-MLC48098689757_112021-O.webp">|1|
  |**Display LCD 16x2 (Interfaz I2C incluida)**|<img width="150" height="125" src="https://www.winstar.com.tw/uploads/photos/character-lcd-display-modules/WH1602W-TDI-2.jpg">|1|
  |**Resistores 10k**|<img width="150" height="150" src=https://m.media-amazon.com/images/I/51FT14kt4HL._SX466_.jpg>|1|
  |**Resistores 1k**|<img width="150" height="150" src=https://i.ebayimg.com/images/g/C9gAAOSwqMxfi3dA/s-l500.jpg>|2|
  |**Pulsador Normal Abierto**|<img width="150" height="150" src=https://cdn.sparkfun.com//assets/parts/2/6/2/9/09190-03-L.jpg>|1|
  

* **¡Mira los esquemas del circuito!:**
  - **Esquema físico (Tinkercad):**
  ![The_Watchdog_Project_Image](https://user-images.githubusercontent.com/77955772/195429003-2ade9a4c-f5ee-4cb5-a1ad-4564956b2421.png)
  
  - **Esquema electrónico PDF (Tinkercad):** [¡Accede al PDF en esta URL!](https://github.com/CharlieFuu69/The_Watchdog_Project/files/9768072/The_Watchdog_Project_Scheme.pdf)

---

### Código fuente
El código fuente de este proyecto se encuentra dividido en las siguientes 2 carpetas:
_[Pendiente de subir]_

---

### Licencia
[![cc-by-sa-image]][cc-by-sa]
Este software se distribuye bajo la licencia **Creative Commons BY-SA v4.0**
