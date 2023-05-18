image presplash:
    xsize 1920
    ysize 1080
    "gui/presplash.png"

label splashscreen:
    show presplash with dissolve
    pause 2

    scene black with dissolve
    show screen disclaimer
    pause 4
    hide screen disclaimer with dissolve
    show screen trailer
    pause 56
    hide screen trailer with dissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
