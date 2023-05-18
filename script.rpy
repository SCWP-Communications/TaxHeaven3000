




define i = Character("Iris", window_background=Image("gui/textbox-iris.png", xalign=0.4, yalign=1.0), color="#FFFFFF", who_outlines=[ (2, "#640C35"), (2, "#640C35", 2, 2) ], what_outlines=[ (2, "#FFFFFF") ])
define narrator = Character(None, what_color="#510469", what_outlines=[ (2, "#FFFFFF") ], window_background=Image("gui/textbox.png", xalign=0.4, yalign=1.0))


label start:
    jump scene_0_intro
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
