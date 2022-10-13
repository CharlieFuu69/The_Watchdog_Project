## CharlieFuu69
## (2022) The Watchdog Project

## Script: Interfaz principal del programa (Ren'Py).

#############################################################

screen title_screen():
    modal True
    style_prefix "title_screen"

    timer 4.0 action [Hide("title_screen"), Return()]

    vbox align(0.5, 0.5):
        add "icon_main" at title_alpha(timeset = (0.01, 3.0), x = 0.5) zoom 0.7
        null height 10
        label "Watchdog Alarm" at title_alpha(timeset = (0.5, 2.5), x = 0.5)
        text "[config.version]" at title_alpha(timeset = (0.5, 2.5), x = 0.5)

    text "© 2022 - Todos los derechos reservados." at title_alpha(timeset = (0.75, 2.25), x = 0.5) ypos 0.9 color "#8C8C8C"


## -------------------------------------------------------------------------------------------------------------- ##

screen dashboard():
    style_prefix "dashboard"

    python:
        activity_array = []

    vbox:
        style_prefix "titlepage"
        label "Panel principal" at alpha_ctrl(a = 1.0, delay = 0.5)
        add Solid("#FFF") at splitline(x = 0.5, bef = (0, 2), aft = (1100, 2))

    add Solid("#FFF") at splitline(x = 0.5, bef = (2, 0), aft = (2, 400)) ypos 0.25
    add "ui_wallclock" at alpha_ctrl(a = 1.0, delay = 0.5) align(0.5, 0.16)


    vbox at alpha_ctrl(a = 1.0, delay = 0.5):
        pos(0.1, 0.25)
        spacing 20

        label "ACTIVIDAD DE ZONAS"

        vbox:
            text "Estado de sistema: %s" % streamkey(inst.stream["alarm_status"]) xalign 0.5
            hbox:
                style_prefix "btn"
                spacing 20
                textbutton "Activar (Armar)":
                    action If(inst.device, Function(inst.write_to_stream, data = "1".encode()),
                    Function(system_msg, msg = "Acción inválida. No hay dispositivos conectados.", status = 1))
                textbutton "Desactivar (Desarmar)":
                    action If(inst.device, Function(inst.write_to_stream, data = "0".encode()),
                    Function(system_msg, msg = "Acción inválida. No hay dispositivos conectados.", status = 1))

        ## Lista de zonas + actividad
        vbox:
            spacing 10
            for _num, _key in zip(range(1, 4), ["z01", "z02", "z03"]):
                hbox spacing 10:
                    if inst.stream["alarm_status"] != "WAIT":
                        add "ui_ic_%s_%s" % (inst.stream[_key].lower(), inst.stream["alarm_status"].lower()) zoom 0.5
                    else:
                        add "ui_ic_waiting" zoom 0.5
                    text "Zona %s: %s" % (_num, streamkey(inst.stream[_key])) yalign 0.5


    add "bp_classroom" at alpha_ctrl(a = 1.0, delay = 0.5) pos(0.53, 0.23)

    fixed at alpha_ctrl(a = 1.0, delay = 0.5):
        maximum(500, 419)
        pos(0.53, 0.23)

        if inst.stream["alarm_status"] != "WAIT":
            add "ui_sensor_%s" % inst.stream["z02"].lower() pos(0.04, 0.05) rotate 90 zoom 0.15
            add "ui_sensor_%s" % inst.stream["z03"].lower() pos(0.065, 0.75) zoom 0.15

            add "ui_scanning_%s" % inst.stream["z01"].lower() at scanner((0.63, 0.16), 1.5 if inst.stream["z01"] == "LOCKED" else 0.25)
            add "ui_scanning_%s" % inst.stream["z02"].lower() at scanner((0.07, 0.09), 1.5 if inst.stream["z02"] == "LOCKED" else 0.25)
            add "ui_scanning_%s" % inst.stream["z03"].lower() at scanner((0.07, 0.92), 1.5 if inst.stream["z03"] == "LOCKED" else 0.25)

            add "ui_ic_%s_%s" % (inst.stream["z01"].lower(), inst.stream["alarm_status"].lower()) align(0.64, 0.14) zoom 0.5
            add "ui_ic_%s_%s" % (inst.stream["z02"].lower(), inst.stream["alarm_status"].lower()) align(0.05, 0.06) zoom 0.5
            add "ui_ic_%s_%s" % (inst.stream["z03"].lower(), inst.stream["alarm_status"].lower()) align(0.05, 0.95) zoom 0.5

        else:
            add "ui_ic_waiting" align(0.64, 0.14) zoom 0.5
            add "ui_ic_waiting" align(0.05, 0.06) zoom 0.5
            add "ui_ic_waiting" align(0.05, 0.95) zoom 0.5


    hbox:
        style_prefix "btn"
        xalign 0.5 ypos 0.87
        spacing 20
        textbutton "Debug (Desarrollo)" action [Hide("dashboard"), Show("developer_debug_log")]
        textbutton "Acerca de" action [Hide("dashboard"), Show("development_credits")]
        textbutton "Salir" action [SetVariable("inst.running", False), Quit(confirm =  False)]


## -------------------------------------------------------------------------------------------------------------- ##
## Menú de Instalación de Drivers

screen drivers_menu():
    style_prefix "dashboard_alt"

    default arch = platform.architecture()

    vbox:
        style_prefix "titlepage"
        label "Instalación de Drivers" at alpha_ctrl(a = 1.0, delay = 0.5)
        add Solid("#FFF") at splitline(x = 0.5, bef = (0, 2), aft = (1100, 2))

    use custom_viewport(scale = (1030, 460)):
        text "Si estás teniendo problemas para utilizar el hardware de {color=0F0}Watchdog Alarm{/color}, o no se detecta el dispositivo en el ordenador, es posible que los drivers no estén en buen estado o no hayan sido instalados previamente."
        text "El cliente de {color=0F0}Watchdog Alarm{/color} incluye los drivers compatibles con el hardware para que puedas instalarlos en tu ordenador."

        null height 15

        vbox:
            spacing 15
            add Solid("#FFF") at splitline(x = 0.0, bef = (0, 2), aft = (2000, 2), off = 0.3)
            if "64bit" in arch[0] or "32bit" in arch[0]:
                label "Tu ordenador posee arquitectura %s. Para tu equipo, se recomienda que utilices el siguiente instalador:" % arch[0]

                hbox:
                    style_prefix "btn"
                    if arch[0] == "64bit":
                        textbutton "Arduino LLC AMD64 (64-bit)":
                            action Function(run_wizard, filename = "dpinst-amd64.exe")
                    else:
                        textbutton "Arduino LLC x86 (32-bit)":
                            action Function(run_wizard, filename = "dpinst-x86.exe")

            else:
                label "No se detectó correctamente la arquitectura del PC. Más abajo están todos los instaladores incluidos en {color=0F0}Watchdog Alarm{/color}. Puedes probar cada uno de ellos a tu propio criterio."

        vbox:
            spacing 15
            text u"\u2022 Todos los Instaladores de drivers incluidos en {color=0F0}Watchdog Alarm{/color}:"

            hbox:
                style_prefix "btn"
                spacing 20
                textbutton "Arduino LLC x86 (32-bit)":
                    action Function(run_wizard, filename = "dpinst-x86.exe")
                textbutton "Arduino LLC AMD64 (64-bit)":
                    action Function(run_wizard, filename = "dpinst-amd64.exe")
                textbutton "Arduino UNO (Genérico CH340)":
                    action Function(run_wizard, filename = "CH341SER.EXE")

    hbox:
        style_prefix "btn"
        xalign 0.5 ypos 0.87
        textbutton "Regresar al Dashboard" action [Hide("drivers_menu"), Show("dashboard")]


## -------------------------------------------------------------------------------------------------------------- ##
## Menú de créditos de desarrollo

screen development_credits():
    style_prefix "dashboard"

    vbox:
        style_prefix "titlepage"
        label "Acerca del proyecto" at alpha_ctrl(a = 1.0, delay = 0.5)
        add Solid("#FFF") at splitline(x = 0.5, bef = (0, 2), aft = (1100, 2))

    use custom_viewport(scale = (1030, 460)):
        vbox:
            label "Watchdog Alarm"
            label "[config.version]"

        add Solid("#FFF") at splitline(x = 0.0, bef = (0, 2), aft = (2000, 2), off = 0.3)
        label "CONTENIDO LICENCIADO"

        vbox:
            label "{i}Ren'Py (Motor gráfico){/i}"
            text _("[renpy.license!t]") italic True
            null height 10
            text "- Visitar {a=https://www.renpy.org/}www.renpy.org{/a}"
            text "- Ver la {a=https://www.renpy.org/l/license}Lista de Software y Código Fuente{/a} completo de Ren'Py [[En Inglés]"

        vbox:
            label "{i}© 2022, Watchdog Alarm (Cliente + Firmware) :{/i}"
            text "{color=8C8C8C}\"Watchdog Alarm\"{/color} por {color=8C8C8C}CharlieFuu69{/color}, en colaboración con {color=8C8C8C}Diego Castillo{/color}, se distribuye bajo una {color=8C8C8C}Licencia Creative Commons [[BY-NC-SA v4.0] Internacional{/color}. Basada en una obra en {color=8C8C8C}https://github.com/CharlieFuu69/The_Watchdog_Project{/color}" italic True
            null height 10
            text "La Licencia de Creative Commons de este programa establece los siguientes términos para compartir o distribuirlo:"
            text "- {color=ff0}BY (Atribución){/color} : Al compartir este software, debes dar crédito/atribución del autor (Carlos Cruces - CharlieFuu69)."
            text "- {color=ff0}NC (No Comercial){/color} : No se permite ningún tipo de acto lucrativo al distribuir el cliente o el firmware. El programa es completamente gratuito."
            text "- {color=ff0}SA (Compartir Igual){/color} : Puedes modificar el software y compartirlo, siempre y cuando utilices la misma licencia que el proyecto original (BY-NC-SA)."
            null height 10
            text "- Ir a la {a=http://creativecommons.org/licenses/by-nc-sa/4.0/}Licencia Creative Commons [[BY-NC-SA v4.0]{/a}!"
            text "- Ir al {a=https://github.com/CharlieFuu69/The_Watchdog_Project}Repositorio de \"The Watchdog Project\"{/a} en GitHub!"

        vbox:
            label "{i}Lato (Fuente de Texto) :{/i}"
            text "Copyright © 2011-2015 by tyPoland Lukasz Dziedzic (http://www.typoland.com/) with Reserved Font Name \"Lato\".\nEsta fuente/software está licenciado bajo la {color=ff0}SIL Open Font License{/color} Versión 1.1." italic True
            null height 10
            text "- Ver la {a=http://scripts.sil.org/OFL}Licencia SIL{/a}."

        vbox:
            label "{i}pySerial (API de conexión serie) :{/i}"
            text "Copyright © 2001-2020 Chris Liechti <cliechti@gmx.net> All Rights Reserved." italic True
            text "Esta API se distribuye bajo una licencia BSD/FreeBSD."
            null height 10
            text "- Ver la {a=https://github.com/pyserial/pyserial/blob/master/LICENSE.txt}Licencia BSD{/a}."
            text "- Ver el {a=https://github.com/pyserial/pyserial}Código Fuente{/a} en GitHub."


    hbox:
        style_prefix "btn"
        xalign 0.5 ypos 0.87
        textbutton "Regresar al Dashboard" action [Hide("development_credits"), Show("dashboard")]


screen developer_debug_log():
    style_prefix "dashboard"

    vbox:
        style_prefix "titlepage"
        label "Registro de actividad [[Debug]" at alpha_ctrl(a = 1.0, delay = 0.5)
        add Solid("#FFF") at splitline(x = 0.5, bef = (0, 2), aft = (1100, 2))

    add Solid("#000") alpha 0.3 pos(0.08, 0.16)

    use custom_viewport(scale = (1030, 460), yinit = 1.0):
        for log_line in persistent.debug_log:
            text log_line.replace("[", "[[")

    hbox:
        style_prefix "btn"
        xalign 0.5 ypos 0.87
        textbutton "Regresar al Dashboard" action [Hide("developer_debug_log"), Show("dashboard")]


## -------------------------------------------------------------------------------------------------------------- ##
## Viewport

screen custom_viewport(scale = (500, 500), yinit = 0.0):
    viewport at alpha_ctrl(a = 1.0, delay = 0.5):
        xysize(scale[0], scale[1])
        pos(0.1, 0.18)
        yinitial yinit
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        side_yfill True

        vbox:
            spacing 25
            transclude


#############################################################
## Estilos de UI

define color_theme = "#070"

## title_screen
style title_screen_label_text:
    font gui.interface_text_font
    size 45
    color "#FFF"
    outlines [(2, color_theme, 0, 0), (2, color_theme, 2, 2)]

style title_screen_text:
    font gui.interface_text_font
    size 19
    color "#FFF"
    outlines [(2, "#000", 0, 0)]


## titlepage
style titlepage_vbox:
    xalign 0.5 ypos 0.05
    xsize 1100
    spacing 25

style titlepage_label:
    xalign 0.5

style titlepage_label_text:
    font gui.interface_text_font
    size 30
    color "#FFF"
    outlines [(2, color_theme, 0, 0)]


## dashboard
style dashboard_label_text:
    font gui.interface_text_font
    size 22
    color color_theme
    outlines [(2, "#FFF", 0, 0)]

style dashboard_text:
    font gui.interface_text_font
    size 19
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style dashboard_alt_label_text is dashboard_label_text:
    color "#FF0"
    outlines [(2, "#000", 0, 0)]

style dashboard_alt_text is dashboard_text


## btn
style btn_button:
    idle_background Frame("gui/button/btn_dashboard_idle.png", 25, 25, 25, 25)
    hover_background Frame("gui/button/btn_dashboard_hover.png", 25, 25, 25, 25)
    activate_sound audio.ui_btn_click
    padding(10, 10, 10, 10)

style btn_button_text:
    font gui.interface_text_font
    size 19
    text_align 0.5
    color "#FFF"

    idle_outlines [(2, "#000", 0, 0)]
    hover_outlines [(2, color_theme, 0, 0)]
