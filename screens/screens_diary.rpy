screen diary_main(next_screen=None):
    if not in_diary_tutorial:
        on "show" action Function(evaluate_errors_and_add_diary_pages, changed=None, evaluate_all=True)
    if not in_diary_review and not in_diary_review_bank_info and not in_diary_tutorial:
        on "show" action SetVariable("_diary_section", 0)
        on "show" action SetVariable("_diary_page", 0)
        on "call" action SetVariable("_diary_section", 0)
        on "call" action SetVariable("_diary_page", 0)
        on "show" action SetVariable("diary_bookmark_index", len(personal_diary_pages) - 1)
        on "call" action SetVariable("diary_bookmark_index", len(personal_diary_pages) - 1)
    on "show" action SetVariable("in_diary", True)
    on "call" action SetVariable("in_diary", True)
    on "hide" action SetVariable("in_diary", False)
    on "hide" action Function(clear_errors)
    on "show" action SetVariable("should_close_diary_error_modal", False)
    on "call" action SetVariable("should_close_diary_error_modal", False)

    use diary_error_modal()

    vbox at easein_fast:
        on "show" action SetVariable("_diary_section", 0)
        on "show" action SetVariable("_diary_page", 0)
        style_prefix "diary_main"
        xsize 1209
        xalign 0.5
        ypos 0
        ysize 608
        spacing 43

        hbox:
            yalign 0.5
            xalign 0.5
            xsize 1209
            ysize 608
            if not in_diary_tutorial:
                button:
                    hover_sound "audio/button_click.ogg"
                    style "diary_page_button"
                    if not in_diary_review_bank_info or (in_diary_review_bank_info and not (_diary_section == len(diary_sections) - 1 and _diary_page == len(diary_sections[_diary_section]['pages']) - 2)):
                        if _diary_section == 0 and _diary_page == 0:
                            background Frame("gui/diary/buttons/back-inactive.png")
                            action None
                            if in_diary_review or in_diary_review_bank_info:
                                background Frame("gui/diary/buttons/arrow_back-inactive.png")
                                xsize 175
                                ysize 80
                        else:
                            background Frame("gui/diary/buttons/back-idle.png")
                            hover_background Frame("gui/diary/buttons/back-hover.png")
                            if in_diary_review or in_diary_review_bank_info:
                                background Frame("gui/diary/buttons/arrow_back.png")
                                hover_background Frame("gui/diary/buttons/arrow_back-hover.png")
                                action [ChangeDiaryPage(forwards=False), Function(play_random_paper_sound), Function(has_error_on_current_page), Function(jump_to_correct_dialogue_for_diary_review)]
                                xsize 175
                                ysize 80
                            else:
                                action [ChangeDiaryPage(forwards=False), Function(play_random_paper_sound)]
                    else:
                        if in_diary_review or in_diary_review_bank_info:
                            xsize 175
                            ysize 80
                        background None
                        hover_background None
                        action None

                    xalign 0
            use diary_book()
            if not in_diary_tutorial:
                button:
                    hover_sound "audio/button_click.ogg"
                    style "diary_page_button"
                    if ((in_diary_review and not has_error_on_current_diary_page) or not in_diary_review) and ((in_diary_review_bank_info and not has_error_on_current_diary_page) or not in_diary_review_bank_info):
                        if in_diary_review and _diary_section == len(diary_sections) - 1 and _diary_page == len(diary_sections[_diary_section]['pages']) - 2:
                            if error == False:
                                background Frame("gui/diary/buttons/arrow_confirm.png")
                                hover_background Frame("gui/diary/buttons/arrow_confirm-hover.png")
                                action Hide(), Jump("scene_9_ready_for_refund"), Function(play_random_paper_sound)
                                xsize 179
                                ysize 80
                            else:
                                xsize 179
                                ysize 80
                                background None
                                hover_background None
                                action None
                        elif not in_diary_review and (_diary_section == len(diary_sections) - 1 and _diary_page == len(diary_sections[_diary_section]['pages']) - 1):
                            if in_diary_review_bank_info:
                                background Frame("gui/diary/buttons/arrow_confirm.png")
                                hover_background Frame("gui/diary/buttons/arrow_confirm-hover.png")
                                action Hide(), Jump("scene_9_banking_info_diary_review_ended"), Function(play_random_paper_sound)
                                xsize 179
                                ysize 80
                            else:
                                action None
                                background Frame("gui/diary/buttons/next-inactive.png")
                        elif in_diary_review or in_diary_review_bank_info:
                            background Frame("gui/diary/buttons/arrow_confirm.png")
                            hover_background Frame("gui/diary/buttons/arrow_confirm-hover.png")
                            xsize 179
                            ysize 80
                            action [ChangeDiaryPage(), Function(play_random_paper_sound), Function(has_error_on_current_page), Function(jump_to_correct_dialogue_for_diary_review)]
                        else:
                            background Frame("gui/diary/buttons/next-idle.png")
                            hover_background Frame("gui/diary/buttons/next-hover.png")
                            action [ChangeDiaryPage(), Function(play_random_paper_sound)]
                    else:
                        if in_diary_review or in_diary_review_bank_info:
                            xsize 179
                            ysize 80
                        background None
                        hover_background None
                        action None
                    xalign 1.0

    if not in_diary_tutorial and not in_diary_review and not in_diary_review_bank_info:
        button:
            hover_sound "audio/button_click.ogg"
            background Frame("gui/diary/buttons/exit.png")
            hover_background Frame("gui/diary/buttons/exit-hover.png")
            if next_screen is not None:
                action Jump(next_screen), Hide()
            else:
                action Return(True)
            xsize 79
            ysize 76
            xpos 1372
            ypos 36

style diary_main_text:
    font gui.diary_commentary_font
    size gui.diary_commentary_font_size
    color gui.diary_commentary_color
    outlines gui.diary_commentary_outlines
    text_align 0.5
    ypos 0
    xalign 0.5
    xsize 594
    ysize 85

style diary_page_button:
    xsize 105
    ysize 80
    yalign 0.5
    padding (0, 0, 0, 0)

screen diary_book():
    frame:
        if diary_sections[_diary_section]['id'] == "first_page":
            background Frame(f"gui/diary/page_backgrounds/page_intro.png")
        else:
            background Frame(f"gui/diary/page_backgrounds/page_regular.png")

        if not in_diary_tutorial and not in_diary_review and not in_diary_review_bank_info:

            button:
                action Function(jump_to_bookmarked_page), Function(play_random_paper_sound)
                if _diary_page == diary_bookmark_index and _diary_section == 1:
                    background Frame("gui/diary/buttons/bookmark_full.webp")
                else:
                    background Frame("gui/diary/buttons/bookmark_top.webp")

                if _diary_page == diary_bookmark_index and _diary_section == 1:
                    xpos 46
                    ypos -35
                    xsize 39
                    ysize 285
                elif _diary_section < 2:
                    xpos 820
                    ypos -34
                    xsize 39
                    ysize 39
                else:
                    xpos 46
                    ypos -35
                    xsize 39
                    ysize 39


        xsize 928
        ysize 622
        xalign 0.5
        yalign 0.5

        $ renpy.dynamic("page_0_xpos", "page_0_ypos", "page_1_xpos", "page_1_ypos", "page_2_xpos", "page_2_ypos","page_3_xpos", "page_3_ypos", "page_0_idle_image", "page_1_idle_image", "page_2_idle_image", "page_0_hover_image", "page_1_hover_image", "page_2_idle_image", "page_2_hover_image", "page_0_ysize", "page_1_ysize", "page_2_ysize", "page_0_diary_section", "page_1_diary_section", "page_2_diary_section")

        if _diary_section in [0, 1]:
            $ page_2_xpos = 869
            $ page_2_ypos = 10
            $ page_1_xpos = 869
            $ page_1_ypos = 190
            $ page_0_xpos = 869
            $ page_0_ypos = 285
            $ page_2_idle_image = "gui/diary/buttons/tabs/tab_0_right.png"
            $ page_2_hover_image = "gui/diary/buttons/tabs/tab_0_right_hover.png"
            $ page_1_idle_image = "gui/diary/buttons/tabs/tab_1_right.png"
            $ page_1_hover_image = "gui/diary/buttons/tabs/tab_1_right_hover.png"
            $ page_0_idle_image = "gui/diary/buttons/tabs/tab_2_right.png"
            $ page_0_hover_image = "gui/diary/buttons/tabs/tab_2_right_hover.png"
            $ page_2_ysize = 198
            $ page_1_ysize = 125
            $ page_0_ysize = 222
            $ page_2_diary_section = 2
            $ page_1_diary_section = 3
            $ page_0_diary_section = 4
        elif _diary_section == 2:
            $ page_0_xpos = -2
            $ page_0_ypos = 10
            $ page_2_xpos = 869
            $ page_2_ypos = 190
            $ page_1_xpos = 869
            $ page_1_ypos = 285
            $ page_0_idle_image = "gui/diary/buttons/tabs/tab_0_left.png"
            $ page_0_hover_image = "gui/diary/buttons/tabs/tab_0_left_hover.png"
            $ page_2_idle_image = "gui/diary/buttons/tabs/tab_1_right.png"
            $ page_2_hover_image = "gui/diary/buttons/tabs/tab_1_right_hover.png"
            $ page_1_idle_image = "gui/diary/buttons/tabs/tab_2_right.png"
            $ page_1_hover_image = "gui/diary/buttons/tabs/tab_2_right_hover.png"
            $ page_0_ysize = 198
            $ page_2_ysize = 125
            $ page_1_ysize = 222
            $ page_0_diary_section = 2
            $ page_2_diary_section = 3
            $ page_1_diary_section = 4
        elif _diary_section == 3:
            $ page_0_xpos = -2
            $ page_0_ypos = 10
            $ page_1_xpos = -2
            $ page_1_ypos = 190
            $ page_2_xpos = 869
            $ page_2_ypos = 285
            $ page_0_idle_image = "gui/diary/buttons/tabs/tab_0_left.png"
            $ page_0_hover_image = "gui/diary/buttons/tabs/tab_0_left_hover.png"
            $ page_1_hover_image = "gui/diary/buttons/tabs/tab_1_left_hover.png"
            $ page_1_idle_image = "gui/diary/buttons/tabs/tab_1_left.png"
            $ page_2_idle_image = "gui/diary/buttons/tabs/tab_2_right.png"
            $ page_2_hover_image = "gui/diary/buttons/tabs/tab_2_right_hover.png"
            $ page_0_ysize = 157
            $ page_1_ysize = 187
            $ page_2_ysize = 102
            $ page_0_diary_section = 2
            $ page_1_diary_section = 3
            $ page_2_diary_section = 4
        elif _diary_section == 4:
            $ page_0_xpos = -2
            $ page_0_ypos = 10
            $ page_1_xpos = -2
            $ page_1_ypos = 190
            $ page_2_xpos = -2
            $ page_2_ypos = 285
            $ page_0_idle_image = "gui/diary/buttons/tabs/tab_0_left.png"
            $ page_0_hover_image = "gui/diary/buttons/tabs/tab_0_left_hover.png"
            $ page_1_idle_image = "gui/diary/buttons/tabs/tab_1_left.png"
            $ page_1_hover_image = "gui/diary/buttons/tabs/tab_1_left_hover.png"
            $ page_2_idle_image = "gui/diary/buttons/tabs/tab_2_left.png"
            $ page_2_hover_image = "gui/diary/buttons/tabs/tab_2_left_hover.png"
            $ page_0_ysize = 198
            $ page_1_ysize = 125
            $ page_2_ysize = 222
            $ page_0_diary_section = 2
            $ page_1_diary_section = 3
            $ page_2_diary_section = 4
        button:
            background page_0_idle_image
            hover_background page_0_hover_image
            xsize 25
            ysize page_0_ysize
            xpos absolute(page_0_xpos)
            ypos absolute(page_0_ypos)
            if not in_diary_tutorial and not in_diary_review and not in_diary_review_bank_info:
                action SetVariable("_diary_section", page_0_diary_section), SetVariable("_diary_page", 0), Function(play_random_paper_sound)
        button:
            background page_1_idle_image
            hover_background page_1_hover_image
            xsize 25
            ysize page_1_ysize
            xpos absolute(page_1_xpos)
            ypos absolute(page_1_ypos)
            if not in_diary_tutorial and not in_diary_review and not in_diary_review_bank_info:
                action SetVariable("_diary_section", page_1_diary_section), SetVariable("_diary_page", 0), Function(play_random_paper_sound)
        button:
            background page_2_idle_image
            hover_background page_2_hover_image
            xsize 25
            ysize page_2_ysize
            xpos absolute(page_2_xpos)
            ypos absolute(page_2_ypos)
            if not in_diary_tutorial and not in_diary_review and not in_diary_review_bank_info:
                action SetVariable("_diary_section", page_2_diary_section), SetVariable("_diary_page", 0), Function(play_random_paper_sound)

        frame:
            id "left_side"
            if len(diary_sections[_diary_section]["pages"][_diary_page]["sections"]) > 0 and diary_sections[_diary_section]["pages"][_diary_page]["sections"][0]["display"] == "STUDENT STATUS":
                top_padding 17
            else:
                top_padding 34
            xpos 35
            ypos 0
            xsize 381
            ysize 575
            background None
            if diary_sections[_diary_section]['id'] == "personal_entries":
                style_prefix "diary_left_side"
                text diary_sections[_diary_section]["pages"][_diary_page]["sections"][0]["diary_entry"]

            if diary_sections[_diary_section]["pages"][_diary_page].get("sections") is not None:
                if (diary_sections[_diary_section]['id'] == "personal_details") or (diary_sections[_diary_section]['id'] == "income" and office_visited) or (diary_sections[_diary_section]['id'] == "credits_refund" and library_visited):
                    vbox:
                        spacing 10
                        xalign 0.5
                        if diary_sections[_diary_section]["pages"][_diary_page]["sections"][0].get("display", None) is not None:
                            use diary_section_title(diary_sections[_diary_section]["pages"][_diary_page]["sections"][0].get("display"))
                        else:
                            frame:
                                background None
                                ysize 29
                        vbox:
                            xalign 0.5
                            spacing 20
                            xmaximum 315


                            for field in diary_sections[_diary_section]["pages"][_diary_page]["sections"][0]["fields"]:
                                if (field["type"] == "input"):
                                    if field["display"] is not None:
                                        use diary_input_field_labeled(field["display"].format(first_name), field["value_name"], field["value_type"], prefix=field["prefix"], changed_function=field["changed_function"])
                                    else:
                                        use diary_input_field(field["value_name"], field["value_type"], prefix=field["prefix"], changed_function=field["changed_function"])
                                elif (field["type"] == "checkbox"):
                                    if field.get("options", None) is not None:
                                        use diary_checkbox_field(field["display"].format(first_name), field["value_name"], field["value_type"], options=field.get("options"))
                                    else:
                                        use diary_checkbox_field(field["display"].format(first_name), field["value_name"], field["value_type"])
                                elif (field["type"] == "static"):

                                    if field["display"] is not None:
                                        use diary_input_field_labeled(field["display"].format(first_name), field["value_name"], field["value_type"], prefix=field["prefix"], editable=False)
                                    else:
                                        use diary_input_field(field["value_name"], field["value_type"], prefix=field["prefix"], changed_function=field["changed_function"], editable=False)
                                elif (field["type"] == "file_empty"):

                                    use diary_empty_file(field["display"], field["description"], field["value_name"], pdf_type=PDF_TYPE_MAPPINGS[field["pdf_type"]])
                                elif (field["type"] == "file"):
                                    use diary_file_page(field["display"], field["value_name"], field["index"], pdf_type=PDF_TYPE_MAPPINGS[field["pdf_type"]])
                                elif (field["type"] == "results_text"):
                                    use diary_edu_credit_results_page(field["display"].format(first_name))
                                elif (field["type"] == "plaintext"):
                                    text field["display"].format(first_name):
                                        font gui.diary_entry_font
                                        size 15
                                        color gui.diary_entry_color
                                        outlines []


        if (diary_sections[_diary_section]['id'] == "personal_entries") or (diary_sections[_diary_section]['id'] == "personal_details") or (diary_sections[_diary_section]['id'] == "income" and office_visited) or (diary_sections[_diary_section]['id'] == "credits_refund" and library_visited):
            if diary_sections[_diary_section]["pages"][_diary_page]["sections"][0].get("background", None) is not None:
                frame:
                    background Frame(diary_sections[_diary_section]["pages"][_diary_page]["sections"][0].get("background"))
                    xpos 44
                    ypos 2
                    xsize 381
                    ysize 575
        frame:
            xpos absolute(485)
            ypos 0
            xsize 381
            ysize 550
            background None
            if len(diary_sections[_diary_section]["pages"][_diary_page]["sections"]) > 0 and diary_sections[_diary_section]["pages"][_diary_page]["sections"][0]["display"] == "STUDENT STATUS":
                top_padding 17
            else:
                top_padding 34






            if diary_sections[_diary_section]['id'] == "personal_entries" and len(diary_sections[_diary_section]["pages"][_diary_page]["sections"]) > 1:
                style_prefix "diary_left_side"
                text diary_sections[_diary_section]["pages"][_diary_page]["sections"][1]["diary_entry"]
            vbox:
                spacing 10
                xalign 0.5
                if (diary_sections[_diary_section]['id'] == "personal_details") or (diary_sections[_diary_section]['id'] == "income" and office_visited) or (diary_sections[_diary_section]['id'] == "credits_refund" and library_visited):
                    if len(diary_sections[_diary_section]["pages"][_diary_page]["sections"]) > 1 and diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("display", None) is not None:
                        use diary_section_title(diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("display"))
                    else:

                        frame:
                            background None
                            ysize 29
                vbox:
                    xalign 0.5
                    id "right_side"
                    spacing 20
                    xmaximum 315


                    if (diary_sections[_diary_section]['id'] == "personal_details") or (diary_sections[_diary_section]['id'] == "income" and office_visited) or (diary_sections[_diary_section]['id'] == "credits_refund" and library_visited):
                        if len(diary_sections[_diary_section]["pages"][_diary_page]["sections"]) > 1:
                            if (diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("if_condition", None) is not None and globals()[diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("if_condition")]) or diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("if_condition", None) is None:
                                for field in diary_sections[_diary_section]["pages"][_diary_page]["sections"][1]["fields"]:
                                    if (field["type"] == "input"):
                                        if field["display"] is not None:
                                            use diary_input_field_labeled(field["display"].format(first_name), field["value_name"], field["value_type"], prefix=field["prefix"], changed_function=field["changed_function"])
                                        else:
                                            use diary_input_field(field["value_name"], field["value_type"], prefix=field["prefix"], changed_function=field["changed_function"])
                                    elif (field["type"] == "checkbox"):
                                        if field.get("options", None) is not None:
                                            use diary_checkbox_field(field["display"].format(first_name), field["value_name"], field["value_type"], options=field.get("options"))
                                        else:
                                            use diary_checkbox_field(field["display"].format(first_name), field["value_name"], field["value_type"])
                                    elif (field["type"] == "static"):

                                        if field["display"] is not None:
                                            use diary_input_field_labeled(field["display"].format(first_name), field["value_name"], field["value_type"], prefix=field["prefix"], editable=False)
                                        else:
                                            use diary_input_field(field["value_name"], field["value_type"], prefix=field["prefix"], changed_function=field["changed_function"], editable=False)
                                    elif (field["type"] == "file"):
                                        use diary_file_page(field["display"], field["value_name"], field["index"], pdf_type=PDF_TYPE_MAPPINGS[field["pdf_type"]])
                                    elif (field["type"] == "results_edu_credit_option"):
                                        use diary_circled_result()
                                    elif (field["type"] == "results_text"):
                                        use diary_edu_credit_results_page(field["display"].format(first_name))
                                    elif (field["type"] == "address_input"):
                                        use diary_address_input(field["value_name"], field["display"], field["value_type"])
                                    elif (field["type"] == "plaintext"):
                                        text field["display"].format(first_name):
                                            font gui.diary_entry_font
                                            size 15
                                            color gui.diary_entry_color
                                            outlines []
                                            text_align 0.0
                                            xalign 0

                                if diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("stickies", None) is not None:

                                    use add_remove_stickies_non_file(diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("stickies"))
        if (diary_sections[_diary_section]['id'] == "personal_entries") or (diary_sections[_diary_section]['id'] == "personal_details") or (diary_sections[_diary_section]['id'] == "income" and office_visited) or (diary_sections[_diary_section]['id'] == "credits_refund" and library_visited):
            if len(diary_sections[_diary_section]["pages"][_diary_page]["sections"]) > 1 and diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("background", None) is not None:
                frame:
                    background Frame(diary_sections[_diary_section]["pages"][_diary_page]["sections"][1].get("background"))
                    xpos absolute(485)
                    ypos 2
                    xsize 381
                    ysize 550

style diary_tab_text:
    font gui.diary_tab_font
    size gui.diary_tab_font_size
    color gui.diary_tab_color
    xalign 0.5
    yalign 0.5

style diary_left_side_text:
    font gui.diary_entry_font
    size gui.diary_entry_font_size
    color gui.diary_entry_color

    xalign 0.5
    ypos absolute(68)
    xsize 285

screen diary_section_title(title, subtitle=False):
    frame:
        xsize 330
        style_prefix "diary_section_title"
        ysize 32
        if not subtitle:
            background Frame("gui/diary/marker_line_main.png")
        else:
            background Frame("gui/diary/marker_line_subsection.png")


        text f"{title}":
            xalign 0.5
            yanchor 0.5
            ypos 0.7
            text_align 0.5
            yfill True



style diary_section_title_frame:
    ysize 37
    xalign 0.5
    ypos 0

style diary_section_title_text:
    font gui.diary_entry_font
    size gui.diary_entry_font_size
    color gui.diary_entry_color


screen diary_input_field_labeled(label_text, value_name, value_type, prefix=None, changed_function="save_value_active_input", editable=True):
    vbox:
        style_prefix "diary_input_field_labeled"
        spacing 3
        xfill True
        text f"{label_text}:"
        use diary_input_field(value_name, value_type, prefix, changed_function, editable)

style diary_input_field_labeled_text:
    font gui.diary_entry_font
    size 15
    color gui.diary_entry_color

screen diary_input_field(value_name, value_type, prefix=None, changed_function="save_value_active_input", editable=True, xsize=315, max_chars=24):
    $ renpy.dynamic("_value")
    if "arr_prop" in value_type:
        $ _value = get_value_array_property(value_name)
    elif "prop" in value_type:
        $ _value = get_value_property(value_name)
    else:
        $ _value = globals()[value_name]

    frame:
        style_prefix "diary_input_field"
        background Frame("gui/diary/frame-input_field.png")
        ysize 49
        xsize xsize
        if get_error_message_by_id(value_name) is not None:
            frame:
                background Frame("gui/diary/errors/frame-input_field_error.png")
                xalign 0
                yalign 0.5
                xsize xsize - 10
                ysize 32
        if editable:
            if active_input_field_id != value_name:
                button:

                    xsize xsize - 10

                    if (not in_diary_tutorial or (in_diary_tutorial and value_name == "last_name" and diary_tutorial_can_edit_last_name)):
                        hover_background Color((108, 189, 228, 76.5))
                        hover_ysize 32
                        action SetVariable("active_input_field_id", value_name)
                    if _value == None:
                        $ _value = ''
                    elif value_type == "date" and (_value is not None):
                        $ _value =  f"{convert_date_to_displayable_string(_value)}"
                    elif "number" in value_type:
                        $ _value = "{0:.2f}".format(_value)
                    else:
                        $ _value = str(_value)

                    text f"{prefix if prefix is not None else ''}{get_ellipsized_value(_value, max_chars)}":
                        yalign 0.5
                        ysize 49
                        if get_error_message_by_id(value_name) is not None:
                            color gui.color_red
            else:
                hbox:
                    ysize 49
                    yalign 0.5
                    if prefix is not None:
                        text prefix style "diary_input_field_input"
                    input:
                        copypaste True
                        style "diary_input_field_input"
                        if value_type == "date":
                            if _value is not None:
                                default f"{convert_date_to_displayable_string(_value)}"
                            else:
                                default ""
                        else:
                            default f"{_value if _value is not None else ''}"
                        pixel_width xsize - 16
                        changed CHANGED_FUNCTIONS[changed_function]
                        ysize 49
                        length max_chars
                        if get_error_message_by_id(value_name) is not None:
                            color gui.color_red
        else:
            button:
                action None
                if _value == None:
                    $ _value = ''
                elif value_type == "date" and (_value is not None):
                    $ _value =  f"{convert_date_to_displayable_string(_value)}"
                elif "number" in value_type:
                    $ _value = "{0:.2f}".format(_value)
                else:
                    $ _value = str(_value)
                text f"{prefix if prefix is not None else ''}{_value}":
                    yalign 0.5
                    ysize 49
                    color gui.diary_uneditable_text_color
                    if get_error_message_by_id(value_name) is not None:
                        color gui.color_red

style diary_input_field_button:
    ysize 49
    xsize 306
    yalign 0.5
    padding (0, 0, 0, 0)

style diary_input_field_text is diary_input_field_input

style diary_input_field_input:
    font gui.diary_input_field_font
    size gui.diary_input_field_font_size
    color gui.diary_input_field_color
    ysize 49
    yalign 0.5

screen diary_checkbox_field(label_text, value_name, value_type, options=YES_OR_NO_CHOICES):
    $ renpy.dynamic("options")
    vbox:
        xsize 315
        style_prefix "diary_checkbox_field"
        spacing 0
        text f"{label_text}:":
            if get_error_message_by_id(value_name) is not None:
                color gui.color_red

        for option in options:
            if "arr_prop" in value_type:
                use diary_checkbox(option, value_name, value_type, get_value_array_property(value_name) == option["value"])
            else:
                use diary_checkbox(option, value_name, value_type, globals()[value_name] == option["value"])

style diary_checkbox_field_text:
    font gui.diary_entry_font
    size 15
    color gui.diary_entry_color

screen diary_checkbox(option, value_name, value_type, selected=False):
    button:
        if "arr_prop" in value_type:
            action SetVariableArrayPropOption(value_name, option["value"], True)
        else:
            action SetVariableOption(value_name, option["value"], True)
        style_prefix "diary_checkbox"
        hbox:
            ypos 0.5
            yalign 0.5
            spacing 10
            frame:
                if selected:
                    background Image("gui/diary/checkbox-checked.png")
                else:
                    background Image("gui/diary/checkbox-unchecked.png")
                xsize 32
                ysize 32
                yalign 0.5
            label option["display"]:
                ysize 32


style diary_checkbox_label_text:
    font gui.diary_input_field_font
    size gui.diary_input_field_font_size
    color gui.diary_entry_color
    ypos 0.5
    yanchor 0.3

screen diary_circled_result():
    vbox:
        ypos 20
        style_prefix "diary_credit_circled_results"
        spacing 10
        xalign 0.5
        xsize 315
        frame:
            xfill True
            ysize 29
            xsize 315
            background Frame("gui/diary/marker_line_results.png")

            text "RESULTS":
                size 15

        text f"{first_name} is eligible to claim the...":
            size 18

        frame:
            if claiming_aoc:
                background Frame("gui/diary/frame_circled.png")
            else:
                background None

            text "American Opportunity Credit":
                size 18

        frame:
            if claiming_lllc:
                background Frame("gui/diary/frame_circled.png")
            else:
                background None

            text "Lifetime Learning Credit":
                size 18

style diary_credit_circled_results_frame:
    ysize 55
    xsize 280
    xalign 0.5

style diary_credit_circled_results_text is gui_text:
    font gui.diary_entry_font
    color gui.color_hot_pink
    text_align 0.5
    xalign 0.5
    ypos 0.6
    yanchor 0.5

screen diary_edu_credit_results_page(results_text):
    vbox:
        xalign 0.5
        ypos 150
        xfill True

        frame:
            xfill True
            ysize 29
            xsize 315
            background Frame("gui/diary/marker_line_results.png")

            text "RESULTS" style "diary_credit_circled_results_text":
                size 15

        text results_text style "diary_credit_circled_results_text":
            size 18

screen add_remove_stickies_non_file(stickies):
    hbox:
        ypos 0
        xalign 0.5
        spacing 10
        for key, val in stickies.items():
            if key == "add":
                use diary_post_it_non_file(button_type=key, value_name=val["value_name"], value_type=val["value_type"], form_type=val["display"], xpos=0, ypos=0, index=val["index"])
            else:
                use diary_post_it_non_file(button_type=key, value_name=val["value_name"], value_type=val["value_type"], form_type=val["display"], xpos=0, ypos=0, index=val["index"])

screen diary_post_it_non_file(button_type, value_name, value_type, form_type, xpos, ypos, index=None, xanchor=0, yanchor=0):
    $ renpy.dynamic("post_it_text")
    $ post_it_text = "{}{} {}?".format(button_type.capitalize(), ' additional' if button_type == 'add' else '', form_type)
    frame:
        background None
        ysize 178
        xsize 170
        style_prefix "diary_post_it"
        xpos xpos
        ypos ypos
        xanchor xanchor
        yanchor yanchor
        button:
            xalign 0.5
            yalign 0.5
            if button_type == "add":
                background "gui/diary/documents/post-its/green.png"
                hover_background "gui/diary/documents/post-its/green-hover.png"
                ysize 178
                xsize 170
                action Function(add_value_to_array, value_name, value_type)
            elif button_type == "remove":
                background Frame("gui/diary/documents/post-its/red.png")
                hover_background Frame("gui/diary/documents/post-its/red-hover.png")
                action Function(remove_index_from_array, value_name, index)
                ysize 141
                xsize 136

            text post_it_text:
                if button_type == "remove":
                    size gui.diary_post_it_font_size_sm
                    xsize 90
                else:
                    size gui.diary_post_it_font_size_lg
                    xsize 134

        use diary_washi_tape(button_type, 1)

screen diary_post_it(form_type, button_type, variant_number, value_name, xpos, ypos, index=None, xanchor=0, yanchor=0, pdf_type=PDF):


    $ renpy.dynamic("post_it_text")
    $ post_it_text = "{}{} form {}?".format(button_type.capitalize(), ' additional' if button_type == 'add' else '', form_type)
    frame:
        background None
        ysize 178
        xsize 170
        style_prefix "diary_post_it"
        xpos xpos
        ypos ypos
        xanchor xanchor
        yanchor yanchor
        button:
            xalign 0.5
            yalign 0.5
            if button_type == "replace":
                background Frame("gui/diary/documents/post-its/yellow.png")
                hover_background Frame("gui/diary/documents/post-its/yellow-hover.png")
                ysize 178
                xsize 170
                action Show("add_file_lightbox", None, value_name, form_type, post_function=evaluate_errors_and_add_diary_pages, replace=True, replacement_index=index, pdf_type=pdf_type)
            elif button_type == "remove":
                background Frame("gui/diary/documents/post-its/red.png")
                hover_background Frame("gui/diary/documents/post-its/red-hover.png")
                action Show("diary_file_removal_confirmation", None, value_name, form_type, index, post_function=evaluate_errors_and_add_diary_pages)
                ysize 141
                xsize 136
            elif button_type == "add":
                background "gui/diary/documents/post-its/green.png"
                hover_background "gui/diary/documents/post-its/green-hover.png"
                ysize 178
                xsize 170
                action Show("add_file_lightbox", None, value_name, form_type, post_function=evaluate_errors_and_add_diary_pages, pdf_type=pdf_type)

            text post_it_text:
                if button_type == "remove":
                    size gui.diary_post_it_font_size_sm
                    xsize 90
                else:
                    size gui.diary_post_it_font_size_lg
                    xsize 134

        use diary_washi_tape(button_type, variant_number)


style diary_post_it_text:
    color gui.color_maroon
    text_align 0.5
    xalign 0.5
    yalign 0.5
    font gui.diary_entry_font

screen diary_washi_tape(button_type, variant_number):
    transform:
        xsize 53
        ysize 223
        if button_type == "replace":
            if variant_number == 1:
                rotate 25
                frame:
                    background "gui/diary/documents/washi-tape/04.png"
                    xsize 53
                    ysize 223
                    xpos -125
                    ypos -80
            elif variant_number == 2:
                rotate 0
                frame:
                    background "gui/diary/documents/washi-tape/02.png"
                    xsize 53
                    ysize 223
                    xpos -155
                    ypos -50
            else:
                rotate 26
                frame:
                    background "gui/diary/documents/washi-tape/09.png"
                    xsize 53
                    ysize 223
                    xpos -120
                    ypos -80
        elif button_type == "add":
            if variant_number == 1:
                rotate -28
                frame:
                    background "gui/diary/documents/washi-tape/01.png"
                    xsize 53
                    ysize 223


                    xpos -150
                    ypos 20
            elif variant_number == 2:
                rotate -13
                frame:
                    background "gui/diary/documents/washi-tape/03.png"
                    xsize 53
                    ysize 223
                    xpos -150
                    ypos 0
            else:
                rotate -1
                frame:
                    background "gui/diary/documents/washi-tape/06.png"
                    xsize 53
                    ysize 223
                    xpos -140
                    ypos -40
        else:
            if variant_number == 1:
                rotate 5
                frame:
                    background "gui/diary/documents/washi-tape/07.png"
                    xsize 53
                    ysize 223
                    xpos -155
                    ypos -29
            elif variant_number == 2:
                rotate 5
                frame:
                    background "gui/diary/documents/washi-tape/06.png"
                    xsize 53
                    ysize 223
                    xpos -150
                    ypos -35
            else:
                rotate 4
                frame:
                    background "gui/diary/documents/washi-tape/05.png"
                    xsize 53
                    ysize 223
                    xpos -134
                    ypos -34

screen diary_empty_file(display, description, value_name, pdf_type=PDF):
    $ renpy.dynamic("variant_number", "rotation")
    $ variant_number = 1



    $ rotation = 10
    frame:
        xfill True
        yfill True
        background None
        style_prefix "diary_empty_file"
        transform:
            rotate rotation
            use diary_post_it(display, "add", variant_number, value_name, xpos=0.5, ypos=0.45, xanchor=0.5, yanchor=0.5, pdf_type=pdf_type)

        if description:
            text description

style diary_empty_file_text:
    size 18
    color gui.color_maroon
    xalign 0.5
    ysize 254
    yanchor 0.5
    ypos 0.95
    font gui.diary_entry_font
    text_align 0.5

screen diary_file_page(display, value_name, index, pdf_type=PDF):
    $ renpy.dynamic("preview_file_location", "file_object", "replace_button_xpos", "replace_button_ypos", "replace_button_rotation", "add_button_xpos", "add_button_ypos", "add_button_rotation", "remove_button_xpos", "remove_button_ypos", "remove_button_rotation", "button_variant")
    if index is not None:
        if len(globals()[value_name]) <= index:
            $ file_object = None
        else:
            $ file_object = globals()[value_name][index]
    else:
        $ file_object = globals()[value_name]

    if file_object != None:
        if renpy.macintosh:
            $ thumbnails = file_object.get_preview_images()
        else:
            $ thumbnails = []
        if index is None or index % 3 == 0:
            $ button_variant = 1
            $ replace_button_xpos = 45
            $ replace_button_ypos = 75
            $ replace_button_rotation = -18
            $ add_button_xpos = -40
            $ add_button_ypos = 250
            $ add_button_rotation = 11
            $ remove_button_xpos = 100
            $ remove_button_ypos = 240
            $ remove_button_rotation = 0
        elif index % 3 == 1:
            $ button_variant = 2
            $ replace_button_xpos = 60
            $ replace_button_ypos = 46
            $ replace_button_rotation = 8
            $ add_button_xpos = -30
            $ add_button_ypos = 178
            $ add_button_rotation = -3
            $ remove_button_xpos = 105
            $ remove_button_ypos = 260
            $ remove_button_rotation = 0
        elif index % 3 == 2:
            $ button_variant = 3
            $ replace_button_xpos = -13
            $ replace_button_ypos = -19
            $ replace_button_rotation = 30
            $ add_button_xpos = 100
            $ add_button_ypos = 119
            $ add_button_rotation = 11
            $ remove_button_xpos = 6
            $ remove_button_ypos = 250
            $ remove_button_rotation = -22


        frame:
            background None
            xfill True
            yfill True
            ypos -20

            if renpy.macintosh and len(thumbnails) > 0:
                frame:
                    ypos -62
                    xpos 245
                    xsize 29
                    ysize 112
                    background Frame("gui/diary/documents/paperclip-back.png")
                if len(thumbnails) > 1:
                    transform:
                        rotate 3
                        frame:
                            xanchor 0.5
                            xalign 0.501
                            ypos -115
                            xsize 311
                            ysize 403
                            background Color("#B8B8B8")
                    transform:
                        rotate 3
                        frame:
                            xalign 0.5
                            ypos -113
                            xsize 309
                            ysize 401
                            background Frame(im.Data(thumbnails[1], "eraser.png"))
                frame:
                    xalign 0.5
                    ypos -54
                    xsize 311
                    ysize 403
                    background Color("#B8B8B8")
                frame:
                    xalign 0.5
                    ypos -53
                    xsize 309
                    ysize 401
                    background Frame(im.Data(thumbnails[0], "eraser.png"))

                    button:
                        xalign 0.5
                        yalign 0.5
                        xsize 0.93
                        ysize 0.93
                        hover_background Color((108, 189, 228, 76))
                        action Show("file_lightbox", None, thumbnails)

                frame:
                    ypos -62
                    xpos 245
                    xsize 29
                    ysize 112
                    background Frame("gui/diary/documents/paperclip-front.png")
            else:
                frame:
                    ypos -62
                    xpos 245
                    xsize 29
                    ysize 112
                    background Frame("gui/diary/documents/paperclip-back.png")
                transform:
                    rotate 3
                    frame:
                        xalign 0.5
                        ypos -114
                        xsize 311
                        ysize 403
                        background Color("#B8B8B8")
                transform:
                    rotate 3
                    frame:
                        xalign 0.5
                        ypos -113
                        xsize 309
                        ysize 401
                        background Frame(f"gui/diary/documents/dummy-files/{display}.webp")
                frame:
                    xsize 29
                    ysize 112
                    background Frame("gui/diary/documents/paperclip-back.png")

                frame:
                    xalign 0.5
                    ypos -54
                    xsize 311
                    ysize 403
                    background Color("#B8B8B8")
                frame:
                    xalign 0.5
                    ypos -53
                    xsize 309
                    ysize 401
                    background Frame(f"gui/diary/documents/dummy-files/{display}.webp")

                    button:
                        xalign 0.5
                        yalign 0.5
                        xsize 0.93
                        ysize 0.93
                        hover_background Color((108, 189, 228, 76))
                        action Function(openpdf, file_object.file_path)
                frame:
                    ypos -62
                    xpos 245
                    xsize 29
                    ysize 112
                    background Frame("gui/diary/documents/paperclip-front.png")

            text _(file_object.get_ellipsized_filename()):
                xalign 0.5
                ypos 490
                yanchor 0.5
                size 15
                color gui.color_hot_pink
                text_align 0.5
                font gui.diary_entry_font
                outlines []

            transform:
                rotate remove_button_rotation
                use diary_post_it(display, "remove", button_variant, value_name, remove_button_xpos, remove_button_ypos, index)

            if index is not None:
                transform:
                    rotate add_button_rotation
                    use diary_post_it(display, "add", button_variant, value_name, add_button_xpos, add_button_ypos, index, pdf_type=pdf_type)
            transform:
                rotate replace_button_rotation
                use diary_post_it(display, "replace", button_variant, value_name, replace_button_xpos, replace_button_ypos, index, pdf_type=pdf_type)

screen file_lightbox(thumbnails):
    zorder 10000
    modal True
    use overlay:
        viewport:
            mousewheel True
            draggable True
            xsize 635
            xalign 0.5
            ysize 1080
            has vbox:
                xfill True
                spacing 30
            frame:
                background None
                ysize 135
            for thumbnail in thumbnails:
                frame:
                    xsize 635
                    ysize 822
                    background Frame(im.Data(thumbnail, "eraser.png"))
            frame:
                background None
                ysize 135

screen add_file_lightbox(value_name, value_display_name, post_function=None, replace=False, replacement_index=None, pdf_type=PDF):
    on "show" action SetVariable("should_close_modal", False), SetVariable("file_slotted_for_upload", None)
    timer 0.1 action Function(file_uploader.upload_pdf, location_value_name=value_name, should_return=False, post_function=file_uploader.set_slotted_file)
    zorder 10000
    modal True
    use overlay:
        if file_slotted_for_upload is not None:
            use diary_file_upload_submit_modal(file_slotted_for_upload, value_name, value_display_name, replace=replace, replacement_index=replacement_index, pdf_type=pdf_type)
        if should_close_modal:
            if in_diary_review or in_diary_review_bank_info:
                timer 0.1 action Hide(), Function(file_upload_diary_review_evaluate_errors_and_add_diary_pages, value_name)
            else:
                timer 0.1 action Hide(), Function(evaluate_errors_and_add_diary_pages, value_name, False)

screen diary_file_upload_submit_modal(file_slotted_for_upload, value_name, value_display_name, post_function=None, replace=False, replacement_index=None, pdf_type=PDF):
    $ renpy.dynamic("filename_without_path")
    frame:
        style_prefix "upload_modal_button"
        background Frame("gui/frame-narrator.png")
        xsize 495
        ysize 332
        xalign 0.5
        yalign 0.5

        has vbox:
            xfill True
            ysize 275
            yalign 0.5
            spacing 38
        frame:
            background "gui/frame-upload.png"
            xsize 444
            ysize 160
            xalign 0.5

            has vbox:
                spacing 2
            $ filename_without_path = file_uploader.get_ellipsized_file_name_for_path(file_slotted_for_upload)
            text filename_without_path
            textbutton _("{u}Change File{u}"):
                hover_sound "audio/button_click.ogg"
                action SetVariable("file_slotted_for_upload", None), Function(file_uploader.upload_pdf, location_value_name=value_name, should_return=False)
        textbutton _("Submit") style "diary_pink_text_button":
            hover_sound "audio/button_click.ogg"
            xsize 432
            action Function(file_uploader.save_pdf, chosen_file=file_slotted_for_upload, location_value_name=value_name, pdf_type=pdf_type, replace=replace, replacement_index=replacement_index, notification_message=f'A Form {value_display_name} {"was successfully replaced" if replace else "has been added"}.', post_function=post_function, changed=f'{value_name}{"[" + str(replacement_index) + "]" if replacement_index is not None else ""}', evaluate_all=False)


screen diary_file_removal_confirmation(value_name, value_display_name, index, post_function=None):
    $ renpy.dynamic("_removal_text")
    on "show" action SetVariable("should_close_modal", False)
    zorder 10000
    modal True
    use overlay:
        if should_close_modal:
            if in_diary_review or in_diary_review_bank_info:
                timer 0.1 action Hide(), Function(file_upload_diary_review_evaluate_errors_and_add_diary_pages, f'{value_name}[{index}]')
            else:
                timer 0.1 action Hide(), Function(evaluate_errors_and_add_diary_pages, f'{value_name}[{index}]' if index != None else f'{value_name}', False)
        frame:
            style_prefix "upload_modal_button"
            background Frame("gui/frame.png", 40, 40)
            xsize 495
            xalign 0.5
            yalign 0.5
            bottom_padding 33
            left_padding 50
            right_padding 50
            top_padding 50

            has vbox:
                spacing 49
            vbox:
                style_prefix "diary_file_removal_confirmation"
                spacing 20
                xalign 0.5
                if index is not None:
                    $ _removal_text = f'Are you sure you want to remove Form {value_display_name} named "{"" if len(globals()[value_name]) <= index else globals()[value_name][index].get_file_name()}"?'
                else:
                    $ _removal_text = f'Are you sure you want to remove Form {value_display_name} named "{"" if globals()[value_name] is None else globals()[value_name].get_file_name()}"?'
                text _(_removal_text):
                    xalign 0.5
                text _('This change cannot be undone.'):
                    xalign 0.5
            vbox:
                spacing 10
                textbutton _(f'Remove Form {value_display_name}') style "diary_pink_text_button":
                    hover_sound "audio/button_click.ogg"
                    xsize 450
                    action Function(file_uploader.delete_pdf, index, location_value_name=value_name, notification_message=f'Form {value_display_name} was successfully removed.')
                textbutton _("{u}Nevermind, I'll keep this form{u}"):
                    hover_sound "audio/button_click.ogg"
                    action Hide("diary_file_removal_confirmation")

style diary_file_removal_confirmation_text:
    size 28
    color gui.color_dark_pink
    outlines [(2, gui.color_white)]
    text_align 0.5

style diary_pink_text_button is pink_text_button:
    ysize 90
    xalign 0.5

style diary_pink_text_button_text is pink_text_button_text:
    size 32

screen diary_error_modal():
    $ renpy.dynamic("_modal_transform")
    if should_close_diary_error_modal:
        $ _modal_transform = slide_out_left(-8)
        timer 1.0 action SetVariable("should_close_diary_error_modal", False)
    elif len(error_messages) == 0 or (len(error_messages) == 1 and error_messages.get("screener_choice", None) is not None):
        $ _modal_transform = x()
    else:
        $ _modal_transform = slide_in_left(-8)

    frame at _modal_transform:
        background None
        xsize 350
        ysize 370
        ypos 549
        xpos -8

        has vbox:
            xsize 350
            spacing 0
            xpos 0
        frame:
            background Frame("gui/diary/errors/frame-error_header.png")
            xsize 350
            ysize 45
            ypos 0
            text _("Errors to Resolve"):
                font gui.text_font
                size 20
                color gui.color_white
                xalign 0.42
                yalign 0.5
                text_align 0.5
            frame:
                background Frame("gui/diary/errors/frame-error_number.png")
                xsize 46
                ysize 46
                xpos 18
                ypos -27

                text _(str(len(error_messages))):
                    font gui.text_font
                    size 20
                    color gui.color_white
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5

        viewport:
            xsize 350
            mousewheel True
            draggable True
            xpos -15
            has frame:
                background Frame("gui/diary/errors/frame-error_bg.png")
                xfill True

            vbox:
                for value_name, message in error_messages.items():
                    if value_name != "screener_choice":
                        use diary_error_line_item(value_name, message)

screen diary_error_line_item(value_name, message):
    frame:
        background Frame("gui/diary/errors/frame-error_line_item.png")
        xpos 0
        xsize 350
        ysize 57

        has button:
            xalign 0.5
            yalign 0.5
            xsize 350
            ysize 34
            text _('{u}[message]{/u}'):
                font gui.font_arial
                color gui.color_white
                size 18
                xpos 0.12
                text_align 0.0
            hover_background Frame("gui/diary/errors/error_line_item-hover.png")
        if not in_diary_review and not in_diary_review_bank_info:
            action SetVariable("_diary_section", diary_field_section_page_mapping[value_name]["section_number"]), SetVariable("_diary_page",  diary_field_section_page_mapping[value_name]["page_number"])
        else:
            action None
screen diary_closed():
    add "gui/diary/diary_closed.png":
        xalign 0.5
        ypos 50

screen diary_address_input(value_name, display, type):
    if type == "prop":
        vbox:
            style_prefix "diary_address_input"
            use diary_input_field_labeled(display, f'{value_name}.line_1', f"{type}_string", changed_function=f"validate_and_save_active_input_required_property")
            use diary_input_field(f'{value_name}.line_2', f"{type}_string", changed_function="validate_and_save_active_input_property")
            hbox:
                use diary_input_field(f'{value_name}.city', f"{type}_string", changed_function="validate_and_save_active_input_required_property", xsize=228, max_chars=15)
                use diary_input_field(f'{value_name}.state', f"{type}_string", changed_function="validate_and_save_active_input_state_prop", xsize=62)
            use diary_input_field(f'{value_name}.zip', f"{type}_string", changed_function="validate_and_save_active_input_zip_prop")
    elif type == "arr_prop":
        vbox:
            style_prefix "diary_address_input"
            use diary_input_field_labeled(display, f'{value_name}.line_1', f"{type}_string", changed_function=f"validate_and_save_active_input_required_array_property")
            use diary_input_field(f'{value_name}.line_2', f"{type}_string", changed_function="validate_and_save_active_input_array_property")
            hbox:
                use diary_input_field(f'{value_name}.city', f"{type}_string", changed_function="validate_and_save_active_input_required_array_property", xsize=228, max_chars=15)
                use diary_input_field(f'{value_name}.state', f"{type}_string", changed_function="validate_and_save_active_input_state_array_prop", xsize=62)
            use diary_input_field(f'{value_name}.zip', f"{type}_string", changed_function="validate_and_save_active_input_zip_array_prop")

style diary_address_input_vbox:
    xfill True
    spacing 9

style diary_address_input_hbox:
    spacing 25
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
