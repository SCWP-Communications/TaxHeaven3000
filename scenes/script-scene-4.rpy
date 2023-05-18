label scene_4a:
    scene bg sidewalk
    window hide
    pause 1
    play music "audio/main_theme.ogg" fadein 0.5
    jump scene_4a_map

label scene_4a_map:
    $ map_selected_screen = None
    play sound "audio/map_unfold.ogg"
    show screen map

    $ ctc_disabled = True
    while map_selected_screen == None:
        "Alright, where should I go?{nw}{fast}"

    while True:
        $ ctc_disabled = False
        if map_selected_screen == "the cafe":
            "I’ve got plenty of time. I guess I could stop by the cafe. But maybe it would be better to go straight to the library."
            if map_selected_screen == "the cafe":
                $ map_selected_screen = None
                hide screen map
                if not scene_6b_completed:
                    call scene_transition ("scene_6b_intro") from _call_scene_transition_19
                elif True:
                    call scene_transition ("scene_6d_intro") from _call_scene_transition_26
        elif map_selected_screen == "the library":
            "This must be where Iris works. I should go see if I can find her!"
            if map_selected_screen == "the library":
                $ map_selected_screen = None
                hide screen map
                call scene_transition ("scene_5_intro") from _call_scene_transition_1

label scene_4b:
    $ show_overlay = True
    if first_diary_visit_completed and not cafe_visited and not library_visited and not office_visited:
        scene bg sidewalk with dissolve
    elif True:
        scene bg sidewalk
        window hide
        pause 1
        play music "audio/main_theme.ogg" fadein 0.5
    jump scene_4b_map

label scene_4b_map:
    $ map_selected_screen = None
    play sound "audio/map_unfold.ogg"
    show screen map
    $ ctc_disabled = True

    while map_selected_screen == None:
        "Where should I go?"

    while True:
        $ ctc_disabled = False
        if map_selected_screen == "the office":
            if not office_visited:
                "I think Iris said she wanted me to keep her company while she went to the office building."
            elif True:
                "The library branch office, a generic corporate building."
            if map_selected_screen == "the office":
                hide screen map
                $ map_selected_screen = None
                if not office_visited:
                    call scene_transition ("scene_7_intro") from _call_scene_transition_2
                elif not scene_7b_completed:
                    call scene_transition ("scene_7b_intro") from _call_scene_transition_15
                elif True:
                    call scene_transition ("scene_7c_intro") from _call_scene_transition_38
        elif map_selected_screen == "the cafe":
            if not cafe_visited:
                "Should I meet Iris at the cafe? This could be my chance to get to know her better!"
            elif True:
                "The local coffeeshop. Nothing fancy, but nice."
            if map_selected_screen == "the cafe":
                hide screen map
                $ map_selected_screen = None
                if (not first_diary_visit_completed and not scene_6b_completed) or (cafe_visited and not scene_6b_completed):
                    call scene_transition ("scene_6b_intro") from _call_scene_transition_20
                elif (not first_diary_visit_completed and scene_6b_completed):
                    call scene_transition ("scene_6d_intro") from _call_scene_transition_51
                elif not cafe_visited:
                    call scene_transition ("scene_6_intro") from _call_scene_transition_3
                elif not scene_6c_completed:
                    call scene_transition ("scene_6c_intro") from _call_scene_transition_21
                elif True:
                    call scene_transition ("scene_6d_intro") from _call_scene_transition_22
        elif map_selected_screen == "the library":
            if cafe_visited and office_visited and not library_visited:
                "Iris asked me to come find her at the library… sounds like she’ll be there this time."
            elif True:
                "The library where Iris works. I can edit her diary here if I need to."
            if map_selected_screen == "the library":
                hide screen map
                $ map_selected_screen = None
                if not first_diary_visit_completed:
                    call scene_transition ("scene_5_intro") from _call_scene_transition_25
                elif first_diary_visit_completed and office_visited and cafe_visited and not library_visited:
                    call scene_transition ("scene_8_intro") from _call_scene_transition_4
                elif first_diary_visit_completed and not scene_5c_completed:
                    call scene_transition ("scene_5c_intro") from _call_scene_transition_23
                elif first_diary_visit_completed and office_visited and cafe_visited and library_visited and scene_5c_completed and not scene_5d_completed:
                    call scene_transition ("scene_5d_intro") from _call_scene_transition_24
                elif True:
                    call scene_transition ("scene_5_diary_recurring") from _call_scene_transition_5
        elif True:

            "Hmmmm... should I go to %(map_selected_screen)s?"
            if map_selected_screen == "Iris' house":
                hide screen map

                $ map_selected_screen = None
                if not iris_home_visited:
                    call scene_transition ("scene_9_intro") from _call_scene_transition_6


label scene_4c:
    $ map_selected_screen = None
    $ show_overlay = True
    scene bg sidewalk
    pause 1
    play music "audio/main_theme.ogg" fadein 0.5
    "Today’s another lovely day!"
    "What now?"
    "It sounded like Iris wanted to take things to the next level in our relationship"
    "Am I ready for that?"
    jump scene_4c_map

label scene_4c_map_short_intro:
    $ map_selected_screen = None
    $ show_overlay = True
    scene bg sidewalk
    pause 1
    play music "audio/main_theme.ogg" fadein 0.5
    jump scene_4c_map

label scene_4c_map:
    scene bg sidewalk
    $ ctc_disabled = True
    play sound "audio/map_unfold.ogg"
    show screen map
    "Alright, where should I go?"

    while map_selected_screen == None:
        "Alright, where should I go?"

    $ ctc_disabled = False

    while True:

        if map_selected_screen == "the office":
            "The library branch office, a generic corporate building."
            if map_selected_screen == "the office":
                hide screen map
                $ map_selected_screen = None
                if not scene_7b_completed:
                    call scene_transition ("scene_7b_intro") from _call_scene_transition_16
                elif True:
                    call scene_transition ("scene_7c_intro") from _call_scene_transition_39
        elif map_selected_screen == "the cafe":
            "The local coffeeshop. Nothing fancy, but nice."
            if map_selected_screen == "the cafe":
                hide screen map
                $ map_selected_screen = None
                if (cafe_visited and not scene_6b_completed):
                    call scene_transition ("scene_6b_intro") from _call_scene_transition_18
                elif not scene_6c_completed:
                    call scene_transition ("scene_6c_intro") from _call_scene_transition_27
                elif True:
                    call scene_transition ("scene_6d_intro") from _call_scene_transition_28
        elif map_selected_screen == "the library":
            "The library where Iris works. I can edit her diary here if I need to. I should make sure everything Iris knows about me is correct before I go see her at her house."
            if map_selected_screen == "the library":
                hide screen map
                $ map_selected_screen = None
                if not scene_5c_completed:
                    call scene_transition ("scene_5c_intro") from _call_scene_transition_31
                elif not scene_5d_completed:
                    call scene_transition ("scene_5d_intro") from _call_scene_transition_32
                elif True:
                    call scene_transition ("scene_5_diary_recurring") from _call_scene_transition_35
        elif True:
            "Iris sounded pretty serious the other day. I should be ready for some real commitment before I go here."
            if map_selected_screen == "Iris' house":
                hide screen map

                $ map_selected_screen = None
                call scene_transition ("scene_9_intro") from _call_scene_transition_30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
