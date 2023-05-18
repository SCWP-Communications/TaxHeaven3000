screen map():
    $ renpy.dynamic("office_button_background", "office_button_hover_background", "library_button_background", "library_button_hover_background", "cafe_button_background", "cafe_button_hover_background", "iris_house_button_background", "iris_house_button_hover_background", "office_button_action", "cafe_button_action", "library_button_action", "iris_house_action")
    on "show" action SetVariable("map_selected_screen", None)
    frame at easein_fast:
        style_prefix "map"
        background "gui/map/frame-map.png"
        xsize 1374
        ysize 504
        xalign 0.5
        ypos 152

        if dates_completed == 1 and not first_diary_visit_completed:
            $ office_button_background = Frame("gui/map/buttons/office-locked.webp")
            $ office_button_hover_background = Frame("gui/map/buttons/office-locked.webp")
            $ office_button_action = None

            $ library_button_background = Frame("gui/map/buttons/library-interest.webp")
            $ library_button_hover_background = Frame("gui/map/buttons/library-hover.webp")

            $ cafe_button_background = Frame("gui/map/buttons/cafe-idle.webp")
            $ cafe_button_hover_background = Frame("gui/map/buttons/cafe-hover.webp")
            $ cafe_button_action = [SetVariable("map_selected_screen", "the cafe"), renpy.curry(renpy.restart_interaction)]

            $ iris_house_button_background = Frame("gui/map/buttons/iris-house-locked.webp")
            $ iris_house_button_hover_background = None
            $ iris_house_action = None

        if dates_completed == 1 and first_diary_visit_completed:
            $ office_button_background = Frame("gui/map/buttons/office-interest.webp")
            $ office_button_hover_background = Frame("gui/map/buttons/office-hover.webp")
            $ office_button_action = [SetVariable("map_selected_screen", "the office"), renpy.curry(renpy.end_interaction)(True)]

            $ library_button_background = Frame("gui/map/buttons/library-idle.webp")
            $ library_button_hover_background = Frame("gui/map/buttons/library-hover.webp")

            $ cafe_button_background = Frame("gui/map/buttons/cafe-interest.webp")
            $ cafe_button_hover_background = Frame("gui/map/buttons/cafe-hover.webp")
            $ cafe_button_action = [SetVariable("map_selected_screen", "the cafe"), renpy.curry(renpy.end_interaction)(True)]

            $ iris_house_button_background = Frame("gui/map/buttons/iris-house-locked.webp")
            $ iris_house_button_hover_background = None
            $ iris_house_action = None

        if dates_completed == 2:
            if office_visited:
                $ office_button_background = Frame("gui/map/buttons/office-idle.webp")
            else:
                $ office_button_background = Frame("gui/map/buttons/office-interest.webp")
            $ office_button_hover_background = Frame("gui/map/buttons/office-hover.webp")
            $ office_button_action = [SetVariable("map_selected_screen", "the office"), renpy.curry(renpy.end_interaction)(True)]

            $ library_button_background = Frame("gui/map/buttons/library-idle.webp")
            $ library_button_hover_background = Frame("gui/map/buttons/library-hover.webp"
)
            if cafe_visited:
                $ cafe_button_background = Frame("gui/map/buttons/cafe-idle.webp")
            else:
                $ cafe_button_background = Frame("gui/map/buttons/cafe-interest.webp")
            $ cafe_button_hover_background = Frame("gui/map/buttons/cafe-hover.webp")
            $ cafe_button_action = [SetVariable("map_selected_screen", "the cafe"), renpy.curry(renpy.end_interaction)(True)]

            $ iris_house_button_background = Frame("gui/map/buttons/iris-house-locked.webp")
            $ iris_house_button_hover_background = None
            $ iris_house_action = None

        if dates_completed == 3:
            $ office_button_background = Frame("gui/map/buttons/office-idle.webp")
            $ office_button_hover_background = Frame("gui/map/buttons/office-hover.webp")
            $ office_button_action = [SetVariable("map_selected_screen", "the office"), renpy.curry(renpy.end_interaction)(True)]

            $ library_button_background = Frame("gui/map/buttons/library-interest.webp")
            $ library_button_hover_background = Frame("gui/map/buttons/library-hover.webp")

            $ cafe_button_background = Frame("gui/map/buttons/cafe-idle.webp")
            $ cafe_button_hover_background = Frame("gui/map/buttons/cafe-hover.webp")
            $ cafe_button_action = [SetVariable("map_selected_screen", "the cafe"), renpy.curry(renpy.end_interaction)(True)]

            $ iris_house_button_background = Frame("gui/map/buttons/iris-house-locked.webp")
            $ iris_house_button_hover_background = None
            $ iris_house_action = None

        if dates_completed == 4:
            $ office_button_background = Frame("gui/map/buttons/office-idle.webp")
            $ office_button_hover_background = Frame("gui/map/buttons/office-hover.webp")
            $ office_button_action = [SetVariable("map_selected_screen", "the office"), renpy.curry(renpy.end_interaction)(True)]

            $ library_button_background = Frame("gui/map/buttons/library-idle.webp")
            $ library_button_hover_background = Frame("gui/map/buttons/library-hover.webp")

            $ cafe_button_background = Frame("gui/map/buttons/cafe-idle.webp")
            $ cafe_button_hover_background = Frame("gui/map/buttons/cafe-hover.webp")
            $ cafe_button_action = [SetVariable("map_selected_screen", "the cafe"), renpy.curry(renpy.end_interaction)(True)]

            $ iris_house_button_background = Frame("gui/map/buttons/iris-house-interest.webp")
            $ iris_house_button_hover_background = Frame("gui/map/buttons/iris-house-hover.webp")
            $ iris_house_action = [SetVariable("map_selected_screen", "Iris' house"), renpy.curry(renpy.end_interaction)(True)]

















        imagebutton id "office_button":
            hover_sound "audio/button_click.ogg"
            if map_selected_screen == "the office":
                idle Frame("gui/map/buttons/office-selected.webp")
            else:
                idle office_button_background
                if ctc_disabled or map_selected_screen != None:
                    hover office_button_hover_background
                    action office_button_action
            xpos absolute(502)
            ypos absolute(11)
            xsize 386
            ysize 179
            focus_mask True
        imagebutton id "library_button":
            hover_sound "audio/button_click.ogg"
            if map_selected_screen == "the library":
                idle Frame("gui/map/buttons/library-selected.webp")
            else:
                idle library_button_background
                if ctc_disabled or map_selected_screen != None:
                    hover library_button_hover_background
                    action [SetVariable("map_selected_screen", "the library"), renpy.curry(renpy.restart_interaction)]
            xpos absolute(958)
            ypos absolute(120)
            xsize 386
            ysize 179
        imagebutton id "cafe_button":
            hover_sound "audio/button_click.ogg"
            if map_selected_screen == "the cafe":
                idle Frame("gui/map/buttons/cafe-selected.webp")
            else:
                idle cafe_button_background
                if ctc_disabled or map_selected_screen != None:
                    hover cafe_button_hover_background
                    action cafe_button_action
            xpos absolute(63)
            ypos absolute(123)
            xsize 386
            ysize 179
        imagebutton id "iris_house_button":
            hover_sound "audio/button_click.ogg"
            if map_selected_screen == "Iris' house":
                idle Frame("gui/map/buttons/iris-house-selected.webp")
            else:
                idle iris_house_button_background
                if ctc_disabled or map_selected_screen != None:
                    action iris_house_action
                    hover iris_house_button_hover_background
            xpos absolute(456)
            ypos absolute(254)
            xsize 486
            ysize 179

style map_button:
    padding (0, 0, 0, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
