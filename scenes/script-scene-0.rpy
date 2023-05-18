label scene_0_intro:
    scene bg apartment
    play music "audio/main_theme.ogg" fadein 0.5
    $ show_overlay = False
    jump scene_0_name_entry

label scene_0_name_entry:
    $ purge_saves()
    show screen multi_line_input(NAME_VALUES, headline="Your name", x_pos=0.5, y_pos=0.4, xalign=0.5, yalign=0.4, variant="narrator")
    "What is my name?"

    while first_name == "" or last_name == "" or get_error_message_by_id("first_name") is not None or get_error_message_by_id("last_name") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if get_error_message_by_id("first_name") is None and get_error_message_by_id("last_name") is None:
            if first_name == "":
                $ add_error("first_name", "You must respond!")
            if last_name == "":
                $ add_error("last_name", "You must respond!")
            $ renpy.restart_interaction()

        "What is my name?"
    $ purge_saves()
    hide screen multi_line_input
    stop music fadeout 0.5
    call scene_transition ("scene_1_intro") from _call_scene_transition_7
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
