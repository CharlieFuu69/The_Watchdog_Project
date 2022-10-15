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

<h1 align = "center"> Conociendo la Interfaz Gráfica </h1>

[![cc-by-sa-shield]][cc-by-sa] [![renpy-shield]][renpy] [![arduino-shield]][arduino] ![build-shield]

En este archivo README podrás ver información acerca de la interfaz gráfica implementada para el proyecto. Se señala con antelación que esta GUI requiere una conexión física de la placa Arduino, es decir, mediante un cable USB para el tránsito de datos por el puerto serie.

---
### 1. Descarga e instalación.

La última versión emitida de <ins>_**Watchdog Alarm**_</ins>, se puede encontrar en la sección **"Releases (Lanzamientos)"** de este repositorio. Los lanzamientos consisten en un archivo ZIP con el **Setup de Instalación** del cliente GUI (Windows 7, 8, 8.1, 10 y 11) y el **Sketch de Arduino** para cargar a las placas mediante el IDE de Arduino.

<p align="center">
  <img width="800" height="450" src="https://user-images.githubusercontent.com/77955772/195959537-94aaff42-b19d-4fc3-b937-5f944a92f4bf.png">
  <h5 align="center"> <i>[Screenshot] Setup de Instalación. Hecho con Inno Setup Compiler</i> </h5>
</p>

---

### 2. Vista general del cliente GUI.

<p align="center">
  <img width="800" height="450" src="https://user-images.githubusercontent.com/77955772/195959919-f4339879-3dd9-40eb-a3a8-daeeb7582713.png">
  <h5 align="center"> <i>[Screenshot] Panel principal del cliente de Watchdog Alarm</i> </h5>
</p>

El panel principal se divide en 2 áreas visuales. El área izquierda de la pantalla contiene el <ins>**control básico para armar y desarmar el sistema**</ins> de alarma, junto con la actividad de las zonas señalada con íconos y textualmente. El área derecha representa <ins>**la ubicación de los sensores en un diagrama vertical**</ins> de algún edificio o una residencia _(en este caso, el diagrama hace alusión a la sala de laboratorio donde desarrollé este proyecto)_.

**NOTA:** _Las opciones de **"Armar"** y **"Desarmar"** estarán inhabilitadas si no se conecta una Arduino al PC mediante un cable USB_.

* **LISTA DE ÍCONOS EN LA UI:**
  |Ícono|Descripción|
  |---|---|
  |![ui_icon_waiting](https://user-images.githubusercontent.com/77955772/195720041-a490267d-2f0f-458d-8888-f90e2d0b454b.png)|Esperando respuesta/sincronización de la placa Arduino.|
  |![ui_icon_safe](https://user-images.githubusercontent.com/77955772/195719965-3dbcadad-c04e-43b9-897c-3285a403a136.png)|La zona es segura.|
  |![ui_icon_alert_disarmed](https://user-images.githubusercontent.com/77955772/195720173-77096a0c-1485-4017-bd6e-a148322792d0.png)|Intrusos detectados en la zona "X" (Desarmado)|
  |![ui_icon_alert_armed](https://user-images.githubusercontent.com/77955772/195720220-fdd8c335-b780-47cc-b0f2-f33f41aff1c5.png)|Intrusos detectados en la zona "X" (Armado)|

---

### 3. Puesta en marcha del sistema.

1. Cuando la placa Arduino sea conectada al PC, reciba el código desde el IDE o inicies el cliente GUI, el sistema iniciará en modo <ins>**Desarmado**</ins> .
2. Para armar el sistema (activar la alarma), puedes hacerlo de dos formas: activarlo físicamente desde el botón del circuito electrónico, o bien, activarlo desde el cliente GUI. Dos beeps cortos y el LED verde encendido indicarán que la alarma está en funcionamiento.
3. En el caso hipotético de que una de las zonas haya sido vulnerada, el buzzer emitirá secuencias de beeps largos señalando que una zona (o más) han sido vulneradas por intrusos. En el display aparecerá un ícono de Among Us xd.
4. Para desactivar el ruido, presiona brevemente el botón o desactiva desde programa GUI.



