










init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    on "show" action SetVariable("current_char", who)
    on "show" action SetVariable("quick_menu", True)
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()

    style_prefix "say"

    window:
        id "window"

        if who is not None:

            frame:
                id "namebox"
                style "namebox"
                text who id "who"

            button:
                style "ctc_iris"
                xsize 222
                ysize 60
                xpos 0.7678
                ypos 0.75
                hover_sound "audio/button_click.ogg"
                if not ctc_disabled:
                    action renpy.curry(renpy.restart_interaction)
                    background Frame("gui/ctc-iris.png")
                    hover_background Frame("gui/ctc-iris_hover.png")
                else:
                    background Frame("gui/ctc-iris-disabled.png")

            if rollback_enabled:
                button:
                    xsize 222
                    ysize 60
                    xpos 0.115
                    ypos 0.745
                    action Rollback()
                    background Frame("gui/rollback-iris.png")
                    hover_background Frame("gui/rollback-iris_hover.png")
                    hover_sound "audio/button_click.ogg"

        else:
            button:
                style "ctc"
                hover_sound "audio/button_click.ogg"
                xsize 222
                ysize 60
                xpos 0.7678
                ypos 0.75
                if not ctc_disabled:
                    action renpy.curry(renpy.restart_interaction)
                    hover_background Frame("gui/ctc_hover.png")
                else:
                    background Frame("gui/ctc-disabled.png")


        text what id "what" style "say_thought"
        use quick_menu




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default

init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label

init -1 style ctc is default
init -1 style ctc_iris is default

init -1 style say_dialogue:
    line_spacing 43

init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background None

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xminimum 314
    left_padding 15
    right_padding 15
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/frame-headline.png", xalign=gui.name_xalign)


init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

init -1 style ctc:
    background Frame("gui/ctc.png")











init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    modal True
    zorder 5000
    style_prefix "choice"
    use overlay(with_close=False):



        frame:
            background Frame("gui/frame-choice.png", 60, 60)
            padding (50, 50, 50, 50)
            xalign 0.5
            yalign 0.5
            has vbox at choice_transform
            for i in items:
                textbutton i.caption action i.action:
                    hover_sound "audio/button_click.ogg"

transform -1 choice_bg_transform_show:
    blur 20.0

transform -1 choice_bg_transform_hide:
    blur 0.0

transform -1 choice_transform:
    alpha 0.0
    easein 0.5 alpha 1.0

    on hide:
        easein 0.5 alpha 0.0

init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    spacing gui.choice_spacing

init -1 style choice_button is default:
    yalign 0.5
    ysize gui.choice_button_height
    properties gui.button_properties("choice_button")
    background Frame("gui/button/choice_idle_background_shadow.png", 36, 36)
    hover_background Frame("gui/button/choice_hover_background_shadow.png", 36, 36)

init -1 style choice_button_text is default:
    yalign 0.3
    properties gui.button_text_properties("choice_button")




init -501 screen tax_deadline():
    zorder 1000
    if show_overlay:
        if has_dated:
            frame at easein:
                background Frame("gui/overlay/deadline.png")
                ypos absolute(32)
                xpos 1460
                xsize 428
                ysize 115



init -501 screen progress_tracker():
    zorder 1000
    if show_overlay:
        if has_dated == True:
            frame at easein:
                ypos absolute(28)
                xpos absolute(45)
                xsize 350
                ysize 197
                xpadding 0
                ypadding 0
                background None

                frame:
                    background Frame("gui/overlay/progress/progress-blank_new.png")
                    xpos absolute(115)
                    ypos absolute(12)
                    right_padding 100
                    ysize 106

                    has vbox:
                        xpos 70
                        ypos -9
                        spacing 6
                    hbox:
                        xfill True
                        ysize 50

                        hbox:
                            yalign 0.5
                            spacing 9
                            add "gui/overlay/progress/progress_heart.png" xsize 18 ysize 15 yalign 0.7
                            text f"DATES" style "date_progress_label_text"

                        frame:
                            ysize 50
                            background None
                            left_margin 20
                            xalign 1.0
                            text f"{dates_completed} / 4" style "date_progress_text"


                    hbox:
                        xfill True

                        ysize 50
                        text f"{'TAX OWED' if form_1040_line_37 > 0 else 'REFUND'}" style "date_progress_label_text" yalign 0.55
                        frame:
                            ysize 50
                            background None
                            left_margin 20
                            xalign 1.0
                            text f"${(int(refund) if form_1040_line_37 == 0 else int(form_1040_line_37)):,}" style "date_progress_text"
                frame:
                    xpos absolute(0)
                    ypos absolute(0)
                    xsize 181
                    ysize 192
                    background Frame(f"gui/overlay/progress/affection_level-{dates_completed}.png")


init -1 style date_progress_text is text:
    font gui.name_text_font
    color "#FFFFFF"
    size 24
    outlines [ (2, gui.text_color), (2, gui.text_color, 2.35, 2.35) ]
    xalign 1.0
    yalign 0.5
    text_align 1.0

init -1 style date_progress_label_text is text:
    font gui.sub_label_font
    size 18
    color "#FFFFFF"
    outlines []
    xalign 0.0
    yalign 0.5
    text_align 0.0








init -501 screen quick_menu():


    zorder 1000

    if quick_menu:

        hbox:
            style_prefix "quick"

            xanchor 0.0
            xpos 0.7235
            ypos 80
            yanchor 0.5
            if current_char is not None:
                textbutton _("SAVE"):
                    style "save_button_iris"
                    if not past_return_downloading:
                        action CustomAutoSave()
                        hover_sound "audio/button_click.ogg"
                    else:
                        text_color Color("#8A0141", alpha=0.3)

                textbutton _("SETTINGS") action ShowMenu("preferences") style "settings_button_iris" hover_sound "audio/button_click.ogg"




            else:
                textbutton _("SAVE"):
                    style "save_button"
                    if not past_return_downloading:
                        action CustomAutoSave()
                        hover_sound "audio/button_click.ogg"
                    else:
                        text_color Color("#6A018A", alpha=0.3)
                textbutton _("SETTINGS") action ShowMenu("preferences") style "settings_button_dialogue" hover_sound "audio/button_click.ogg"



init -1 python:

    config.overlay_screens.append("tax_deadline")
    config.overlay_screens.append("progress_tracker")
    renpy.add_layer("transitions", above="overlay")

init -1 style quick_button is default
init -1 style quick_button_text is button_text


init -1 style save_button is quick_button:
    xsize 147
    ysize 50

init -1 style save_button_text is quick_button_text


init -1 style save_button_iris is quick_button_iris:
    xsize 147
    ysize 50

init -1 style save_button_iris_text is quick_button_iris_text


init -1 style settings_button_dialogue is quick_button:
    xsize 161
    ysize 50

init -1 style settings_button_dialogue_text is quick_button_text


init -1 style settings_button_iris is quick_button_iris:
    xsize 161
    ysize 50

init -1 style settings_button_iris_text is quick_button_iris_text


init -1 style autoplay_button is quick_button:
    xsize 220
    ysize 50

init -1 style autoplay_button_text is quick_button_text

init -1 style autoplay_button_on is quick_button:
    xsize 220
    ysize 50
    left_margin 28
    right_margin 28
    top_margin 13
    bottom_margin 15
    background Solid("#6B1687")

init -1 style autoplay_button_on_text is quick_button_text:
    idle_color "#DEBEF9"
    hover_color "#DEBEF9"


init -1 style autoplay_button_iris is quick_button_iris:
    xsize 220
    ysize 50

init -1 style autoplay_button_iris_text is quick_button_iris_text

init -1 style autoplay_button_on_iris is autoplay_button_on:
    background Solid("#7A033B")

init -1 style autoplay_button_on_iris_text is quick_button_text:
    idle_color "#FFC6EC"
    hover_color "#FFC6EC"


init -1 style quick_button:
    properties gui.button_properties("quick_button")
    left_margin 6
    right_margin 6
    hover_background Solid("#AF5DD2")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")

init -1 style quick_button_iris is quick_button:
    hover_background Solid("#EE7BBD")

init -1 style quick_button_iris_text is quick_button_text:
    idle_color "#8A0141"
    hover_color "#8A0141"












init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu and not has_saved:
            textbutton _("Start") action Start() style "pink_text_button"

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):



            textbutton _("Quit") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








init -501 screen main_menu():
    tag menu



    add gui.main_menu_background xsize 1920 ysize 1080
    frame:
        background "sparkles_first"
    frame:
        background "sparkles_second"
    add "gui/main_menu/mschftax-logo.webp" xpos 40 ypos 40 xsize 342 ysize 75 at easein_pause(0.75)
    add "gui/main_menu/other-forms.webp" xsize 1570 ysize 1671 xpos 679 ypos -127 at easein_pause(1.0)
    add "gui/main_menu/form-6.webp" xsize 156 ysize 167 xpos 385 ypos 25 at easein_pause(0.7, 0.5)
    add "gui/main_menu/form-5.webp" xsize 182 ysize 212 xpos 238 ypos 105 at easein_pause(0.6, 0.5)
    add "gui/main_menu/form-4.webp" xsize 249 ysize 279 xpos 101 ypos 232 at easein_pause(0.5, 0.5)
    add "gui/main_menu/form-3.webp" xsize 332 ysize 387 xpos 91 ypos 458 at easein_pause(0.4, 0.5)
    add "gui/main_menu/form-2.webp" xsize 474 ysize 524 xpos 235 ypos 662 at easein_pause(0.3, 0.5)
    add "gui/main_menu/form-1.webp" xsize 365 ysize 445 xpos 687 ypos 930 at easein_pause(0.2, 0.5)

    add "gui/main_menu/iris.webp" ysize 1080 xsize 1382 ypos 0 at slide_in_right(pause_time=1.0), easein_pause
    add "gui/main_menu/logo.webp" xalign 0.5 ypos 75 xsize 1227 ysize 763 at easein_pause(0.75), bob(75)







    vbox at easein_pause(0.75):
        style_prefix "main_menu_secondary"
        xpos absolute(1620)
        ypos absolute(38)
        spacing 0
        textbutton _("TERMS & CONDITIONS") action OpenURL("https://taxheaven3000.com/terms-of-service.pdf")
        textbutton _("SUPPORT") action OpenURL("mailto:support@mschf.com")



    frame at appear_up:
        background Frame("gui/main_menu/game_menu_bar.webp")
        ysize 185
        xfill True
        ypos 1.0
        yanchor 1.0
        has hbox:
            $ renpy.dynamic("has_saved", "newest_slot")
            style "main_menu_hbox"
        $ newest_slot = renpy.newest_slot()
        $ has_saved = True if newest_slot is not None else False

        if has_saved:
            $ x_size = (1920 - 70 * 5)/4
        else:
            $ x_size =  (1920 - 70 * 4)/3

        textbutton _("New Game") action If(has_saved, true=Show("confirm", None, START_NEW_GAME_MESSAGE, Hide(), [Function(renpy.invoke_in_thread, delete_pdfs_in_save_dir), Start()], no_message="Start New Game", yes_message="Nevermind, keep my current save"), false=Start()):
            hover_sound "audio/button_click.ogg"
            style "main_menu_text_button"
            xsize absolute(x_size)

        if has_saved:
            textbutton _("Continue") action FileLoad(newest_slot, confirm=False, slot=True) style "main_menu_text_button" xsize absolute(x_size):
                hover_sound "audio/button_click.ogg"

        textbutton _("Settings") action ShowMenu("preferences") style "main_menu_text_button" xsize absolute(x_size):
            hover_sound "audio/button_click.ogg"
        textbutton _("Quit") action Quit() style "main_menu_text_button" xsize absolute(x_size):
            hover_sound "audio/button_click.ogg"


init -1 style main_menu_frame is empty
init -1 style main_menu_hbox is hbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_hbox:
    xalign 0.5
    yalign 0.5
    spacing 70

init -1 style main_menu_text_button is pink_text_button:
    ysize 114

init -1 style main_menu_text_button_text is pink_text_button_text:
    size 32

init -1 style main_menu_secondary_button is gui_button:
    yalign 0.5
    xalign 1.0

init -1 style main_menu_secondary_button_text is gui_button_text:
    font gui.sub_label_font
    size 20
    color gui.color_white
    text_align 1.0


init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")











init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 60
    top_padding 240

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 560
    yfill True

init -1 style game_menu_content_frame:
    left_margin 80
    right_margin 40
    top_margin 20

init -1 style game_menu_viewport:
    xsize 1840

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 20

init -1 style game_menu_label:
    xpos 100
    ysize 240

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -60









init -501 screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():
    tag menu


    use file_slots(_("Save"))


init -501 screen load():
    tag menu


    use file_slots(_("Load"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 100
    ypadding 6

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")






init -501 screen name_entry():
    frame:
        background Color((33, 45, 50, 200))
        xfill True
        yfill True
    frame:
        background "sparkles_first"
        xfill True
        yfill True
    frame:
        background "sparkles_second"
        xfill True
        yfill True

    use heart_frame(x_size=520, y_size=705, xalign=0.45, yalign=0.45, show_errors_for_ids=['first_name', 'last_name']):
        vbox:
            xfill True
            spacing 27
            use headline(text_xsize=378, pos=(0, 0), label="Your first name")
            use input_box(value_name="first_name", frame_width=absolute(444), frame_height=absolute(55), placeholder_string="First Name")
            use headline(text_xsize=378, pos=(0, 0), label="Your middle name")
            use input_box(value_name="middle_name", frame_width=absolute(444), frame_height=absolute(55), placeholder_string="Middle Name")
            use headline(text_xsize=378, pos=(0, 0), label="Your last name")
            use input_box(value_name="last_name", frame_width=absolute(444), frame_height=absolute(55), placeholder_string="Last Name")
            textbutton _("Ok") style "name_entry_button" action SubmitNameEntry()

init -1 style name_entry_button is pink_text_button:
    xsize 460
    ysize 100
    xanchor 0.5
    xpos 0.485
    ypos absolute(13)

init -1 style name_entry_button_text is pink_text_button_text:
    size 32








init -501 screen preferences():
    modal True
    use overlay(sparkles=True, with_close=False):

        use heart_frame(x_size=500, xalign=0.47, yalign=0.50):
            fixed:
                yfit True
                vbox:
                    spacing 27
                    xalign 0.5
                    vbox:
                        xalign 0.5
                        xfill True
                        style_prefix "slider"
                        label _("Text Speed")

                        bar value Preference("text speed")

                        frame:
                            style_prefix "slider_under"
                            background None
                            ysize 40
                            label _("SLOW") xalign 0
                            label _("FAST") xalign 1.0

                        if config.has_music:
                            label _("Music Volume") xsize 1.0
                            bar value Preference("music volume")
                            frame:
                                background None
                                ysize 40
                                xfill True
                                xalign 1.0
                                style_prefix "slider_under"
                                label _("QUIET") xalign 0
                                label _("LOUD") xalign 1.0 bottom_margin 30

                        if config.has_sound:

                            label _("SFX Volume") ypos 0
                            bar value Preference("sound volume")
                            frame:
                                background None
                                ysize 40
                                style_prefix "slider_under"
                                label _("QUIET") xalign 0
                                label _("LOUD") xalign 1.0
                    style_prefix "settings"
                    textbutton _("Ok") action Return(), Hide():
                        hover_sound "audio/button_click.ogg"
                        xfill True
                        text_size 32

init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 4

init -1 style pref_label_text:
    font gui.name_text_font
    outlines gui.name_text_outlines
    color gui.name_text_color
    size 32
    yalign 1.0

init -1 style slider_under_label is gui_label

init -1 style slider_under_label_text:
    font gui.sub_label_font
    color gui.color_maroon
    size 18

init -1 style pref_vbox:
    xsize 450

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5


init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style settings_button is pink_text_button:
    xalign 0.5

    ysize absolute(100)

init -1 style settings_button_text is pink_text_button_text










init -501 screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define -1 gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 30

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 16

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 500
    right_padding 40

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action, yes_message="Yes, I'm sure", no_message="No, keep playing"):

    modal True

    zorder 10000

    style_prefix "confirm"

    use overlay(sparkles=True, with_close=False):
        use heart_frame(xalign=0.5, yalign=0.5, x_size=550):
            vbox:
                spacing 32
                xfill True
                xalign 0.5
                text message
                vbox:
                    xfill True
                    spacing 10
                    xalign 0.5
                    textbutton _(no_message) style "pink_text_button":
                        hover_sound "audio/button_click.ogg"
                        xfill True
                        ysize 100
                        xalign 0.5
                        action no_action
                        text_size 32
                    textbutton _('{u}' + f'{yes_message}' + '{u}'):
                        hover_sound "audio/button_click.ogg"
                        if type(yes_action) == renpy.revertable.RevertableList:
                            if any(isinstance(item, store.Quit) for item in yes_action) and not past_return_downloading:
                                action [Function(purge_saves)] + yes_action
                            else:
                                action yes_action
                        elif type(yes_action) == store.Quit and not past_return_downloading:
                            action Function(purge_saves), yes_action
                        else:
                            action yes_action

init -1 style confirm_label:
    xalign 0.5

init -1 style confirm__label_text:
    font gui.name_text_font
    size 60
    color gui.color_white
    outlines [(3, gui.color_maroon), (3, gui.color_maroon, 4, 4)]
    text_align 0.5
    xalign 0.5

init -1 style confirm_text:
    xsize 505
    font gui.text_font
    size 28
    color gui.color_maroon
    outlines [(2, gui.color_white)]
    text_align 0.5
    xalign 0.5

init -1 style confirm_button:
    xalign 0.5

init -1 style confirm_button_text:
    font gui.text_font
    size 20
    color gui.color_hot_pink
    xalign 0.5
    text_align 0.5








init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 12

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):
    zorder 10000
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

        if message == DEFAULT_FILE_ERROR_MESSAGE or message == FILE_IS_ENCRYPTED_ERROR_MESSAGE:
            style "notify_frame_error"

    timer 3.25 action Hide('notify'), SetVariable("confirmation_message", None)


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    yalign 0.5
    xalign 0.5
    xsize 1840
    ysize 83

    background Frame("gui/notify.png")

init -1 style notify_frame_error is notify_frame:
    background Frame("gui/notify-error.png")

init -1 style notify_text:
    properties gui.text_properties("notify")
    xalign 0.5
    yalign 0.45









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 900



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


init -1 style window:
    variant "small"
    background None

init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 680

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 800

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_vbox:
    variant "small"
    xsize None

init -1 style slider_slider:
    variant "small"
    xsize 1200


init -501 screen screener_choice(choices=STANDARD_CHOICES, variant=None):
    use choice_heart_frame("screener_choice", choices, xpos=0.77, ypos=430, headline_x_size=276, variant=variant)

init -501 screen screener_multi_choice(choices=STANDARD_CHOICES, xpos=0.77, ypos=430):
    use choice_heart_frame("screener_choices", choices, xpos=xpos, ypos=ypos, headline_x_size=276, allow_multiple=True)

init -501 screen one_line_input(label_text, value_name, placeholder_text, changed_function=None, value_type="string"):
    use heart_frame(x_pos=0.77, y_pos=430, show_errors_for_ids=[value_name]):
        vbox:
            xfill True
            spacing 27
            use headline(text_xsize=350, pos=(0, 0), label=label_text)
            use input_box(value_name=value_name, frame_width=absolute(444), frame_height=absolute(55), placeholder_string=placeholder_text, changed_function=changed_function, value_type=value_type)

init -501 screen multi_line_input(values, headline="Address", x_pos=0.77, y_pos=430, xalign=None, yalign=None, variant=None):
    use heart_frame(x_pos=x_pos, y_pos=y_pos, xalign=xalign, yalign=yalign, show_errors_for_ids=[value["value_name"] for value in values], variant=variant):
        vbox:
            xfill True
            spacing 27
            use headline(text_xsize=350, pos=(0, 0), label=headline, variant=variant)

            for value in values:
                use input_box(value_name=value["value_name"], frame_width=absolute(444), frame_height=absolute(55), placeholder_string=value["placeholder_text"], changed_function=CHANGED_FUNCTIONS[value["changed_function"]], value_type=value["type"], variant=variant)


init -501 screen choice_input(value_name, choices=STANDARD_CHOICES, variant=None, value_type="bool"):
    use choice_heart_frame(value_name, choices, xpos=0.77, ypos=430, headline_x_size=276, variant=variant, value_type=value_type)

init -501 screen w2_upload_modal(upload_number):
    use file_upload_modal('w2_objects', upload_number, 'W-2', is_multiple=True, pdf_type=W2)

init -501 screen unemployment_1099g_upload_modal():
    use file_upload_modal('unemployment_1099g_file_location', 0, '1099-G', headline_xsize=260)

init -501 screen signature_modal():
    use heart_frame(x_pos=0.77, y_pos=430, show_errors_for_ids=['signature_img_location']):
        vbox:
            xfill True
            spacing 10
            use headline(text_xsize=171, pos=(0, 0), label='Sign Below')
            use signature_box()

init -501 screen download_return_modal():
    use heart_frame(x_pos=0.77, y_pos=430, show_errors_for_ids=['return_file_location']):
        vbox:
            xfill True
            spacing 10
            style_prefix "download_return"

            use headline(text_xsize=282, pos=(0, 0), label='Download your returns')
            vbox:
                xfill True
                xalign 0.5
                spacing -10
                add "gui/return-preview.png":
                    xsize 334
                    ysize 258
                    xalign 0.5
                textbutton _("Download") action Function(download_file, return_file_location, 'return_file_location')

init -1 style download_return_button is pink_text_button:
    xsize 435
    ysize 95
    xalign 0.5

init -1 style download_return_button_text is pink_text_button_text:
    size 32

init -501 screen game_over_modal(jump_back_to=None, message="We're sorry, you can't keep playing!"):
    modal True
    zorder 10000
    use overlay(sparkles=True, with_close=False):
        transform:
            rotate -21
            frame:
                background Frame("gui/overlay/game-over-frame-heart.png")
                xsize 148
                ysize 130
                xpos 535
                ypos 240
        transform:
            rotate 21
            frame:
                background Frame("gui/overlay/game-over-frame-heart.png")
                xsize 148
                ysize 130
                xpos 1180
                ypos 640
        frame:
            background Frame("gui/frame.png", 65, 65)
            padding (20, 20, 20, 20)
            xalign 0.5
            yalign 0.5
            xsize 615
            style_prefix "game_over"
            has vbox:
                spacing 32
                xfill True
                xalign 0.5
            label "Game Over"
            text message
            vbox:
                xfill True
                spacing 10
                xalign 0.5
                if jump_back_to:
                    button style "pink_text_button":
                        text _("Replay previous question") style "pink_text_button_text":
                            yalign 0.4
                            size 32
                        xfill True
                        ysize 100
                        xalign 0.5
                        action Hide(), Jump(jump_back_to)
                elif in_diary:
                    textbutton _("Revise answer") style "pink_text_button":
                        xfill True
                        ysize 100
                        xalign 0.5
                        action Hide()
                        text_size 32
                textbutton _("{u}Go to main menu{u}") action MainMenu(confirm=False, save=False)

init -1 style game_over_label:
    xalign 0.5

init -1 style game_over_label_text:
    font gui.name_text_font
    size 60
    color gui.color_white
    outlines [(3, gui.color_maroon), (3, gui.color_maroon, 4, 4)]
    text_align 0.5
    xalign 0.5

init -1 style game_over_text:
    xsize 505
    font gui.text_font
    size 28
    color gui.color_maroon
    outlines [(2, gui.color_white)]
    text_align 0.5
    xalign 0.5

init -1 style game_over_button:
    xalign 0.5

init -1 style game_over_button_text:
    font gui.text_font
    size 20
    color gui.color_hot_pink
    xalign 0.5
    text_align 0.5

init -501 screen text_message(message, frame):
    vbox:
        xfill True
        spacing 0
        frame:
            background frame
            xsize 586
            top_padding 20
            bottom_padding 20
            left_padding 35
            right_padding 20

            text message:
                font "fonts/SF-Pro-Text-Regular.otf"
                size 37
                xalign 0.0
                yalign 0.5
                color gui.color_black
                xfill True


init -501 screen multiple_texts(messages=["Heyy [first_name]! Sorry, I got stuck doing some work in the library archive room today!", "I'll make it up to you, okay? {image=gui/emojis/kissy-emoji.png}"], frames=[Frame("gui/frame-text-message-large.png"), Frame("gui/frame-text-message-small.png")], shadow_bg=Frame("gui/frame-text-shadow.png", ypos=-35), yalign=0.4, yminimum=413, with_number=True, spacing=20):
    frame at hop(x=0.5, y=yalign):
        background shadow_bg
        yminimum yminimum
        xsize 667
        padding (0, 0, 0, 0)
        has vbox:
            xalign 0.5
            ypos 0
            spacing spacing
            xsize 600
        if with_number:
            frame:
                background Frame("gui/frame-phone-number.png")
                xalign 0.04
                xsize 215
                ysize 33
                padding (0, 0, 0, 0)
                text "314-778-2937":
                    color gui.color_white
                    size 28
                    font "fonts/SF-Pro-Text-Semibold.otf"
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5
        vbox:
            spacing 23
            xfill True
            for idx, message in enumerate(messages):
                use text_message(message, frames[idx])

init -501 screen text_scene_2_1():
    use multiple_texts(messages=["[first_name], I'm sorry I missed you yesterday! {image=gui/emojis/nervous-emoji.png}"], frames=[Frame("gui/frame-text-message-medium.png")], shadow_bg=Frame("gui/shadow_1.png", ypos=-33, xpos=-5), yalign=0.23, yminimum=264)

init -501 screen text_scene_2_2():
    use multiple_texts(messages=["Do you want to meet me at the cafe? I've been looking forward to seeing you again."], frames=[Frame("gui/frame-text-large-2.png")], shadow_bg=Frame("gui/shadow_2.png", ypos=-33, xpos=-5), yalign=0.415, yminimum=258, with_number=False)

init -501 screen text_scene_2_3():
    use multiple_texts(messages=["Or, I've got to run an errand at the library branch office. You could keep me company {image=gui/emojis/smile-emoji.png}"], frames=[Frame("gui/frame-text-large-2.png")], shadow_bg=Frame("gui/shadow_3.png", ypos=-33, xpos=-5), yalign=0.596, yminimum=258, with_number=False)

init 499 image library_to_sunset:
    "bg library"
    "bg library sunset" with Dissolve(0.5, alpha=True)

init 499 image room_to_copier:
    "bg bedroom sunset"
    "bg copier" with Dissolve(0.5, alpha=True)

init 499 image copier_to_room:
    "bg copier"
    "bg bedroom sunset" with Dissolve(0.5, alpha=True)

init 499 image room_to_sunset:
    "bg bedroom"
    "bg bedroom sunset" with Dissolve(0.5, alpha=True)

init -501 screen disclaimer:
    frame:
        background Frame("gui/main_menu/title_screen.webp")
        xfill True
        yfill True
    use overlay(with_close=False, sparkles=True):
        use heart_frame(xanchor=0.5, yanchor=0.5, x_pos=885, y_pos=0.5, x_size=1000):
            text "{i}Tax Heaven 3000{/i} is designed to prepare 2022 US federal income tax returns for single filers without dependents.\n\n{i}Tax Heaven 3000{/i} does not support all tax situations, and may not check for all possible deductions and credits that could apply to your individual tax situation. {i}Tax Heaven 3000{/i} is intended for filers with simple W-2 income, does not support amended or late tax returns, and does not support state returns.\n\n{i}Tax Heaven 3000{/i} is designed to assist in tax preparation only: it is the responsibility of the user to provide accurate information and to ultimately file their return once complete.":
                style "confirm_text"
                xsize 960

init 499 image trailer_movie = Movie(play="videos/trailer.webm")

init -501 screen trailer:
    add "trailer_movie" xsize 1920 ysize 1080

    textbutton _("Skip") style "pink_text_button":
        text_size 32
        text_align 0.5
        xsize 259
        ysize 104
        xpos 1627
        ypos 947
        action Dissolve(1.0), MainMenu(confirm=False)

init 499 image perfect_ending_credits = Movie(play="videos/CREDITS-PerfectEnding.webm")
init 499 image non_perfect_ending_credits = Movie(play="videos/CREDITS-nonPerfectEnding.webm")

init -501 screen credits_perfect_ending():
    add "perfect_ending_credits" xsize 1920 ysize 1080

init -501 screen credits_non_perfect_ending():
    add "non_perfect_ending_credits" xsize 1920 ysize 1080
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
