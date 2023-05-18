screen minigame_intro():
    frame:
        background Frame("gui/minigame/copier_bg_main.png")
        xsize 851
        ysize 459
        xpos 534
        ypos 184

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            button:
                if not minigame_completed:
                    background Frame("gui/minigame/buttons/print_copy_disabled.png")
                else:
                    background Frame("gui/minigame/buttons/print_copy.png")
                    hover_background Frame("gui/minigame/buttons/print_copy_hover.png")
                    action Hide(screen="minigame_intro"), Call("scene_transition", "scene_7_w2_quantity")
                xsize 230
                ysize 286
            button:
                background Frame("gui/minigame/buttons/print_previous.png")
                hover_background Frame("gui/minigame/buttons/print_previous_hover.png")
                xsize 230
                ysize 286
                action Jump("scene_7_minigame_print_previous")
            button:
                background Frame("gui/minigame/buttons/troubleshooting.png")
                hover_background Frame("gui/minigame/buttons/troubleshooting_hover.png")
                action Jump("scene_7_minigame_main")
                xsize 230
                ysize 286

                if not minigame_completed:
                    frame:
                        background Frame("gui/minigame/alert_icon.png")
                        xsize 46
                        ysize 46
                        xpos 164
                        ypos 3

        if not minigame_completed:
            frame:
                background Color(gui.minigame_error_frame_color)
                ysize 39
                xsize 222
                xpos 62
                ypos 370
                text "ERROR":
                    xalign 0.5
                    yalign 0.5
                    text_align 0.5
                    color gui.minigame_error_text_color
                    font gui.minigame_error_text_font

screen minigame_butt_copy():
    frame:
        xfill True
        yfill True
        background None

        has transform:
            rotate 10
        frame:
            background Frame("gui/minigame/butt_copy.png")
            xsize 826
            ysize 625
            xalign 0.53
            ypos -60

screen minigame_main():
    on "show" action SetVariable("minigame_text", "[[TYPE A COMMAND]\n"), SetVariable("minigame_hacker_text_index", 0)
    $ renpy.dynamic("success_text_visible")
    $ success_text_visible = True
    frame:
        background Frame("gui/minigame/copier_bg_game.png")
        xsize 851
        ysize 459
        xpos 534
        ypos 184
        top_padding 30
        left_padding 20
        right_padding 20
        bottom_padding 30

        if not show_minigame_success_screen:
            timer 0.5 repeat True action If(minigame_text[-1] == '|', true=SetVariable("minigame_text", minigame_text[:-1]), false=SetVariable("minigame_text", minigame_text + '|'))
            if minigame_active and not minigame_completed:
                input:
                    xpos -1000
                    ypos -1000
                    changed minigame_text_input_changed
            text f'{minigame_text}':
                xfill True
                yfill True
                properties gui.text_properties("minigame")
        else:
            text f'[[ SUCCESS ]' at blink:
                font gui.minigame_text_font
                color gui.minigame_text_color
                size 40
                xalign 0.5
                yalign 0.5
                text_align 0.5


init python:
    minigame_hacker_text = ''
    with open(f'{renpy.config.gamedir}/text_files/minigame.txt', 'r') as file:
        minigame_hacker_text = file.read()

    def minigame_text_input_changed(value=""):
        global minigame_hacker_text_index, minigame_text, minigame_hacker_text_increment, minigame_completed, minigame_checkpoint_reached, minigame_checkpoint_2_reached
        if minigame_hacker_text_index == 0:
            minigame_text = '|'
        
        
        if minigame_hacker_text_index < len(minigame_hacker_text):
            revised_text = minigame_text
            if minigame_text[-1] == '|':
                revised_text = minigame_text[:-1]
            
            revised_text += minigame_hacker_text[minigame_hacker_text_index:minigame_hacker_text_index + minigame_hacker_text_increment]
            minigame_text = revised_text
            minigame_hacker_text_index += minigame_hacker_text_increment
        else:
            minigame_completed = True
        
        if minigame_hacker_text_index > minigame_checkpoint_index:
            minigame_checkpoint_reached = True
        
        if minigame_hacker_text_index > minigame_checkpoint_2_index:
            minigame_checkpoint_2_reached = True
        
        renpy.restart_interaction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
