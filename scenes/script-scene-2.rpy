label scene_2_intro:
    $ show_overlay = False
    scene bg sidewalk
    play music "audio/main_theme.ogg" fadein 0.5
    jump scene_2_intro_dialogue

label scene_2_intro_dialogue:
    "Well, it’s certainly not the biggest town in the world, but then again there’s always something to be said for walkable infrastructure!"
    "There’s a cute cafe near me, and the streets seem pretty lively. There’s a bit of a business district too."
    "Oh! Here we go. Is this a stationery store?"
    "It has a cute mascot, some kind of rabbit, and a cheerful font for the store name:\n“Mulberry Press.”"
    "I’m never sure exactly what kind of products a store like this sells, but I bet I can at least get a pencil in here–"
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open at flipped
    i "\"Uh oh! watch–– oof!\""
    show iris_upright pose10 brows_angry eyes_crazy mouth_embarrassed at flipped with vpunch

    "Yikes! I was so caught up trying to decipher the contents of this hygge little store that I wasn’t paying attention to where I was going and now I’ve bumped into––"

    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush

    i "\"Are you okay?\""
    "––this incredibly cute girl!"

    show iris_bent pose4 brows_sad eyes_wide_open mouth_embarrassed -more_blush

    i "\"I’m so sorry, I didn’t see you there! You’re not hurt, are you?\""
    "\"Yeah, looks like I’m fine.\""
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling
    "\"But hang on! How about, as an apology, you tell me your name?\""

    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_closed_happy mouth_smiling more_blush at flipped

    i "\"Ha ha! My name is Iris. What's yours?\""
    "\"I'm %(first_name)s. I just moved here\""
    jump scene_2_is_us_resident

label scene_2_is_us_resident:
    $ screener_choice = None
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling -more_blush at move_left_from_center, flipped
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="I...sure am!", no_text="Well, no, I'm not.", has_what=True, what_text="I\'m not sure"))
    i "\"Oh, really? So, %(first_name)s, you're a US resident?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Are you a US resident?\""

    if screener_choice == False:
        hide screen screener_choice
        hide iris_upright
        show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed at move_center_from_left
        i "\"%(first_name)s, I ummm, I think you're kinda cute but I don't think I can do long-distance right now.\""
        i "\"Maybe it's better if we just go our separate ways.\""
        call screen game_over_modal(jump_back_to="scene_2_is_us_resident", message="{i}Tax Heaven 3000{/i} only supports filers who are U.S. residents")
    elif screener_choice == True:
        show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling at move_center_from_left, flipped
        hide screen screener_choice
        jump scene_2_pencil_and_eraser
    elif True:
        hide screen screener_choice
        jump scene_2_has_green_card

label scene_2_has_green_card:
    $ screener_choice = None
    show iris_upright pose11 brows_neutral eyes_neutral mouth_smiling at left, flipped
    show screen screener_choice(choices=YES_OR_NO_CHOICES)
    i "Did you have a green card in [TAX_YEAR], [first_name]?"

    while screener_choice == None:
        i "Did you have a green card in [TAX_YEAR], [first_name]?"

    hide screen screener_choice
    if screener_choice:
        show iris_upright pose7 brows_neutral eyes_neutral mouth_smiling at move_center_from_left, flipped
        i "\"There you go then! That makes you a resident.\""
        jump scene_2_pencil_and_eraser
    elif True:
        jump scene_2_substantial_presence_test

label scene_2_substantial_presence_test:
    $ days_present_in_us = None
    show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open more_blush at move_center_from_left
    i "\"Okay, %(first_name)s, we can run through the Substantial Presence Test to see if you are considered a U.S. resident.\""

    show iris_upright pose8 brows_neutral eyes_neutral mouth_talking -more_blush at move_left_from_center, flipped
    show screen one_line_input(label_text="Number of days", value_name="days_present_in_us", placeholder_text="", changed_function=validate_and_save_active_input_number_of_days)
    i "\"How many days were you present in the US in {b}[TAX_YEAR]{/b}?\""

    while days_present_in_us == None or get_error_message_by_id('days_present_in_us') is not None:
        i "\"How many days were you present in the US in {b}[TAX_YEAR]{/b}?\""

    hide screen one_line_input
    if days_present_in_us < 31:
        show iris_upright pose8 brows_neutral eyes_neutral mouth_talking at move_center_from_left, flipped
        i "\"I see. That means you are not a resident of the US.\""
        i "\"%(first_name)s, I ummm, I think you're kinda cute but I don't think I can do long-distance right now.\""
        i "\"Maybe it's better if we just go our separate ways.\""
        call screen game_over_modal(jump_back_to="scene_2_is_us_resident", message="{i}Tax Heaven 3000{/i} only supports filers who are U.S. residents")
    elif True:
        jump scene_2_substantial_presence_year_prior

label scene_2_substantial_presence_year_prior:
    $ days_present_in_us_one_year_prior = None
    $ days_present_two_years_prior = None
    show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at left, flipped
    show screen one_line_input(label_text="Number of days", value_name="days_present_in_us_one_year_prior", placeholder_text="", changed_function=validate_and_save_active_input_number_of_days)
    i "\"And how about the year prior? How many days were you present in the US in {b}[PREVIOUS_TAX_YEAR]{/b}?\""

    while days_present_in_us_one_year_prior == None or get_error_message_by_id('days_present_in_us_one_year_prior') is not None:
        i "\"And how about the year prior? How many days were you present in the US in {b}[PREVIOUS_TAX_YEAR]{/b}?\""

    hide screen one_line_input
    show screen one_line_input(label_text="Number of days", value_name="days_present_two_years_prior", placeholder_text="", changed_function=validate_and_save_active_input_number_of_days)

    show iris_upright pose9 brows_neutral eyes_neutral mouth_talking at left, flipped
    i "\"Now, this may seem like ancient history, but how many days were you present in the US in {b}[TWO_YEARS_PRIOR]{/b}?\""
    while days_present_two_years_prior == None or get_error_message_by_id('days_present_two_years_prior') is not None:
        i "\"Now, this may seem like ancient history, but how many days were you present in the US in {b}[TWO_YEARS_PRIOR]{/b}?\""

    hide screen one_line_input
    if days_present_two_years_prior + days_present_in_us_one_year_prior < 183:
        show iris_upright pose7 brows_sad eyes_closed_neutral mouth_frowning at move_center_from_left, flipped
        i "\"Hmmm, %(first_name)s, based on the information you've told me, I don't think you're considered a U.S. resident for tax purposes.\""
        i "\"I see. That means you are not a resident of the US.\""
        i "\"%(first_name)s, I ummm, I think you're kinda cute but I don't think I can do long-distance right now.\""
        i "\"Maybe it's better if we just go our separate ways.\""
        call screen game_over_modal(jump_back_to="scene_2_is_us_resident", message="{i}Tax Heaven 3000{/i} only supports filers who are U.S. residents")
    elif True:
        show iris_upright pose7 brows_neutral eyes_neutral mouth_wide_open at move_center_from_left, flipped
        i "\"Okay, %(first_name)s, based on the information you’ve told me, you are considered a U.S. resident for tax purposes!\""
        jump scene_2_pencil_and_eraser

label scene_2_pencil_and_eraser:
    "This girl makes a weirdly nationalist first impression."
    "\"Say, you were just coming out of this store when you bumped into me, right? Is it a stationery store? I need to buy a pencil.\""
    hide iris_upright
    show iris_bent pose6 brows_neutral eyes_wide_open mouth_wide_open

    i "\"Oooh! [first_name], do you like stationery?? I have a little notebook that I write down everything in\""
    i "\"What I did today, new things I learned, cute people I– well, anyway, it’s like a second memory!\""

    hide iris_bent
    show pencil_eraser at pen_center, easein
    i "\"Here, these are for you!\""
    "This is…a really fancy technical pencil and a super cute eraser. I don’t think I’ve ever put this much thought into choosing a writing instrument in my life."
    hide pencil_eraser

label scene_2_ending_dialogue:
    show iris_bent pose5 brows_neutral eyes_looking_away mouth_wide_open more_blush at easein_fast
    i "\"I’ve tested a lot of writing supplies and these are my favorites. You never know when you’ll need a good pencil, [first_name]!\""
    i "\"Maybe you want to write down your social security number, or give someone your phone number.\""
    "\"Thank you, Iris!\""
    show iris_bent pose6 brows_neutral eyes_closed_happy mouth_wide_open -more_blush
    i "\"It’s so exciting to move to a new town!\""
    i "\"I’d be happy to show you around and maybe talk some more–\""

    show iris_bent pose4 brows_neutral eyes_looking_away mouth_smiling more_blush
    i "\"Uh…if you’re not too busy that is.\""
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open
    i "\"I know it’s tax season so some people are–\""
    "\"I’d love that!\""

    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open at flipped

    i "\"Okay! I need to get back to work. How about getting coffee tomorrow?\""
    i "\"12:30, Okay? I’ll meet you at the cafe!\""

    show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open at easeout, flipped
    "Wow, lucky! I can’t believe I bumped into this super cute girl outside a stationery store. And on my first real day in town!"
    hide iris_upright

    call scene_transition ("scene_2_alarm_clock") from _call_scene_transition_53

label scene_2_alarm_clock:
    $ show_overlay = False
    scene black
    pause 0.6
    scene bg alarm clock
    with fade

    "Wait, did she say tax season?"
    "..."
    "It's almost April 18th and I haven't done my taxes!"
    "Ugh. Now's not the time to worry about it, but I'll have to deal with that soon."
    "In any case, I've got a date with a cute girl to look forward to. At least I {i}think{/i} it's a date."

    $ purge_saves()
    scene black
    with fade
    jump new_day_1

label new_day_1:
    scene black
    window hide
    play sound "audio/new_day.ogg"
    pause 3
    call scene_transition ("new_day_sidewalk") from _call_scene_transition_54

label new_day_sidewalk:
    $ show_overlay = False
    scene bg sidewalk
    pause 0.8
    play music "audio/main_theme.ogg" fadein 0.5
    "Ahh~ I needed a good rest after unpacking all day yesterday."
    "What now?"
    "I told Iris I’d meet her for coffee…"
    "Better get going!"

    stop music fadeout 0.2
    play sound "audio/wipe.ogg"
    call scene_transition ("scene_3_intro") from _call_scene_transition_55
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
