label scene_5_intro:
    scene bg library
    if not first_diary_visit_completed:
        jump diary_tutorial_intro
    elif True:
        jump scene_5_diary

label scene_5_diary(text='Iris records just about every detail of our interactions here. If something isn\'t right I can change it so I know she has the correct information about me'):
    stop music
    play music "audio/diary_theme.ogg" fadein 1.0
    scene bg library

    show screen diary_main

    call scene_5_diary_say_dialogue (text=text) from _call_scene_5_diary_say_dialogue

label scene_5_diary_say_dialogue(text='Iris records just about every detail of our interactions here. If something isn\'t right I can change it so I know she has the correct information about me'):
    $ in_diary = True
    $ ctc_disabled = True
    $ renpy.say(None, text + '{fast}')
    hide screen diary_main with dissolve
    $ ctc_disabled = False

    if not (cafe_visited and office_visited and first_diary_visit_completed and not library_visited):
        "Okay, that’s enough of that. Looks like everything Iris knows about me is accurate. I’d better get out of here before she comes back to her desk."
        $ purge_saves()
    elif True:
        "I’ll just talk a walk through the aisles for a minute to until she comes back to her desk and then I can go talk to her."
        $ purge_saves()

    if not first_diary_visit_completed:
        $ in_diary = False
        call scene_transition ("scene_5_library_text") from _call_scene_transition_56
    elif cafe_visited and office_visited and not library_visited:
        jump scene_8_diary_segue
    elif cafe_visited and library_visited and office_visited:
        $ in_diary = False
        call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_36
    elif True:
        $ in_diary = False
        call scene_transition from _call_scene_transition_37

label scene_5_diary_recurring:
    scene bg library
    play music "audio/main_theme.ogg" fadein 0.5
    "This little library is starting to feel familiar. I understand why Iris enjoys spending time here."
    jump scene_5_diary_recurring_choice

label scene_5_diary_recurring_choice:
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Edit Iris' notebook", no_text="Examine Iris' desk", has_what=True, what_text="Leave"), variant="narrator")
    "Looks like she’s not at her desk right now. Her notebook is sitting out though."

    while screener_choice == None:
        "Looks like she’s not at her desk right now. Her notebook is sitting out though."

    hide screen screener_choice
    if screener_choice == True:
        jump scene_5_diary
    elif screener_choice == False:
        jump scene_5_iris_desk
    elif True:
        if cafe_visited and library_visited and office_visited:
            call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_33
        elif True:
            call scene_transition from _call_scene_transition_34

label scene_5_iris_desk:
    if len(books_iris_is_reading) == 1:
        "[books_iris_is_reading[0]]"
    elif len(books_iris_is_reading) == 2:
        "[books_iris_is_reading[1]]"
    elif True:
        "[books_iris_is_reading[2]]"

    jump scene_5_diary_recurring_choice

label scene_5_library_text:
    $ show_overlay = True
    scene bg library sunset
    pause 0.8
    play music "audio/main_theme.ogg" fadein 0.5
    hide screen diary_main
    "There's still no sign of Iris."

    play sound "audio/text_message.ogg"
    "Hang on a second, looks like I got a text message just a moment ago."

    show screen multiple_texts
    "It sounds like I won't get to see her today after all."
    hide screen multiple_texts
    "Well, at the very least I was able to edit my information in her diary."
    "If I'm correct, it seems like she reviews that diary every morning, so she'll now know my name properly."
    $ first_diary_visit_completed = True
    scene black with fade
    jump scene_5_plus

label diary_tutorial_intro:
    $ active_input_field_id = None
    $ diary_tutorial_can_edit_last_name = False
    play music "audio/main_theme.ogg" fadein 0.5
    "As I walk through the doors of the library I smell the comforting aroma of old paper and dust."
    "Libraries are like memorials to a bygone age of public amenities. There’s an air of solemnity over an otherwise cozy space."
    "Now, to figure out where Iris is."
    "..."
    "There’s a library assistant’s desk toward the front with a familiar pink notebook on it. It really is recognizable."
    "I don’t see Iris though. Maybe she’s off in the stacks shelving books or something."
    $ screener_choice = None
    scene bg library
    show screen diary_closed
    show screen choice_input("screener_choice", choices=YES_OR_NO_CHOICES, variant="narrator")
    "Her notebook is sitting there temptingly...should I peek at it?"

    while screener_choice is None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Her notebook is sitting there temptingly...should I peek at it?"

    hide screen choice_input
    if screener_choice is True:
        jump diary_tutorial_start
    elif True:
        $ screener_choice = None
        show screen choice_input("screener_choice", choices=[{"display": "Yes", "value": True}, {"display": "No", "value": False}], variant="narrator")
        "Butttttt maybe just a little peek?"
        while screener_choice is None:
            play sound "audio/error_beep.ogg" volume 0.3
            $ add_error("screener_choice", "You must respond!")
            "Butttttt maybe just a little peek??"

        hide screen choice_input

        if screener_choice:
            jump diary_tutorial_start
        elif True:
            $ screener_choice = None
            show screen choice_input("screener_choice", choices=[{"display": "Yes", "value": True}, {"display": "Stop kidding yourself, you have to look", "value": False}], variant="narrator")
            "What if I’m interested in starting my own diary some day? Wouldn’t it be useful to know what a well-organized one looks like?"

            while screener_choice is None:
                play sound "audio/error_beep.ogg" volume 0.3
                $ add_error("screener_choice", "You must respond!")
                "What if I’m interested in starting my own diary some day? Wouldn’t it be useful to know what a well-organized one looks like?"

            hide screen choice_input
            jump diary_tutorial_start

label diary_tutorial_start:
    stop music
    play music "audio/diary_theme.ogg" fadein 1.0
    hide screen diary_closed
    show screen diary_main
    $ in_diary_tutorial = True
    $ _diary_section = 0
    $ _diary_page = 0
    "Just a quick look is all. What's the harm?"

    $ _diary_section = 1
    $ _diary_page = 0
    "Wow this is...\n...A SHOCKINGLY literal transcription of Iris' day-to-day activities in exhastive detail."
    "I can see notes where she has gone back and annotated past events with updates and cross-references."
    "It’s like this notebook is her outsourced memory."

    $ _diary_section = 2
    $ _diary_page = 0
    $ last_name = DUMMY_LAST_NAME
    "Oh wow. This part is about me!\nThis is pretty much everything that we've talked about since we met"
    "Hang on a second - does Iris think I have \"[DUMMY_LAST_NAME]\" as a last name? Why did she write that? That’s definitely not right."
    "Damn, that’s what I do in my phone contacts when I can’t remember someone’s name."
    "Maybe I didn’t make as memorable an impression as I thought…"
    "I don’t want her to have incorrect information about me. Especially since it looks like she re-reads these pages with some regularity."

    hide screen diary_main
    show pencil_eraser at pen_center, easein
    "Since Iris gave me the exact technical pencil and eraser she uses.\nI can mimic her writing perfectly"
    hide pencil_eraser
    show screen diary_main with Dissolve(0.5)
    $ _diary_section = 2
    $ _diary_page = 0

    $ ctc_disabled = True
    $ add_error("last_name", "Enter your real last name")
    $ diary_tutorial_can_edit_last_name = True
    $ variable_change_callbacks.update({'last_name': disable_ctc_if_last_name_changed})
    "I should probably edit this line to be my real last name. I guess in the future if I ever need to correct anything I tell her I know how to do it"
    while last_name == DUMMY_LAST_NAME or get_error_message_by_id('last_name') is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        "I should probably edit this line to be my real last name. I guess in the future if I ever need to correct anything I tell her I know how to do it..."
    $ clear_error_by_id("last_name")
    $ variable_change_callbacks.pop('last_name', None)
    $ renpy.restart_interaction()
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="Continue flipping through the pages", no_text="Close the notebook"), variant="narrator")
    "Alright, all fixed\nShould I keep looking at this, or close it?"
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Alright, all fixed\nShould I keep looking at this, or close it?"

    hide screen choice_input
    $ in_diary_tutorial = False
    $ purge_saves()
    if screener_choice == True:
        call scene_5_diary from _call_scene_5_diary
    elif True:
        hide screen diary_main with dissolve
        call scene_transition ("scene_5_library_text") from _call_scene_transition_57

label scene_5_plus:
    scene black
    stop music fadeout 1.0
    play sound "audio/new_day.ogg"
    pause 3
    scene bg apartment with dissolve

    play music "audio/main_theme.ogg" fadein 0.5
    play sound "audio/text_message.ogg"
    show screen text_scene_2_1

    pause 1.5
    play sound "audio/text_message.ogg"
    show screen text_scene_2_2

    pause 1.5
    play sound "audio/text_message.ogg"
    show screen text_scene_2_3

    "Iris texted! Where should we go for our make-up date?"
    hide screen text_scene_2_1
    hide screen text_scene_2_2
    hide screen text_scene_2_3 
    with dissolve

    $ show_overlay = False
    jump scene_4b
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
