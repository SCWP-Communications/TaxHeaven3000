label scene_7_intro:
    scene office_animated
    show iris_upright pose11 brows_neutral eyes_neutral mouth_wide_open at flipped, easein_fast
    play music "audio/main_theme.ogg" fadein 0.5
    i "\"Hey [first_name]! Over here!\""
    show iris_upright pose7 brows_angry eyes_crazy mouth_talking more_blush at flipped
    i "\"I don’t have to go to the branch office very often. I don’t really like the atmosphere in here.\""

    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open -more_blush
    i "\"Thanks for keeping me company today.\""

    "The library branch office is a pretty stereotypical office. The rows of desks and cubicles, the water cooler, the copying machine…it’s all so picture perfect it almost feels like set dressing."
    "I’m not entirely sure why this dry, stereotypical office building makes Iris uncomfortable, but I’m happy to tag along if it means I can spend some more time with her."

    hide iris_upright
    show iris_bent pose4 brows_angry eyes_crazy mouth_embarrassed more_blush

    i "\"Uh oh… the copy machine isn’t working…\""
    show iris_bent pose2 brows_sad eyes_wide_open mouth_embarrassed more_blush
    i "\"[first_name] can you help me fix this?\""

    "Way to put me on the spot, Iris!"
    show iris_bent pose2 brows_sad eyes_wide_open mouth_smiling -more_blush
    "Fixing a photocopier in front of a live (very attractive) audience…"
    "There are few worse things I can imagine!"
    hide iris_bent
    jump scene_7_minigame_intro_bg

label scene_7_minigame_intro_bg:
    scene bg copier with fade
    window show
    show screen minigame_intro with dissolve
    "Okay here we go. [first_name], this is no problem. You can troubleshoot a photocopier."
    jump scene_7_minigame_intro

label scene_7_minigame_intro:
    $ ctc_disabled = True
    while True:
        "Let's see what this printer interface is like."

label scene_7_minigame_print_previous:
    scene bg copier
    $ ctc_disabled = False
    show screen minigame_butt_copy with dissolve
    hide screen minigame_intro
    "Huh, I guess the last person who used this machine photocopied their butt!\nAnyways, I better try to fix this thing."
    hide screen minigame_butt_copy
    show screen minigame_intro
    with dissolve
    jump scene_7_minigame_intro

label scene_7_minigame_main:
    scene bg copier game
    hide screen minigame_intro
    show screen minigame_main
    $ ctc_disabled = False
    $ renpy.restart_interaction()
    $ minigame_active = False
    $ minigame_checkpoint_reached = False
    $ minigame_checkpoint_2_reached = False
    $ minigame_completed = False
    $ show_minigame_success_screen = False
    play music "audio/diary_remix.ogg"

    i "\"Wow [first_name]! You’re really technical. What’s wrong? Don’t stop now.\""
    "Oh geez. What the heck is this?"
    "This appears to be terminal access to the photocopier? What am I supposed to do, hack the machine?"
    i "\"So, you can hack the machine right? It should be pretty simple.\""
    "Oh my god I’m about to embarrass myself in front of Iris. I don’t know what I’m doing!"
    $ ctc_disabled = True
    $ minigame_active = True
    $ renpy.restart_interaction()
    "I can’t just sit here. I’ve got to at least type SOMETHING in here.{p=4}{nw}"

    if minigame_text == "[[TYPE A COMMAND]\n" or minigame_text == "[[TYPE A COMMAND]\n|":
        "I’d better just hit some keys on the keyboard. I’ve got to at least try!{nw}"
        while not minigame_checkpoint_reached:
            "I’d better just hit some keys on the keyboard. I’ve got to at least try!{fast}{nw}"
    elif True:
        while not minigame_checkpoint_reached:
            "I can’t just sit here. I’ve got to at least type SOMETHING in here.{fast}{nw}"

    "I...holy shit... I'm on fire! I can see the code!{nw}"
    while not minigame_checkpoint_2_reached:
        "I...holy shit... I'm on fire! I can see the code!{fast}{nw}"

    "I am the one! Iris! Witness me!{nw}"

    while not minigame_completed:
        "I am the one! Iris! Witness me!{fast}{nw}"

    $ ctc_disabled = False
    $ renpy.restart_interaction()
    play sound "audio/printer.ogg"
    "…I’ve got it!!! That’s it. Once I hit confirm, it’s fixed."
    $ show_minigame_success_screen = True
    "I cannot believe this worked."
    stop sound fadeout 1.0
    stop music fadeout 1.0
    hide screen minigame_main
    jump scene_7_upload_intro

label scene_7_upload_intro:
    scene bg office on with fade
    play music "audio/main_theme.ogg" fadein 0.5
    show iris_upright pose10 brows_angry eyes_neutral mouth_wide_open more_blush at easein_fast

    i "\"Wow [first_name] I’m impressed! I think you fixed it! Hehe, you sure are good with your fingers.\""

    show iris_upright pose8 brows_sad eyes_closed_happy mouth_smiling
    "I feel like I’m hyperventilating."
    "This is the kind of flow state that an athlete experiences once in their life and then dreams of forever after."
    "I’ve tapped into an elevated state of consciousness to impress a girl by fixing her office photocopier."

    hide iris_upright
    show iris_bent pose3 brows_angry eyes_wide_open mouth_talking more_blush
    i "Alright! The first thing we’ll need is a document to test with."
    jump scene_7_w2_quantity

label scene_7_w2_quantity:
    scene bg office on
    show iris_bent pose3 brows_angry eyes_wide_open mouth_talking more_blush at move_left_from_center
    $ has_more_than_one_w2 = None
    $ ctc_disabled = False
    show screen choice_input("has_more_than_one_w2", choices=W2_FORM_CHOICES)
    i "\"I know! [first_name] let’s use your W-2 form! So do you have more than one W-2 for [TAX_YEAR], or just one?\""
    while has_more_than_one_w2 == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_more_than_one_w2", "You must respond!")
        i "\"I know! [first_name] let’s use your W-2 form! So do you have more than one W-2 for [TAX_YEAR], or just one??\""

    hide screen choice_input
    if has_more_than_one_w2 is not True and has_more_than_one_w2 is not False:
        hide iris_bent
        show iris_upright pose8 brows_neutral eyes_neutral mouth_talking at move_center_from_left
        i "\"A form W-2 is a tax form issued by a full or part-time employer. It reports the employee’s income for the year, as well as the amount of tax withheld from their paychecks.\""
        hide iris_upright
        jump scene_7_w2_quantity

    $ w2s_to_upload = 0

    hide screen choice_input
    jump scene_7_w2_upload_screener

label scene_7_w2_upload_screener:
    hide iris_bent
    show iris_upright pose8 brows_sad eyes_neutral mouth_wide_open at left, flipped
    $ screener_choice = None
    if has_more_than_one_w2:
        show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Okay, got it..", no_text="Hang on, I need to go get my W-2 forms!"))
        i "\"Okay! Let’s just start with one for now, and then we’ll do the others after we finish up with the first.\""

        while screener_choice is None:
            play sound "audio/error_beep.ogg" volume 0.3
            $ add_error("screener_choice", "You must respond!")
            i "\"Okay! Let’s just start with one for now, and then we’ll do the others after we finish up with the first.\""
    elif True:
        show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Okay, got it..", no_text="Hang on, I need to go get my W-2!"))
        i "\"Great, grab it and slide it into the copier feed.\""

        while screener_choice is None:
            play sound "audio/error_beep.ogg" volume 0.3
            $ add_error("screener_choice", "You must respond!")
            i "\"Great, grab it and slide it into the copier feed.\""

    hide screen screener_choice
    if screener_choice:
        jump scene_7_w2_upload
    elif True:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at move_center_from_left
        i "\"Okay! Take your time, I’ll wait for you~.\""
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_smiling at flipped
        i "\"Make sure to get all your W-2 forms as .PDF files that you can access.\""
        "...Alright. I've got them now."
        jump scene_7_w2_upload

label scene_7_w2_upload:
    $ w2s_to_upload += 1
    hide iris_bent
    show iris_upright pose8 brows_sad eyes_neutral mouth_wide_open at left, flipped
    show screen w2_upload_modal(w2s_to_upload)
    i "\"Great, grab the form and slide it into the copier feed.\""

    while len(w2_objects) < w2s_to_upload:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("w2_objects", "You must upload a file!")
        i "\"Great, grab the form and slide it into the copier feed.\""

    hide screen w2_upload_modal

    if w2s_to_upload == 1:
        jump scene_7_first_w2_interstitial
    elif True:
        jump scene_7_other_w2_interstitial

label scene_7_first_w2_interstitial:
    hide iris_upright
    show iris_bent pose1 brows_neutral eyes_wide_open mouth_wide_open at move_center_from_left
    i "\"Great, we’ve got that W-2 copied! Let’s make sure everything is clear.\""
    i "\"Come over here [first_name] and so we can look over these prints.\""

    show iris_bent pose2 brows_sad eyes_looking_away mouth_smiling more_blush

    i "\"It’s okay silly! You can stand closer than that. \""
    "Iris leans up next to me. She’s very close. I can’t help noticing that she smells nice."

    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_wide_open at flipped
    i "\"Mmm, that’s better. Now…\""

    jump scene_7_taxable_income

label scene_7_other_w2_interstitial:
    show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open at move_center_from_left
    i "\"Okay, all done! Now let’s make sure everything is copied clearly.\""
    jump scene_7_taxable_income

label scene_7_taxable_income:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_wide_open mouth_talking at move_left_from_center

    show screen one_line_input(label_text="Your taxable income", value_name=f"w2_objects[{w2s_to_upload-1}].box_1", placeholder_text="", changed_function=validate_and_save_dollar_active_field_array_property, value_type="arr_prop_float")
    i "\"What was your total taxable income in [TAX_YEAR], as reported on this W-2? That should be in Box 1 of your W-2 form.\""

    while w2_objects[w2s_to_upload-1].box_1 == 0 or w2_objects[w2s_to_upload-1].box_1 == None or get_error_message_by_id(f"w2_objects[{w2s_to_upload-1}].box_1") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if w2_objects[w2s_to_upload-1].box_1 == 0 or w2_objects[w2s_to_upload-1].box_1 == None:
            $ add_error(f"w2_objects[{w2s_to_upload-1}].box_1", "You must respond!")
        i "\"What was your total taxable income in [TAX_YEAR], as reported on this W-2? That should be in Box 1 of your W-2 form.\""

    hide screen one_line_input
    jump scene_7_federal_tax_witheld

label scene_7_federal_tax_witheld:
    show screen one_line_input(label_text="Federal tax witheld", value_name=f"w2_objects[{w2s_to_upload-1}].box_2", placeholder_text="", changed_function=validate_and_save_dollar_active_field_array_property, value_type="arr_prop_float")
    i "\"You’ve been working hard, [first_name]! Next up let’s make sure we’ve got your withheld income tax - that should be Box 2 of your W-2 form.\""

    while (get_error_message_by_id(f"w2_objects[{w2s_to_upload-1}].box_2") is not None) or w2_objects[w2s_to_upload-1].box_2 == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if w2_objects[w2s_to_upload-1].box_2 == None:
            $ add_error(f"w2_objects[{w2s_to_upload-1}].box_2", "You must respond!")
        i "\"You’ve been working hard, [first_name]! Next up let’s make sure we’ve got your withheld income tax - that should be Box 2 of your W-2 form.\""

    hide screen one_line_input
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at move_center_from_left
    i "\"Alright, that seems clear.\""
    jump scene_7_social_security_tax_witheld

label scene_7_social_security_tax_witheld:
    show iris_bent pose3 brows_neutral eyes_wide_open mouth_talking at move_left_from_center
    show screen one_line_input(label_text="Tax witheld", value_name=f"w2_objects[{w2s_to_upload-1}].box_4", placeholder_text="", changed_function=validate_and_save_dollar_active_field_array_property, value_type="arr_prop_float")
    i "\"In addition to that, how much social security tax was withheld from your income on this W-2? That should be Box 4\""

    while get_error_message_by_id(f"w2_objects[{w2s_to_upload-1}].box_4") is not None or w2_objects[w2s_to_upload-1].box_4 == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if w2_objects[w2s_to_upload-1].box_4 == None:
            $ add_error(f"w2_objects[{w2s_to_upload-1}].box_4", "You must respond!")
        i "\"In addition to that, how much social security tax was withheld from your income on this W-2? That should be Box 4\""

    hide screen one_line_input
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush at move_center_from_left
    i "\"Got it. Hehe, let’s promise not to withhold anything from each other, okay?\""
    if w2_objects[w2s_to_upload-1].box_4 > max_social_security_tax_this_year:
        hide iris_bent
        show iris_upright pose11 brows_sad eyes_looking_away mouth_embarrassed
        i "\"Hmmm, you know, [first_name], the federal limit on social security holding for [TAX_YEAR] is $9,114. It looks like your emplyer may have witheld excess social security tax from your paychecks. They should adjust the tax for you, but you'll need to talk to them.\""
        i "\"If they won't adjust it, you can file a claim for a refund using form 843.\""
        i "\"I'm sorry, [first_name], but I'm not great at dealing with situations like this. You'll need to talk to your employer yourself.\""
        jump scene_7_box_12_screener
    elif True:
        jump scene_7_box_12_screener

label scene_7_box_12_screener:
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices())
    $ calculate_return_up_to_agi()
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling more_blush at left, flipped
    i "\"[first_name], is there a code listed in box 12 of this W-2? You might have more than one.\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"[first_name], is there a code listed in box 12 of this W-2? You might have more than one.\""

    hide screen screener_choice
    if screener_choice:
        jump scene_7_box_12_code_choice
    elif True:
        jump scene_7_more_w2s_choice

label scene_7_box_12_code_choice:
    $ screener_choices = []
    show screen screener_multi_choice(choices=BOX_12_CHOICES)
    $ calculate_return_up_to_agi()
    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open at left, flipped
    i "\"Okay! Which codes do you have? I think we’re past the point of shyness, [first_name]: Tell me all that apply!\""

    while screener_choices == []:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choices", "You must respond!")
        i "\"Okay! Which codes do you have? I think we’re past the point of shyness, [first_name]: Tell me all that apply!\""

    hide screen screener_multi_choice
    if BOX_12_RED_CHOICE in screener_choices:
        hide iris_bent
        show iris_upright pose10 brows_angry eyes_crazy mouth_embarrassed at move_center_from_left
        i "\"Oh you… you do?\""
        show iris_upright pose7 brows_sad eyes_neutral mouth_embarrassed
        i "\"Um, I’m sorry [first_name] but I think you’re getting to be a little more than I bargained for.\""
        i "\"I’m trying to avoid any…complicated situations, you know?\""
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_looking_away mouth_embarrassed more_blush at flipped
        i "\"I didn’t mean for this to get weird but…maybe we shouldn’t see each other anymore.\""
        call screen game_over_modal(jump_back_to="scene_7_box_12_screener", message="Your tax status is more complex than {i}Tax Heaven 3000{/i} currently supports")
    elif BOX_12_YELLOW_CHOICE in screener_choices and form_1040_line_11 <= 34000:
        jump scene_7_box_12_warning
    elif True:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open more_blush at move_center_from_left, flipped
        i "\"Got it! These are informational codes. That’s easy! \""
        jump scene_7_more_w2s_choice

label scene_7_box_12_warning:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at move_center_from_left
    i "\"Hmm I see…\""

    show iris_bent pose3 brows_sad eyes_wide_open mouth_embarrassed at flipped
    i "\"I have a confession to make, [first_name]. You might be eligible for specific credits that I haven’t learned about yet.\""

    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling
    i "\"We can keep seeing each other but…\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Continue with suboptimal return", no_text="Exit"))
    i "\"You have to understand that I might not know how to maximize your return…\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"You have to understand that I might not know how to maximize your return…\""

    hide screen screener_choice
    if screener_choice:
        jump scene_7_more_w2s_choice
    elif True:
        $ MainMenu(confirm=False, save=False)()

label scene_7_more_w2s_choice:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_wide_open mouth_talking at move_left_from_center
    $ has_more_w2s_to_upload = None
    show screen choice_input("has_more_w2s_to_upload", choices=custom_yes_or_no_choices(yes_text="I've got more", no_text="No, that's it"))
    i "\"Now, did you have more Forms W-2, or was that the last one?\""

    while has_more_w2s_to_upload == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_more_w2s_to_upload", "You must respond!")
        i "\"Now, did you have more Forms W-2, or was that the last one?\""

    if has_more_w2s_to_upload:
        hide screen choice_input
        jump scene_7_w2_upload
    elif True:
        $ total_amount_w2_box_1 = get_total_w2_box_1()
        hide screen choice_input
        jump scene_7_other_income_intro

label scene_7_other_income_intro:
    show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open at move_center_from_left
    i "\"…You know I’m always looking for ways to make a little more on the side..\""

    jump scene_7_employee_wages_not_on_w2

label scene_7_employee_wages_not_on_w2:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling at move_left_from_center, flipped
    $ has_household_wages_not_reported_on_w2 = None
    show screen choice_input("has_household_wages_not_reported_on_w2", choices=custom_yes_or_no_choices(has_what=True, what_text="What?"))
    i "\"Did you have any household employee wages for [TAX_YEAR] that weren’t reported on form W-2?\""

    while has_household_wages_not_reported_on_w2 == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_household_wages_not_reported_on_w2", "You must respond!")
        i "\"Did you have any household employee wages for [TAX_YEAR] that weren’t reported on form W-2?\""

    hide screen choice_input
    if has_household_wages_not_reported_on_w2 is True:
        jump scene_7_input_employee_wages_not_on_w2
    elif has_household_wages_not_reported_on_w2 is False:
        $ household_empoloyee_wages_not_reported_on_w2 = 0
        jump scene_7_income_interest_intro
    elif True:
        hide iris_bent
        show iris_upright pose8 brows_neutral eyes_neutral mouth_talking at flipped, move_center_from_left
        $ rollback_enabled = False
        i "\"A household employee is paid to provide a service within their employer’s residence. For example, a housekeeper, maid, baby-sitter, gardener, or other individual who works in or around private residences is a household employee!\""
        $ rollback_enabled = True
        i "\"If a household employee is paid more than $1,900, the employer is required to withhold social security and medicare taxes, and issue the employee a form W-2.\""
        i "\"If the employee is paid less than $1,900, the employer is not required to issue a form W-2 but the earnings still must be reported on the employee’s tax return.\""
        i "\"That’s why I wanted to ask about it separately, [first_name].\""
        $ rollback_enabled = False
        hide iris_upright
        hide screen choice_input
        jump scene_7_employee_wages_not_on_w2

label scene_7_input_employee_wages_not_on_w2:
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_wink mouth_wide_open more_blush at left
    show screen one_line_input(label_text="Employee wages not reported", value_name="household_empoloyee_wages_not_reported_on_w2", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"Hehe. There’s always more to you than meets the eye. What amount of household employee wages did you have?\""

    while get_error_message_by_id("household_empoloyee_wages_not_reported_on_w2") is not None or household_empoloyee_wages_not_reported_on_w2 == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if household_empoloyee_wages_not_reported_on_w2 == None:
            $ add_error("household_empoloyee_wages_not_reported_on_w2", "You must respond!")
        i "\"Hehe. There’s always more to you than meets the eye. What amount of household employee wages did you have?\""

    hide screen one_line_input
    if household_empoloyee_wages_not_reported_on_w2 >= 1900:
        $ household_empoloyee_wages_not_reported_on_w2 = 0
        jump scene_7_too_much_employee_wages_not_on_w2
    elif True:
        jump scene_7_income_interest_intro

label scene_7_too_much_employee_wages_not_on_w2:
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Oops, okay nevermind I'll record this income differently", no_text="Oh hang on, I didn't actually make this much in household employee wages. I made..."))
    i "\"Wow, [first_name]! Technically, if you made household employee wages of $1,900 or more, you should have been issued a W-2, and should report it that way.\""
    while screener_choice == None:
        i "\"Wow, [first_name]! Technically, if you made household employee wages of $1,900 or more, you should have been issued a W-2, and should report it that way.\""

    hide screen screener_choice
    if screener_choice:
        jump scene_7_more_w2s_choice
    elif True:
        jump scene_7_input_employee_wages_not_on_w2

label scene_7_income_interest_intro:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_wide_open more_blush at move_center_from_left, flipped
    i "\"I know there are a few other sources of income some people have. How about you, [first_name]?\""
    i "\"As long as we’re here we should make copies of all your forms!\""

    jump scene_7_income_interest

label scene_7_income_interest:
    $ has_income_interest = None
    $ int_1099_index = 0
    show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open at move_left_from_center, flipped
    show screen choice_input("has_income_interest", choices=custom_yes_or_no_choices(yes_text="Yes, I did get one or more Forms 1099-INT", no_text="No, I didn't get any 1099-INT forms for 2022"))
    i "\"Did you have any income from interest in [TAX_YEAR], [first_name]? You’d know by whether or not you received one or more Forms 1099-INT.\""

    while has_income_interest == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_income_interest", "You must respond!")
        i "\"Did you have any income from interest in [TAX_YEAR], [first_name]? You’d know by whether or not you received one or more Forms 1099-INT.\""

    if has_income_interest is True:
        hide screen choice_input
        jump scene_7_interest_income_input_intro
    elif has_income_interest is False:
        hide screen choice_input 
        jump scene_7_social_security_benefits

label scene_7_interest_income_input_intro:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_wide_open mouth_smiling at move_center_from_left, flipped
    i "\"Oh that’s great, [first_name]! I’m not too knowledgeable about interest income– maybe you could give me lessons.\""

    jump scene_7_income_interest_input_payer_name

label scene_7_income_interest_input_payer_name:
    $ int_1099_objects.append(Int1099())
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open at move_left_from_center, flipped
    show screen one_line_input(label_text="Payer Name", value_name=f"int_1099_objects[{int_1099_index}].payer_name", placeholder_text="", changed_function=validate_and_save_active_input_required_array_property, value_type="arr_prop_str")
    if len(int_1099_objects) == 1:
        i "\"Let’s start with your first 1099-INT form. What was the name of the payer?\""
    elif True:
        i "\"What was the name of your payer?\""

    while get_error_message_by_id(f"int_1099_objects[{int_1099_index}].payer_name") is not None or int_1099_objects[int_1099_index].payer_name is "":
        play sound "audio/error_beep.ogg" volume 0.3
        if int_1099_objects[int_1099_index].payer_name is "":
            $ add_error(f"int_1099_objects[{int_1099_index}].payer_name", "You must respond!")
        if len(int_1099_objects) == 1:
            i "\"Let’s start with your first 1099-INT form. What was the name of the payer?\""
        elif True:
            i "\"What was the name of your payer?\""

    hide screen one_line_input
    jump scene_7_income_interest_input_total_interest

label scene_7_income_interest_input_total_interest:
    show screen one_line_input(label_text="Total Interest", value_name=f"int_1099_objects[{int_1099_index}].total_interest", placeholder_text="", changed_function=validate_and_save_dollar_active_field_array_property, value_type="arr_prop_float")
    i "\"And how much total interest income did you have from this payer? This information can be found in Box 1 of the Form 1099-INT.\""

    while get_error_message_by_id(f"int_1099_objects[{int_1099_index}].total_interest") is not None or int_1099_objects[int_1099_index].total_interest is None:
        play sound "audio/error_beep.ogg" volume 0.3
        if int_1099_objects[int_1099_index].total_interest is None:
            $ add_error(f"int_1099_objects[{int_1099_index}].total_interest", "You must respond!")
        i "\"And how much total interest income did you have from this payer? This information can be found in Box 1 of the Form 1099-INT.\""

    hide screen one_line_input
    jump scene_7_income_interest_input_tax_exempt_amount

label scene_7_income_interest_input_tax_exempt_amount:
    show screen one_line_input(label_text="Tax Exempt Interest", value_name=f"int_1099_objects[{int_1099_index}].tax_exempt_interest", placeholder_text="", changed_function=validate_and_save_dollar_active_field_array_property, value_type="arr_prop_float")
    i "\"Was any portion of tax exempt %(first_name)s? This information would be listed in box 8 of form 1099-INT.\""

    while get_error_message_by_id(f"int_1099_objects[{int_1099_index}].tax_exempt_interest") is not None or int_1099_objects[int_1099_index].tax_exempt_interest is None:
        play sound "audio/error_beep.ogg" volume 0.3
        if int_1099_objects[int_1099_index].tax_exempt_interest is None:
            $ add_error(f"int_1099_objects[{int_1099_index}].tax_exempt_interest", "You must respond!")
        i "\"Was any portion of tax exempt %(first_name)s? This information would be listed in box 8 of form 1099-INT.\""
    hide screen one_line_input

    if int_1099_objects[int_1099_index].tax_exempt_interest > 0:
        hide iris_upright
        show iris_bent pose4 brows_sad eyes_looking_away mouth_smiling more_blush at move_center_from_left, flipped
        i "\"Oh wow! You must be pretty savvy\""

    jump scene_7_income_interest_income_tax_witheld

label scene_7_income_interest_income_tax_witheld:
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open at left, flipped
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="Yes, the box 4 value is...", no_text="I didn’t have any withheld federal income tax in Box 4 of this 1099-INT"))
    i "\"Was any federal income tax withheld %(first_name)s? This would be listed in Box 4 of form 1099-INT?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Was any federal income tax withheld %(first_name)s? This would be listed in Box 4 of form 1099-INT?\""

    if screener_choice is True:
        hide screen choice_input
        jump scene_7_income_interest_input_income_tax_witheld
    elif screener_choice is False:
        $ int_1099_objects[int_1099_index].federal_income_tax_witheld = 0
        hide screen choice_input 
        jump scene_7_more_1099_ints_choice

label scene_7_income_interest_input_income_tax_witheld:
    show screen one_line_input(label_text="Tax Witheld", value_name=f"int_1099_objects[{int_1099_index}].federal_income_tax_witheld", placeholder_text="", changed_function=validate_and_save_dollar_active_field_array_property, value_type="arr_prop_float")
    i "\"How much federal income tax withheld %(first_name)s? This would be listed in Box 4 of form 1099-INT\""

    while get_error_message_by_id(f"int_1099_objects[{int_1099_index}].federal_income_tax_witheld") is not None or int_1099_objects[int_1099_index].federal_income_tax_witheld == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if int_1099_objects[int_1099_index].federal_income_tax_witheld == None:
            $ add_error(f"int_1099_objects[{int_1099_index}].federal_income_tax_witheld", "You must respond!")
        i "\"How much federal income tax withheld %(first_name)s? This would be listed in Box 4 of form 1099-INT\""

    hide screen one_line_input
    jump scene_7_more_1099_ints_choice

label scene_7_more_1099_ints_choice:
    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open at left
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=YES_OR_NO_CHOICES)
    i "\"Alright! Did you have another 1099-INT form, [first_name]? If not we should be all set here..\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Alright! Did you have another 1099-INT form, [first_name]? If not we should be all set here.\""

    if screener_choice is True:
        hide screen choice_input
        $ int_1099_index += 1
        jump scene_7_income_interest_input_payer_name
    elif screener_choice is False:
        hide screen choice_input 
        jump scene_7_interest_income_final_screener

label scene_7_interest_income_final_screener:
    $ renpy.dynamic("total_interest_income")
    $ total_interest_income = get_total_1099_int_box_1()
    if total_interest_income >= 2300 and age < 18:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_neutral mouth_talking at move_center_from_left
        i "\"That's a lot of interest income, [first_name].\""
        i "\"And at your age, too.\""
        if len(int_1099_objects) > 1:
            $ int_1099_objects.pop(int_1099_index)
            $ int_1099_index -= 1
            call screen game_over_modal(jump_back_to="scene_7_more_1099_ints_choice", message="T{i}Tax Heaven 3000{/i} does not currently support certain filers under age 24 with interest income over $2300")
        elif True:
            $ int_1099_objects.pop(int_1099_index)
            call screen game_over_modal(jump_back_to="scene_7_income_interest_input_payer_name", message="{i}Tax Heaven 3000{/i} does not currently support certain filers under age 24 with interest income over $2300")
    elif total_interest_income >= 2300 and age == 18:
        jump scene_7_interest_income_greater_than_2300_and_age_is_18_screener
    elif total_interest_income >= 2300 and age >= 19 and age < 24:
        jump scene_7_interest_income_greater_than_2300_and_age_between_19_24_screener
    elif True:
        jump scene_7_social_security_benefits

label scene_7_interest_income_greater_than_2300_and_age_is_18_screener:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_talking at left
    $ interest_income_earned_income_half_of_support = None
    show screen choice_input("interest_income_earned_income_half_of_support",choices=custom_yes_or_no_choices(has_what=True, what_text="What does \"total support\" mean?"))

    i "\"Was your earned income more than half your total support?\""
    while interest_income_earned_income_half_of_support == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("interest_income_earned_income_half_of_support", "You must respond!")
        i "\"Was your earned income more than half your total support?\""

    hide screen choice_input
    if interest_income_earned_income_half_of_support == True:
        show iris_upright pose8 brows_sad eyes_closed_happy mouth_smiling
        i "\"Okay, got it! You're very independent.\""
        $ aoc_refundable_earned_income_half_of_support = True
        jump scene_7_social_security_benefits
    elif interest_income_earned_income_half_of_support == False:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_neutral mouth_talking
        i "\"Umm…don’t take this the wrong way [first_name] but I’m getting a little intimidated\""
        i "\"I think this might be more complicated than I’m really looking for right now.\""
        $ aoc_refundable_earned_income_half_of_support = False
        call screen game_over_modal(jump_back_to="scene_7_interest_income_greater_than_2300_and_age_is_18_screener",message="{i}Tax Heaven 3000{/i} does not currently support certain filers under age 24 with interest income over $2300")
    elif True:
        show iris_upright pose11 brows_neutral eyes_neutral mouth_talking
        $ rollback_enabled = False
        i "\"Support includes the value of food, shelter, clothing, medical and dental care, education, and the like. To figure out your total support, count support provided by you, your parents, and others.\""
        $ rollback_enabled = True
        i "\"A scholarship received by you, however, isn't considered support if you were a full-time student.\""
        $ rollback_enabled = False
        hide iris_upright
        jump scene_7_interest_income_greater_than_2300_and_age_is_18_screener

label scene_7_interest_income_greater_than_2300_and_age_between_19_24_screener:
    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_closed_happy mouth_talking at left
    $ was_full_time_student_one_term = None
    show screen choice_input("was_full_time_student_one_term", choices=YES_OR_NO_CHOICES)

    i "\"Were you a full time student in [TAX_YEAR] for at least one academic term? I mean specifically full time with a full course load – half or part time doesn’t count.\""
    while was_full_time_student_one_term == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("was_full_time_student_one_term", "You must respond!")
        i "\"Were you a full time student in [TAX_YEAR] for at least one academic term? I mean specifically full time with a full course load – half or part time doesn’t count.\""

    hide screen choice_input
    if was_full_time_student_one_term == True:
        jump scene_7_interest_income_greater_than_2300_and_age_is_18_screener
    elif was_full_time_student_one_term == False:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open at flipped
        i "\"Okay, got it! Juggling school and real life at the same time is very impressive, [first_name].\""
        jump scene_7_social_security_benefits

label scene_7_social_security_benefits:
    $ has_social_security_benefits = None
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_wide_open mouth_talking at left
    show screen choice_input("has_social_security_benefits", choices=custom_yes_or_no_choices(yes_text="Yes, I did", no_text="No", has_what=True, what_text="Huh?"))
    i "\"Did you receive any social security benefits in 2022, [first_name]? You’d know if you received a Form SSA-1099\""

    while has_social_security_benefits == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_social_security_benefits", "You must respond!")
        i "\"Did you receive any social security benefits in 2022, [first_name]? You’d know if you received a Form SSA-1099\""

    hide screen choice_input
    if has_social_security_benefits is True:
        jump scene_7_input_social_security_benefits
    elif has_social_security_benefits is False:
        jump scene_7_has_unemployment_compensation
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_closed_happy mouth_talking at move_center_from_left
        $ rollback_enabled = False
        i "\"If you received social security benefits in [TAX_YEAR], the U.S. Social Security Administration will have issued you a form SSA-1099, which reports the total amount of benefits paid.\""
        $ rollback_enabled = True
        i "\"If you don’t have one of these forms, then you don’t need to worry about this.\""
        $ rollback_enabled = False
        hide screen choice_input
        jump scene_7_social_security_benefits

label scene_7_input_social_security_benefits:
    hide iris_bent
    show iris_upright pose9 brows_sad eyes_neutral mouth_wide_open at left, flipped
    show screen one_line_input(label_text="Taxable amount", value_name="social_security_taxable_amount", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"Okay! Let’s handle that form as well. Social welfare programs are amazing! What was the amount of those benefits? This information can be found in Box 5 of your form SSA-1099\""

    while get_error_message_by_id("social_security_taxable_amount") is not None or social_security_taxable_amount == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if social_security_taxable_amount == None:
            $ add_error("social_security_taxable_amount", "You must respond!")
        i "\"Okay! Let’s handle that form as well. Social welfare programs are amazing! What was the amount of those benefits? This information can be found in Box 5 of your form SSA-1099\""
    hide screen one_line_input
    jump scene_7_has_unemployment_compensation

label scene_7_has_unemployment_compensation:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_talking at left
    $ has_unemployment_compensation = None
    show screen choice_input("has_unemployment_compensation", choices=custom_yes_or_no_choices(yes_text="Oh yes, I did get one of those", no_text="No, I didn't"))
    i "\"One more thing – [first_name], in [TAX_YEAR], did you receive any unemployment compensation? That would be reported on a 1099-G form.\""

    while has_unemployment_compensation == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_unemployment_compensation", "You must respond!")
        i "\"One more thing – [first_name], in [TAX_YEAR], did you receive any unemployment compensation? That would be reported on a 1099-G form.\""

    hide screen choice_input
    if has_unemployment_compensation is True:
        jump scene_7_1099g_upload
    elif has_unemployment_compensation is False:
        jump scene_7_outro

label scene_7_1099g_upload:
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open at left, flipped
    show screen unemployment_1099g_upload_modal
    i "\"Let's make a copy of your Form 1099-G too!\""

    while unemployment_1099g_file_location is None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("unemployment_1099g_file_location", "You must upload a file!")
        i "\"Let's make a copy of your Form 1099-G too!\""

    hide screen unemployment_1099g_upload_modal
    jump scene_7_unemployment_compensation_input

label scene_7_unemployment_compensation_input:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open at move_center_from_left, flipped
    i "\"Great! Now let's make sure all the information is clear.\""
    show iris_upright pose9 brows_neutral eyes_neutral mouth_talking at move_left_from_center, flipped
    show screen one_line_input(label_text="Your compensation", value_name="unemployment_compensation", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"What was your total unemployment compensation in [TAX_YEAR]? That's listed in Box 1 of the 1099-G.\""

    while unemployment_compensation == None or get_error_message_by_id("unemployment_compensation") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if unemployment_compensation == None:
            $ add_error("unemployment_compensation", "You must upload a file!")
        i "\"What was your total unemployment compensation in [TAX_YEAR]? That's listed in Box 1 of the 1099-G.\""
    hide screen one_line_input
    jump scene_7_unemployment_compensation_tax_witheld_input

label scene_7_unemployment_compensation_tax_witheld_input:
    show screen one_line_input(label_text="Tax witheld", value_name="unemployment_compensation_tax_witheld", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"Okay that looks good. And then how much federal income tax was withheld from your unemployment? That should be in Box 4 of the form.\""

    while unemployment_compensation_tax_witheld == None or get_error_message_by_id("unemployment_compensation_tax_witheld") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if unemployment_compensation_tax_witheld == None:
            $ add_error("unemployment_compensation_tax_witheld", "You must upload a file!")
        i "\"Okay that looks good. And then how much federal income tax was withheld from your unemployment? That should be in Box 4 of the form.\""

    hide screen one_line_input
    jump scene_7_outro

label scene_7_outro:
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open at move_center_from_left
    i "\"Phew, all done! That was more copying than I expected.\""

    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling
    "Iris leans on my shoulder. It’s getting later in the day and the light in the office is starting to dim."

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush at flipped
    i "\"Thanks for coming with me today. I don’t really like being in places like this…but with you I feel a bit better.\""

    "I wonder what bad memories Iris has that this mundane corporate building is so off-putting."

    "\"Have you worked in an office before? Did something happen?\""

    hide iris_bent
    show iris_upright pose7 brows_sad eyes_neutral mouth_embarrassed
    i "\"No I didn’t work in one, I… well I just spent a lot of time in one.\""

    hide iris_upright
    show iris_bent pose3 brows_angry eyes_wide_open mouth_frowning more_blush
    i "\"Hey, promise me something. Don’t use corporate tax software, okay? \""

    "Huh? I guess I won’t this year because Iris said she’d help me out. And those kinds of software do always try to nickel and dime you to death."
    "Somehow Iris is making it sound more serious than that though."

    show iris_bent pose2 brows_sad eyes_closed_neutral mouth_smiling -more_blush
    "\"Okay, I promise.\""

    hide iris_bent
    show iris_upright pose8 brows_angry eyes_neutral mouth_wide_open
    i "\"Good.\""

    show iris_upright pose10 brows_neutral eyes_neutral mouth_smiling more_blush
    i "\"Sighh.. It’s nice being here like this with you [first_name], with no one else around.\""

    show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open -more_blush
    i "\"And I’m glad that I was able to help you with your tax forms a bit!\""
    $ add_book_to_iris_desk()
    jump scene_7_final_calculation

label scene_7_final_calculation:
    if cafe_visited:
        call pre_scene_8_interstitial ("office") from _call_pre_scene_8_interstitial_1
    elif True:
        window hide
        $ office_visited = True
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_6)
        $ update_completed_dates()
        $ calculate_return()
        $ purge_saves()
        jump generic_new_day
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
