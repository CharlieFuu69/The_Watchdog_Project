## CharlieFuu69
## (2022) The Watchdog Project

## Script: Animaciones con ATL (Ren'Py).

#############################################################

transform title_alpha(timeset = (0.01, 0.01), x = 0.0):
    xanchor 0.5
    xpos x

    block:
        alpha 0.0
        pause timeset[0]
        ease 0.4 alpha 1.0
        pause timeset[1]
        ease 0.3 alpha 0.0


transform alpha_ctrl(off = 0.01, a = 1.0, delay = 1.0):
    subpixel True

    on start:
        alpha 0.0
        pause off
        ease delay alpha a

    on hide:
        alpha a
        ease delay alpha 0.0

transform splitline(x, bef, aft, off = 0.01):
    subpixel True
    xanchor 0.5
    xpos x

    on start:
        xysize(bef[0], bef[1])
        pause off
        easein_quint 0.3 xysize(aft[0], aft[1])

    on hide:
        xysize(aft[0], aft[1])
        easeout_quint 0.2 xysize(bef[0], bef[1])


transform scanner(xy = (0.0, 0.0), delta = 1.0):
    subpixel True
    anchor(0.5, 0.5)
    pos(xy[0], xy[1])

    block:
        parallel:
            zoom 0.0
            pause delta
            linear 0.75 zoom 0.3
        parallel:
            alpha 1.0
            pause delta
            ease 0.75 alpha 0.0
        repeat
