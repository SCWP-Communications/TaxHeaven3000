label scene_6_intro:
    scene bg coffee
    jump scene_6_intro_dialogue
    $ clear_errors()

label scene_6_intro_dialogue:
    play music "audio/main_theme.ogg" fadein 0.5
    "Here we are back at the cafe. At this time of day it’s pretty calm, just a few people sitting at the tables, and some folks from the surrounding offices."
    "It looks like I’m here first. I guess I’ll get something to drink."

    $ screener_choice = None
    show screen screener_choice(choices=COFFEE_SCENE_MC_CHOICES)
    show barista at easein_fast, center
    barista "\"Hi there! What can I get you\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        barista "\"Hi there! What can I get you\""

    hide screen screener_choice

    $ iris_drink = None
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Yes, that would be a nice gesture", no_text="No, I'll let her decide what she wants when she arrives"), variant="narrator")
    "Alright! Should I get something for Iris…?"

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Alright! Should I get something for Iris…?"

    hide screen screener_choice
    if screener_choice:
        jump scene_6_get_iris_drink
    elif True:
        show barista at easeout, center
        jump scene_6_post_drink_order


label scene_6_get_iris_drink:
    $ screener_choice = None
    $ renpy.dynamic("iris_drink_choices")
    if scene_6b_completed and knows_iris_favorite_drink:
        $ iris_drink_choices = random.sample(COFFEE_SCENE_CHOICES, k=2)
        $ iris_drink_choices.append({"display": "”Ventichagomachiucci”","value": IRIS_FAV_DRINK_CHOICE})
    elif True:
        $ iris_drink_choices = random.sample(COFFEE_SCENE_CHOICES, k=3)

    show screen screener_choice(choices=iris_drink_choices + [{"display": "Nevermind, actually", "value": "nevermind"}])
    "Okay, I'll get her a..."
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Okay, I'll get her a..."

    hide screen screener_choice
    if screener_choice != "nevermind":
        $ iris_drink = screener_choice
        barista "\"Thanks! I’ll get your drinks going and bring it over to you when it’s ready.\""

    show barista at easeout, center
    jump scene_6_post_drink_order

label scene_6_post_drink_order:
    "I’ll get a seat by the window, the light is great in here."
    hide barista
    show iris_upright pose10 brows_sad eyes_neutral mouth_embarrassed more_blush at easein_fast
    i "\"Oh! [first_name] you beat me here. I hope I didn’t make you wait!\""
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush
    "She’s on-time to the minute, in fact, I was just here early."
    "\"Not at all! I just got here a little faster than I expected to. I’m still learning the town.\""
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open -more_blush
    i "\"Of course– say, [first_name] I was wondering, where do you live?\""

    jump scene_6_address

label scene_6_address:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open at move_left_from_center
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="My address is...", no_text="What exactly are you asking?"))
    i "\"What's your street address?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"What's your street address?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_6_address_input
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_looking_away mouth_talking at move_center_from_left
        i "\"Well, I want to know your current primary residential address! You know, if the IRS or something wanted to send you an official document, where would they send it?\""
        jump scene_6_address


label scene_6_address_input:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open at left
    show screen multi_line_input(ADDRESS_VALUES)
    i "\"What's your street address?\""
    while residential_address.line_1 == "" or residential_address.city == "" or residential_address.state == "" or residential_address.zip == "" or get_error_message_by_id("residential_address.state") is not None or get_error_message_by_id("residential_address.zip") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if residential_address.line_1 == "" and residential_address.city == "" and residential_address.state == "" and residential_address.zip == "":
            $ add_error("residential_address.line_1", "You must respond!")
            $ add_error("residential_address.city", "You must respond!")
            $ add_error("residential_address.state", "You must respond!")
            $ add_error("residential_address.zip", "You must respond!")
        i "\"What's your street address?\""

    hide screen multi_line_input
    jump scene_6_got_iris_drink

label scene_6_got_iris_drink:
    if iris_drink is not None:
        hide iris_upright
        show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush at move_center_from_left
        i "\"Sayyy, [first_name] is that drink for me? That’s so nice of you.\""
        if iris_drink == IRIS_FAV_DRINK_CHOICE:
            show iris_bent pose4 brows_sad eyes_crazy mouth_wide_open -more_blush
            i "\"And you got me a ventichagomachiucci?! Wow! I didn’t think anyone else knew about it, it’s my favorite drink!\""
        elif True:
            hide iris_bent
            show iris_upright pose8 brows_sad eyes_looking_away mouth_smiling at flipped
            i "\"Oh, it’s a [iris_drink]. Thanks [first_name], that was sweet of you.\""
        hide iris_bent
        show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open more_blush at move_left_from_center, flipped
        jump scene_6_dependent
    elif True:
        hide iris_bent
        show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open more_blush at left, flipped
        jump scene_6_dependent

label scene_6_dependent:
    $ someone_can_claim_as_dependent = None
    show screen choice_input("someone_can_claim_as_dependent", custom_yes_or_no_choices(yes_text="Someone does claim me as a dependent", no_text="No one claims me as a dependent", has_what=True, what_text="As a what? How would I know?"))
    i "\"I’m glad you could come meet me here [first_name]. I hope you don't mind me asking, but are you fully independent or does someone else claim you as a dependent on their tax return?\""
    while someone_can_claim_as_dependent == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("someone_can_claim_as_dependent", "You must respond!")
        i "\"I’m glad you could come meet me here [first_name]. I hope you don't mind me asking, but are you fully independent or does someone else claim you as a dependent on their tax return?\""
    hide screen choice_input
    if someone_can_claim_as_dependent == False:
        show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open more_blush at move_center_from_left, flipped
        jump scene_6_job
    elif someone_can_claim_as_dependent == True:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open
        i "\"I see! I hope you have a good support network in your life, [first_name]!\""
        jump scene_6_job
    elif True:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_neutral mouth_talking at move_center_from_left
        $ rollback_enabled = False
        i "\"Those are good questions, [first_name]. A dependent is someone who relies on another person for support, such as housing, food, clothing, and other necessities.\""
        $ rollback_enabled = True
        i "\"As far as I know, the best way to figure out if you’ve been claimed as a dependent on someone else’s return would be to ask the person who you think may have claimed you.\""
        $ rollback_enabled = False
        hide iris_bent
        show iris_upright pose9 brows_neutral eyes_neutral mouth_talking at move_left_from_center
        jump scene_6_dependent

label scene_6_job:
    "I’m kind of flattered that Iris is so interested in the details of my personal life situation. That said, her bluntness of inquiry is unlike anyone I’ve ever met!"
    "Somehow she makes even nosiness seem charming."
    jump scene_6_job_screener

label scene_6_job_screener:
    hide iris_bent
    show iris_upright pose8 brows_angry eyes_neutral mouth_wide_open at move_left_from_center, flipped

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="My job? I'm a...", no_text="What?"))
    i "\"And what do you do for a living, [first_name]? What is your job?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"And what do you do for a living, [first_name]? What is your job?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_6_job_input
    elif True:
        show iris_upright pose11 brows_neutral eyes_neutral mouth_wide_open at move_center_from_left

        i "\"I’ve had my fair share of interesting jobs and I’m eager to learn what you’re interested in. You know, IRS tax documents ask for your occupation–you can just give the best description you can.\""
        jump scene_6_job_screener
    jump scene_6_job_input

label scene_6_job_input:
    show screen one_line_input(label_text="Your job", value_name="occupation", placeholder_text="", changed_function=save_value_active_input_required)
    i "\"And what do you do for a living, [first_name]? What is your job?\""
    while occupation == "":
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("occupation", "You must respond!")
        i "\"And what do you do for a living, [first_name]? What is your job?\""

    hide screen one_line_input

    jump scene_6_blind_intro

label scene_6_blind_intro:
    hide iris_upright
    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling at move_center_from_left
    "Iris leans in, peering at me intently."

    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open more_blush
    i "\"You’ve got a very nice face, [first_name].\""
    i "\"I could look at you for hours~\""
    jump scene_6_blind

label scene_6_blind:
    $ is_blind = None
    show screen choice_input("is_blind", custom_yes_or_no_choices(yes_text="Yes, I was", no_text="Nope, I was not legally blind on 12/31/22", has_what=True, what_text="What?"))
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling more_blush at move_left_from_center, flipped
    i "\"How’s your vision [first_name]? Were you legally blind on 12/31/22?\""

    while is_blind == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("is_blind", "You must respond!")
        i "\"How’s your vision [first_name]? Were you legally blind on 12/31/22?\""

    hide screen choice_input
    if is_blind is not True and is_blind is not False:
        show iris_upright pose7 brows_neutral eyes_neutral mouth_talking -more_blush at flipped, move_center_from_left

        i "\"Are you not sure what legally blind means? Well, I guess I’m asking if you cannot see better than 20/200 in your better eye with glasses or contact lenses, or if your field of vision is not more than 20 degrees.\""
        jump scene_6_blind
    elif True:
        jump scene_6_social_security_number_intro

label scene_6_social_security_number_intro:
    hide iris_upright
    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling at move_center_from_left
    i "\"I heard someone say eyes are windows to the soul, so I’ve been trying to see if it’s true.\""
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"I like looking at you…and…feeling like I’m memorizing you…\""
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open more_blush
    i "\"Do you also like that feeling, [first_name]? I think it’s okay to get personal…\""
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_looking_away mouth_smiling more_blush at flipped
    i "\"I know! How about we each tell each other a secret.\""
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open more_blush at flipped
    i "\"Okay, you go first!\""

    jump scene_6_social_security_number_screener

label scene_6_social_security_number_screener:
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush at move_left_from_center
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="My social security number is...", no_text="What?"))
    i "\"%(first_name)s, what is your social security number?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"%(first_name)s, what is your social security number?\""

    hide screen screener_choice
    if not screener_choice:
        show iris_bent pose3 brows_neutral eyes_closed_neutral mouth_wide_open -more_blush at flipped, move_center_from_left
        i "\"[first_name], a social security number is a unique identifier issued by the Social Security Administration. I understand that it’s personal, but trust is required in a relationship.\""
        show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush at move_left_from_center
        jump scene_6_social_security_number_screener
    elif True:
        jump scene_6_social_security_number

label scene_6_social_security_number:
    show screen one_line_input(label_text="Your social security number", value_name="social_security_number", placeholder_text="XXX-XX-XXXX", changed_function=validate_and_save_ssn)
    i "\"%(first_name)s, what is your social security number?\""

    while social_security_number == "" or get_error_message_by_id("social_security_number") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if social_security_number == "":
            $ add_error("social_security_number", "You must respond!")
        i "\"%(first_name)s, what is your social security number?\""

    hide screen one_line_input

    jump scene_6_outro

label scene_6_outro:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush at move_center_from_left
    i "\"There’s something about you that makes me feel you’re very trustworthy [first_name]. I hope you feel the same way.\""
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush
    "\"Hang on Iris, you need to tell me a secret too.\""

    i "\"Hmmm. A secret…\""

    show iris_bent pose2 brows_sad eyes_wide_open mouth_embarrassed more_blush
    "Iris suddenly stares directly at me…no, more like through me. Her demeanor has changed completely. She looks haunted."
    hide iris_upright
    show iris_bent pose2 brows_angry eyes_wide_open mouth_frowning more_blush
    stop music fadeout 0.5
    $ ctc_disabled = True
    $ renpy.invoke_in_thread(reenable_ctc_after_time)
    i "\"Don’t ever get involved with TurboTax, [first_name]. They’re dangerous.\""
    play music "audio/main_theme.ogg" fadein 0.5
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush
    "As quick as it came, the moment is gone. Iris tips her head and is back to her usual bubbly self."
    hide iris_bent
    show iris_upright pose7 brows_angry eyes_crazy mouth_talking more_blush
    i "\"Oops, I didn’t mean to get so serious. Don’t mind me [first_name].\""

    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling -more_blush
    i "\"I’ll tell you a simpler secret. How about…\""

    show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open
    i "\"I’ve never been on an airplane before!\""

    show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed
    i "\"I’d like to travel someday but I don’t have a…\""

    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at flipped
    i "\"Well, anyway.\""


    "Somehow Iris makes it sound like she wouldn’t be allowed to board a plane."
    "I don’t understand, is she on the run or something?"
    "I know she said she wanted to share secrets but I feel like we’re only scratching the surface here."

    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open at flipped
    i "\"It’s really easy to talk to you, [first_name]. I’m glad we can be honest with each other.\""

    i "\"Let’s go out again!\""
    $ add_book_to_iris_desk()

    if office_visited:
        call pre_scene_8_interstitial ("cafe") from _call_pre_scene_8_interstitial
    elif True:
        window hide
        $ cafe_visited = True
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_4)
        $ update_completed_dates()
        $ calculate_return()
        $ purge_saves()
        jump generic_new_day

label pre_scene_8_interstitial(from_scene):
    i "\"Why don’t you come see me at the library sometime? There’s something I want to do for you.\""

    hide iris_bent
    show iris_upright pose8 brows_sad eyes_closed_happy mouth_smiling -more_blush at flipped
    i "\"I promise I’ll be there this time!\""

    window hide
    if from_scene == "cafe":
        $ cafe_visited = True
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_4)
    elif True:
        $ office_visited = True
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_6)
    $ update_completed_dates()
    $ calculate_return()
    $ purge_saves()


    jump generic_new_day

label generic_new_day:
    window hide
    stop music fadeout 1.0
    scene black
    with fade
    play sound "audio/new_day.ogg"
    pause 3
    $ show_overlay = False
    call scene_transition from _call_scene_transition_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
