












define config.name = _("Tax Heaven 3000")
define config.screen_width = 1920
define config.screen_height = 1080
define config.keyword_after_python = True



define gui.show_name = False

define config.keymap["dismiss"] = ["K_RIGHT"]
define config.keymap["focus_right"] = []
define config.keymap["focus_left"] = []
define config.keymap['screenshot'] = []
define config.keymap['toggle_fullscreen'] = []
define config.keymap['hide_windows'] = []
define config.keymap["accessibility"] = [],
define config.keymap["self_voicing"] = []
define config.keymap["clipboard_voicing"] = []
define config.keymap["debug_voicing"] = []
define config.keymap["rollback"] = []
define config.keymap["rollforward"] = []
define config.keymap["skip"] = []
define config.keymap["stop_skipping"] = []
define config.keymap["toggle_skip"] = []
define config.keymap["fast_skip"] = []



define config.keymap["toggle_fullscreen"] = []
define config.keymap["game_menu"] = []
define config.keymap["hide_windows"] = []
define config.keymap["launch_editor"] = []
define config.keymap["reload_game"] = []
define config.keymap["inspector"] = []
define config.keymap["full_inspector"] = []
define config.keymap["developer"] = []
define config.keymap["help"] = []
define config.keymap["choose_renderer"] = []
define config.keymap["progress_screen"] = []


define config.keymap["self_voicing"] = []
define config.keymap["clipboard_voicing"] = []
define config.keymap["debug_voicing"] = []


define config.keymap["rollforward"] = []


define config.keymap["focus_left"] = []
define config.keymap["focus_right"] = []
define config.keymap["focus_up"] = []
define config.keymap["focus_down"] = []


define config.keymap["viewport_leftarrow"] = []
define config.keymap["viewport_rightarrow"] = []
define config.keymap["viewport_uparrow"] = []
define config.keymap["viewport_downarrow"] = []
define config.keymap["viewport_wheelup"] = []
define config.keymap["viewport_wheeldown"] = []
define config.keymap["viewport_drag_start"] = []
define config.keymap["viewport_drag_end"] = []
define config.keymap["viewport_pageup"] = []
define config.keymap["viewport_pagedown"] = []


define config.keymap["fast_skip"] = []










define config.keymap["save_delete"] = []



define config.keymap["console"] = []
define config.keymap["console_older"] = []
define config.keymap["console_newer"] = []


define config.keymap["director"] = []


define config.keymap["toggle_music"] = []
define config.keymap["viewport_up"] = []
define config.keymap["viewport_down"] = []


define config.keymap["performance"] = []
define config.keymap["image_load_log"] = []
define config.keymap["profile_once"] = []
define config.keymap["memory_profile"] = []

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_text_cps = 50



define config.version = "1.0"





define gui.about = _p("""
""")






define build.name = "TaxHeaven3000"








define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.has_quicksave = False








define config.mouse = {
    'emotional_support_hand': [("gui/cursors/emotional_support_hand.webp", 75, 60)],
    'single_hand': [("gui/cursors/single_hand.webp", 75, 60)]
}




define config.main_menu_music = "audio/main_theme.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = dissolve
















define config.window = "hide"




define config.window_show_transition = Dissolve(.5)
define config.window_hide_transition = Dissolve(.5)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "TaxHeaven3000-1674076411"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.archive("dev_archive", "dev")

    build.classify('game/x-options-dev.rpyc', "dev_archive")

    build.package("mac-dev", "app-zip app-dmg", "mac renpy all dev")
    build.package("windows-dev", "zip", "windows renpy all dev")


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('wheels/*', None)
    build.classify('**/developer-log.txt', None)
    build.classify('**.rpy', None)

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")
    build.archive("video", "all")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")
    build.classify('game/log-options.rpyc', None)
    build.classify('entitlements.plist', None)
    build.classify('README.md', None)
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")
    build.classify("game/**.webm", "video")



    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
