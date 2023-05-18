screen copier_download():
    button:
        xsize 851
        ysize 459
        xpos 534
        ypos 184
        action NullAction()
        if ready_for_return_printing:
            mouse "emotional_support_hand"

        frame:
            background Frame("gui/minigame/copier_bg_main.png")
            xfill True
            yfill True
            has hbox:
                xalign 0.5
                yalign 0.5
                spacing 15
            button:
                if ready_for_return_printing:
                    mouse "emotional_support_hand"

                if not ready_for_return_printing:
                    background Frame("gui/minigame/buttons/download_returns.png")
                elif not downloaded_return:
                    background Frame("gui/minigame/buttons/download_returns.png")
                    hover_background Frame("gui/minigame/buttons/download_returns_hover.png")
                    action Function(download_file, return_file_location, 'return_file_location')
                else:
                    background Frame("gui/minigame/buttons/returns_downloaded_success.png")

                xsize 417
                ysize 162
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
