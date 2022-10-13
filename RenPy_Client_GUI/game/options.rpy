## CharlieFuu69
## (2022) The Watchdog Project

## Script: Configuración básica del juego (Ren'Py - Python).

#############################################################

## ------------------------------------------------------------------------------------------------------------- ##
## Metadatos

define config.version = "v0.9.33a [Build 20221013_01]"
define config.name = "Watchdog Alarm - Cliente %s" % config.version
define config.window_icon = "gui/icon_window.png"

define build.name = "Watchdog Alarm"


## ------------------------------------------------------------------------------------------------------------- ##
## Preferencias por default

## Gráficos
default preferences.gl_powersave = False
default preferences.gl_framerate = 60
define config.image_cache_size_mb = 512

## Comportamiento del programa
define config.autosave_on_quit = False
define config.autosave_frequency = None
define config.autoreload = False
define config.has_autosave = False
define config.auto_load = None
define config.save_on_mobile_background = False
define config.rollback_enabled = False
define config.skipping = False
define _game_menu_screen = None
define config.help = False
define config.end_splash_transition = dissolve

define config.default_sfx_volume = 0.75
define config.default_voice_volume = 0.75
define config.quit_action = [SetVariable("inst.running", False), Quit(confirm =  False)]

define config.save_directory = config.savedir


## ------------------------------------------------------------------------------------------------------------- ##
## Área de empaquetado

init python:

    build.directory_name = "Watchdog_Alarm"

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.txt", None)
    build.classify("game/**.rpy", None)

    ## Declaración de paquetes RPA
    build.archive("program_data", "windows")

    ## Empaquetado del programa (RPA)
    build.classify("game/**.rpyc", "program_data")
    build.classify("game/audio/**.ogg", "program_data")
    build.classify("game/gui/**.png", "program_data")
    build.classify("game/gui/**.ttf", "program_data")
    build.classify("game/images/**.jpg", "program_data")
    build.classify("game/images/**.png", "program_data")
    build.classify("game/python-packages/**.py", "program_data")
    build.classify("game/python-packages/**.exe", "program_data")
    build.classify("game/python-packages/**.pyc", "program_data")
    build.classify("game/python-packages/**.pyo", "program_data")
