image transition_1 = Movie(loop = True, size=(1920, 1080), play = "gui/transitions/chibi-1.webm")
image transition_2 = Movie(loop = True, size=(1920, 1080), play = "gui/transitions/chibi-2.webm")
image transition_3 = Movie(loop = True, size=(1920, 1080), play = "gui/transitions/chibi-3.webm")
image transition_4 = Movie(loop = True, size=(1920, 1080), play = "gui/transitions/chibi-4.webm")
image transition_5 = Movie(loop = True, size=(1920, 1080), play = "gui/transitions/chibi-5.webm")

label scene_transition(next_label="scene_4b"):
    call scene_transition_main (next_label=next_label) from _call_scene_transition_main
    scene onlayer master
    with wiperight

label scene_transition_main(next_label):
    window hide
    $ show_overlay = False
    stop music fadeout 1.0
    play sound "audio/wipe.ogg"
    show expression f"transition_{dates_completed}"
    with ImageDissolve("gui/transitions/wiperight.png", 0.6, ramplen=20, alpha=True)
    pause 0.8
    $ show_overlay = True
    $ renpy.transition(ImageDissolve("gui/transitions/wiperight.png", 0.6, ramplen=20, alpha=True))
    call expression (next_label) from _call_expression
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
