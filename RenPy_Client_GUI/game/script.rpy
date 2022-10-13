#############################################################
## Ejecución de Ren'Py

init:
    image icon_main = "gui/icon_window.png"
    image bg_main_normal = "images/bg_main.jpg"
    image bg_main_blurfx = im.Blur("images/bg_main.jpg", 1.5)
    image bp_classroom = "images/blueprint_classroom.png"

    image ui_wallclock = DynamicDisplayable(wallclock)
    image ui_ic_waiting = "gui/ui_icon_waiting.png"
    image ui_ic_locked_armed = "gui/ui_icon_safe.png"
    image ui_ic_locked_disarmed = "gui/ui_icon_safe.png"
    image ui_ic_unlocked_armed = "gui/ui_icon_alert_armed.png"
    image ui_ic_unlocked_disarmed = "gui/ui_icon_alert_disarmed.png"

    image ui_sensor_locked = "gui/ui_sensor_safe.png"
    image ui_sensor_unlocked = "gui/ui_sensor_alert.png"
    image ui_scanning_locked = "gui/overlay/ui_scanning_safe.png"
    image ui_scanning_unlocked = "gui/overlay/ui_scanning_alert.png"

    define audio.ui_dashboard_open = "audio/ui_dashboard_open.ogg"
    define audio.ui_notify_0 = "audio/ui_notify_success.ogg"
    define audio.ui_notify_1 = "audio/ui_notify_error.ogg"
    define audio.ui_btn_click = "audio/ui_btn_click.ogg"


label splashscreen:
    scene bg_main_normal with dissolve
    call screen title_screen
    scene bg_main_blurfx with dissolve

    $ threading.Thread(target = inst.serial_connection).start()
    $ threading.Thread(target = inst.serial_stream).start()

    play ui_01 ui_dashboard_open
    call screen dashboard


label start:
    return
