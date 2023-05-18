style pink_text_button is button:
    background Frame("gui/button/button-frame.png", 40, 40)
    hover_background Frame("gui/button/button-frame-hover.png", 40, 40)


style pink_text_button_text is button_text:
    color "#FFFFFF"
    outlines [ (2, gui.text_color), (2, gui.text_color, 2, 2) ]
    font gui.name_text_font
    xalign 0.5
    yalign 0.5
    hover_outlines [ (2, "#03357A"), (2, "#03357A", 2, 2) ]


screen heart_frame(x_pos=None, y_pos=None, xalign=None, yalign=None, x_size=553, y_size=0, show_errors_for_ids=None, variant=None, xanchor=None, yanchor=None):
    fixed at easein_fast:
        xsize x_size
        yfit True


        if x_pos is not None:
            xpos x_pos

        if y_pos is not None:
            ypos y_pos

        if xalign is not None:
            xalign xalign

        if yalign is not None:
            yalign yalign

        if yanchor is not None:
            yanchor yanchor

        if xanchor is not None:
            xanchor xanchor

        xanchor 0.5
        yanchor 0.5

        if (error and show_errors_for_ids is not None):
            $ renpy.dynamic("message", "errors_to_show")
            $ errors_to_show = intersection(error_messages.keys(), show_errors_for_ids)
            if (len(errors_to_show) > 0):
                $ message = error_messages[errors_to_show[0]]
                frame:
                    background Frame("gui/frame-error.png")
                    xpos absolute(95)
                    ypos absolute(5)
                    xsize absolute(x_size-50)
                    ysize absolute(45)
                    label message style "heart_frame_error_label"

        frame:
            xpos absolute(5)
            ypos absolute(0)
            xsize 146
            ysize 125
            if variant == "narrator":
                background Image("gui/frame-corner-heart-narrator.png")
            else:
                background Image("gui/frame-corner-heart.png")
        frame:
            xpos absolute(50)
            ypos absolute(46)
            bottom_padding 20
            left_padding 20
            right_padding 20
            top_padding 20
            xfill True
            if variant == "narrator":
                background Frame("gui/frame-narrator.png", 65, 65)
            else:
                background Frame("gui/frame.png", 65, 65)

            frame:
                background None
                xpos 0.5
                xanchor 0.5
                transclude


style heart_frame_error_label:
    xalign 0.5
    yalign 0.5

style heart_frame_error_label_text:
    font gui.text_font
    size 20
    color gui.color_white
    text_align 0.5

screen headline(text_xsize=None, pos=None, label="", variant=None):
    vbox:
        xfill True
        if pos is not None:
            pos pos
        frame:
            if variant == "narrator":
                style_prefix "headline_narrator"
            else:
                style_prefix "headline"
            if text_xsize is not None:
                xsize text_xsize

            label _(label)
        frame:
            if variant == "narrator":
                style_prefix "headline_line_narrator"
            else:
                style_prefix "headline_line"
            xfill True




style headline_frame:
    ysize 55
    background Frame("gui/frame-headline.png")

style headline_narrator_frame is headline_frame:
    background Frame("gui/frame-headline-narrator.png")

style headline_label is gui_label:
    yalign 0.5
    xpos 29

style headline_label_text is gui_label_text:
    font gui.text_font
    size 20
    color gui.color_maroon

style headline_narrator_label is headline_label

style headline_narrator_label_text is headline_label_text:
    color gui.color_dark_purple

style headline_line_frame:
    ysize 4
    background Color(gui.color_dark_pink)

style headline_line_narrator_frame is headline_line_frame:
    background Color(gui.color_hot_purple)

screen input_box(value_name, frame_width=0, frame_height=0, placeholder_string="", changed_function=None, value_type="string", variant=None, max_chars=24):
    $ renpy.dynamic("_placeholder_showing", "placeholder_string", "_value", "final_value_name", "idx", "attr")
    if "arr_prop" in value_type:
        $ _value = get_value_array_property(value_name)
        $ _placeholder_showing = True if _value == "" or _value == None else False
    elif "prop" in value_type:
        $ _value = get_value_property(value_name)
        $ _placeholder_showing = True if _value == "" or _value == None else False
    else:
        $ _placeholder_showing = True if globals()[value_name] == "" or globals()[value_name] == None else False
        $ _value = globals()[value_name]
    frame:
        style_prefix "diary_input_field"
        if get_error_message_by_id(value_name) is not None:
            background Frame("gui/frame-text-input-error.png")
        elif variant is not None and variant == "narrator":
            background Frame("gui/frame-text-input-narrator.png")
        else:
            background Frame("gui/frame-text-input.png")
        xfill True
        xalign 0.5
        yalign 0.5
        ysize frame_height
        padding (8, 8, 0, 8)
        if active_input_field_id != value_name:
            button:
                action SetVariable("active_input_field_id", value_name)
                has hbox:
                    spacing 0
                if _placeholder_showing:
                    if "float" in value_type:
                        text "$":
                            yfill True
                            ypos 0.5
                            yanchor 0.5
                            if get_error_message_by_id(value_name) is not None:
                                style_prefix "input_text_error"
                            else:
                                style_prefix "input_text"
                    label placeholder_string:
                        style_prefix "placeholder"
                        xfill True
                        yfill True
                        yanchor 0.5
                        ypos 0.6
                        if get_error_message_by_id(value_name) is not None:
                            text_color gui.color_red
                        elif variant is not None and variant == "narrator":
                            text_color gui.color_dark_purple_placeholder
                else:

                    if "float" in value_type:
                        $ _value = "${0:.2f}".format(_value)
                    else:
                        $ _value = str(_value)
                    label get_ellipsized_value(_value, max_chars):
                        if variant is not None and variant == "narrator":
                            text_color gui.color_dark_purple
                        style_prefix "non_placeholder"
                        xsize frame_width
                        yfill True
                        yanchor 0.5
                        ypos 0.66
                        xpos 0
                        text_outlines []

        else:
            hbox:
                ypos 0.5
                yanchor 0.5
                spacing 0
                if "float" in value_type:
                    text "$":
                        yfill True
                        ypos 0.5
                        yanchor 0.5
                        if get_error_message_by_id(value_name) is not None:
                            style_prefix "input_text_error"
                        else:
                            style_prefix "input_text"
                input:
                    copypaste True
                    if get_error_message_by_id(value_name) is not None:
                        style_prefix "input_text_error"
                    elif variant != None and variant == "narrator":
                        style_prefix "input_text_narrator"
                    else:
                        style_prefix "input_text"

                    pixel_width (frame_width - 10)
                    if changed_function is None:
                        value VariableInputValue(value_name, default=True)
                    xfill True
                    yfill True
                    ypos 0.55
                    yanchor 0.5
                    if placeholder_string == "City":
                        length 15
                    else:
                        length max_chars
                    if _value is not None:
                        default str(_value)
                    changed changed_function

style placeholder_label is gui_label
style placeholder_label_text is gui_label_text:
    font gui.text_font
    size 26
    color Color(gui.color_maroon).replace_opacity(0.3)
    outlines [(2, gui.color_white)]
    text_align 0.0

style non_placeholder_label is gui_label
style non_placeholder_label_text:
    font gui.text_font
    size 26
    color gui.color_maroon
    text_align 0.0
    outlines []

style input_text_input:
    xfill True
    yfill True
    yalign 0.5
    font gui.text_font
    size 26
    color gui.color_maroon
    text_align 0.0

style input_text_narrator_input is input_text_input:
    color gui.color_dark_purple

style input_text_text:
    xfill True
    yfill True
    yalign 0.5
    font gui.text_font
    size 26
    color gui.color_maroon
    text_align 0.0

style input_text_narrator_text is input_text_text:
    color gui.color_dark_purple

style input_text_error_input is input_text_input:
    color gui.color_red

style input_text_error_text is input_text_text:
    color gui.color_red

screen choice_checkbox(option, value_name, selected=False, variant=None, allow_multiple=False, value_type="bool"):
    button:
        if allow_multiple:
            action SetVariableMultipleOption(value_name, option["value"])
        elif "arr_prop" in value_type:
            action SetVariableArrayPropOption(value_name, option["value"])
        else:
            action SetVariableOption(value_name, option["value"])
        if variant == "narrator":
            style_prefix "checkbox_choice_narrator"
        else:
            style_prefix "checkbox_choice"
        xfill True
        hbox:
            ypos 0.5
            yalign 0.5
            spacing 14
            xpos 31
            frame:
                if variant == "narrator":
                    if selected:
                        background Image("gui/button/checkbox-checked-narrator.png")
                    else:
                        background Image("gui/button/checkbox-unchecked-narrator.png")
                else:
                    if selected:
                        background Image("gui/button/checkbox-checked.png")
                    else:
                        background Image("gui/button/checkbox-unchecked.png")

                xsize 49
                ysize 42
                yalign 0.5
            text option["display"]:
                yalign 0.5
                xsize 0.9

style checkbox_choice_button is gui_button:
    hover_background Color((220, 7, 107, 76.5))

style checkbox_choice_narrator_button is gui_button:
    hover_background Color((156, 7, 220, 127.5))

style checkbox_choice_text is gui_label_text:
    font gui.text_font
    size 26
    color gui.color_maroon
    outlines [(2, gui.color_white)]

style checkbox_choice_narrator_text is checkbox_choice_text:
    color gui.color_dark_purple

screen choice_heart_frame(value_name, options, xpos, ypos, headline_x_size, variant=None, allow_multiple=False, value_type="bool"):
    $ renpy.dynamic("options_length", "headline_text")
    $ options_length = len(options)
    if allow_multiple:
        $ headline_text = "Choose all that apply"
    else:
        $ headline_text = "Choose 1"
    use heart_frame(x_pos=xpos, y_pos=ypos, variant=variant, show_errors_for_ids=[value_name]):
        frame:
            background None
            xfill True
            has vbox:
                xfill True
                spacing 8.5
            use headline(text_xsize=headline_x_size, label=headline_text, variant=variant)
            for idx, option in enumerate(options):
                $ renpy.dynamic("is_selected")
                if allow_multiple:
                    $ is_selected = True if option["value"] in globals()[value_name] else False
                else:
                    if "arr_prop" in value_type:

                        $ is_selected = True if get_value_array_property(value_name) == option["value"] else False
                    else:
                        $ is_selected = True if globals()[value_name] == option["value"] else False
                use choice_checkbox(option, value_name, is_selected, variant=variant, allow_multiple=allow_multiple, value_type=value_type)


                if (idx is not options_length - 1):
                    frame:
                        if variant == "narrator":
                            background Color(gui.color_hot_purple)
                        else:
                            background Color(gui.color_dark_pink)
                        xfill True
                        ysize 2

screen file_upload_modal(value_name, upload_number, file_label, is_multiple=False, frame_xsize=500, headline_xsize=223, pdf_type=PDF):
    $ renpy.dynamic("filename_without_path", "progress_bar_x_size")
    use heart_frame(x_pos=0.77, y_pos=430, x_size=frame_xsize, show_errors_for_ids=[value_name]):
        vbox:
            xfill True
            spacing 27
            use headline(text_xsize=headline_xsize, pos=(0, 0), label=f'Upload your {file_label}')
            frame:
                padding (0, 0, 0, 0)
                background None
                xsize 444
                ysize 160
                xalign 0.5
                style_prefix "upload_modal_button"
                if (is_multiple and len(globals()[value_name]) == upload_number) or (not is_multiple and globals()[value_name] is not None) and not busy_uploading:

                    vbox:
                        spacing 2
                        if is_multiple:
                            $ filename_without_path = globals()[value_name][upload_number - 1].get_ellipsized_filename()
                        else:
                            $ filename_without_path = globals()[value_name].get_ellipsized_filename()
                        text filename_without_path
                        textbutton _("{u}Change File{u}"):
                            action Function(file_uploader.upload_and_save_pdf, location_value_name=value_name, replace=True, replacement_index=upload_number - 1, pdf_type=pdf_type)
                elif busy_uploading:
                    vbox:
                        spacing 16

















                        text "Uploading..." style "upload_modal_button_button_text"
                elif not busy_uploading:

                    button style "upload_modal_button":
                        hover_background Frame("gui/button/frame-upload-hover.webp")
                        action Function(file_uploader.upload_and_save_pdf, location_value_name=value_name, pdf_type=pdf_type)
                        has vbox
                        add "gui/button/button-upload.png" at upload_modal_button_image
                        text f'Upload your {file_label}'



style upload_modal_button:
    xfill True
    yfill True
    padding (0, 0, 0, 0)

style upload_modal_button_vbox:
    spacing 16
    xalign 0.5
    yalign 0.5

transform upload_modal_button_image:
    xsize 48
    ysize 48
    xalign 0.5
    yalign 0.5

style upload_modal_button_text:
    font gui.text_font
    color gui.color_maroon
    size 26
    text_align 0.5
    xalign 0.5
    yalign 0.5

style upload_modal_button_button:
    xalign 0.5

style upload_modal_button_button_text:
    font gui.text_font
    color gui.color_maroon
    size 16
    xalign 0.5
    text_align 0.5

screen signature_box(ysize=123, xsize=444):
    button:
        mouse "emotional_support_hand"
        action NullAction()
        xfill True
        ysize ysize
        has vbox:
            spacing 0
            xfill True
            ysize ysize

        hbox:
            yfill True
            spacing 5

            add "gui/signature-x.png":
                xsize 28
                ysize 30
                yanchor 0.5
                ypos 0.78
                xpos 10
            $ create_freehand_canvas(xsize, ysize)
            add freehand_canvas

        frame:
            background Color(gui.color_maroon)
            ysize 2
            xfill True

screen overlay(sparkles=False, with_close=True):
    frame:
        background "gui/background-blur.png"
        xsize 1920
        ysize 1080
        if sparkles:
            frame:
                background "sparkles_first_half_opacity"
                xfill True
                yfill True
            frame:
                background "sparkles_second_half_opacity"
                xfill True
                yfill True
        if with_close:
            button:
                background Frame("gui/diary/buttons/exit.png")
                hover_background Frame("gui/diary/buttons/exit-hover.png")
                action Hide()
                xsize 79
                ysize 79
                xpos 1793
                ypos 50
        transclude
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
