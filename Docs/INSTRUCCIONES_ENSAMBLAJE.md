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

<h1 align = "center"> Información útil para ensamblaje y programación </h1>

[![cc-by-sa-shield]][cc-by-sa] [![renpy-shield]][renpy] [![arduino-shield]][arduino] ![build-shield]

En este archivo README podrás ver información necesaria para que puedas ensamblar el circuito electrónico y programar tu placa Arduino para probar y usar este software.
La documentación presente en este archivo estará dividida en 2 secciones: la <ins>**Zona de Ensamblaje**</ins> y la <ins>**Programación de la placa Arduino**</ins>.

---

### 1. Zona de Ensamblaje.

* **Lista de componentes necesarios:**
  |Nombre del componente|Imagen de referencia|Cantidad|
  |---|---|---|
  |**Arduino UNO R3**|<img width="150" height="150" src="https://arduino.cl/wp-content/uploads/2019/09/Arduino-Uno.jpg">|1|
  |**Módulo sensor PIR HC-SR501**|<img width="150" height="115" src="https://www.seekpng.com/png/detail/356-3562233_pir-motion-sensor-module-pir-motion-sensor.png">|3|
  |**Diodos LED (Rojo y Verde)**|<img width="150" height="150" src="https://atlas-content-cdn.pixelsquid.com/assets_v2/283/2830791147733914962/jpeg-600/G03.jpg">|2|
  |**Buzzer piezoeléctrico**|<img width="150" height="125" src="https://http2.mlstatic.com/D_NQ_NP_894633-MLC48098689757_112021-O.webp">|1|
  |**Display LCD 16x2 (Interfaz I2C incluida)**|<img width="150" height="125" src="https://www.winstar.com.tw/uploads/photos/character-lcd-display-modules/WH1602W-TDI-2.jpg">|1|
  |**Resistores 10k**|<img width="150" height="150" src=https://m.media-amazon.com/images/I/51FT14kt4HL._SX466_.jpg>|1|
  |**Resistores 1k**|<img width="150" height="150" src=https://i.ebayimg.com/images/g/C9gAAOSwqMxfi3dA/s-l500.jpg>|2|
  |**Pulsador Normal Abierto**|<img width="150" height="150" src=https://cdn.sparkfun.com//assets/parts/2/6/2/9/09190-03-L.jpg>|1|
  

* **¡Mira los esquemas del circuito!:**
  - **Esquema pictórico (Tinkercad):**
  <img width="720" height="349" src="https://user-images.githubusercontent.com/77955772/195632456-7d74b375-e121-447c-8d95-80e984914c8f.png">
  
  - **Esquema electrónico (Tinkercad):**
  [¡Accede al PDF aquí!](https://github.com/CharlieFuu69/The_Watchdog_Project/files/9777993/The_Watchdog_Project_Scheme_02.pdf)

  
---

### 2. Programación de la placa Arduino.

* **Paso 1:** Para programar la placa Arduino, necesitas tener instalado el IDE de Arduino y los drivers. Si no los tienes instalados, vé a la sección "Software" de la web oficial de Arduino [desde esta URL](https://www.arduino.cc/en/software) y descarga la versión que se acomode a tu PC.
  <img width="800" height="392" src=https://user-images.githubusercontent.com/77955772/195956603-70cd495e-2e78-4935-b584-bb4a71f84822.png>
* **Paso 2:** Descarga el último paquete publicado en el repositorio desde la sección **"Releases" (Lanzamientos)**. Este paquete contiene el Setup de Instalación del programa GUI y la carpeta `alarm_firmware` con el sketch de Arduino.
* **Paso 3:** Abre la carpeta `alarm_firmware` en el IDE de Arduino. Si no tienes instalada la librería **"LiquidCrystal I2C"** en el IDE, ¿qué estás esperando? [¡Presiona aquí!](https://www.arduino.cc/reference/en/libraries/liquidcrystal-i2c/).
* **Paso 4:** Debes comprobar que la dirección de la interfaz I2C sea correcta. Esta dirección depende del fabricante del IC principal de la interfaz, siendo las siguientes direcciones válidas para configurar:
  
  |Código y fabricante|Dirección|
  |---|---|
  |Texas Instruments - PCF8574|`0x27`|
  |NXP Semiconductors - PCF8574|`0x3F`|
  
  Puedes editar la dirección de la pantalla en la variable `i2c_adress`, ubicado en la línea `41` del sketch. Por defecto se estableció la dirección `0x27`.
* **Paso 5:** Si ya hiciste todo lo anterior (incluido el armado del circuito), compila el código y cárgalo a tu placa Arduino. Comprueba antes de que tu placa esté siendo leída en algún puerto, y que ese puerto no esté ocupado.
  <img width="800" height="450" src=https://user-images.githubusercontent.com/77955772/195958922-f86d4573-5cc9-4b61-902d-c014b1cba868.png>


Con todo eso hecho, la placa podrá empezar a operar bajo la programación del sketch.


