label scene_1_intro:
    scene bg apartment
    play music "audio/main_theme.ogg" fadein 0.5
    $ show_overlay = False
    jump scene_1_monologue

label scene_1_monologue:
    "Phew, there we go! I’ve officially moved in."
    "Moving sure obliterates your ability to think about anything else. My mind is drained, and after hauling chairs into a new apartment my body isn't feeling much better."
    "Still, it's a fine bright day. This spring could be a fresh start! I'll be more organized, happier…maybe I'll even find that special someone."
    "Might as well walk around and get to know the town a little bit."
    "Plus – I need to grab a pencil to fill out some final paperwork for my lease. I should keep an eye for a stationery store or something."
    $ purge_saves()
    call scene_transition ("scene_2_intro") from _call_scene_transition_52
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
