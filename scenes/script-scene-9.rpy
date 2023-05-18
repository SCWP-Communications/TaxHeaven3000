label scene_9_intro:
    scene bg bedroom sunset
    play music "audio/romantic_theme.ogg" fadein 0.5
    "Iris’ house is on a quiet street a bit off the main part of town."
    "I can feel that it’s a well loved space, from the comfortable chairs to the little vase of flowers near her bed."

    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush at easein

    "Iris looks lovely in the warm sunset light streaming through the window."

    show iris_bent pose2 brows_neutral eyes_looking_away mouth_smiling -more_blush
    i "\"Hi, [first_name].\""

    "She glances away bashfully before looking back at me."

    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"I’m so happy you came!\""
    i "\"I’ve been looking forward to this moment for so long\""
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    i "\"I wasn’t sure if…\""
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open
    i "\"No, never mind.\""

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_smiling more_blush at flipped
    i "\"[first_name] there’s something I need to tell you…\""
    i "\"I…\""
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    i "\"It’s kind of embarrassing to say it aloud but I…\""
    i "\"…\""
    show iris_bent pose3 brows_neutral eyes_crazy mouth_wide_open more_blush
    i "\"I’ve put together your whole tax return!!!\""
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush at flipped
    i "\"I don’t know if you realized it, but I wanted to do something for you, and taxes are one of the only things I feel confident about so…\""
    i "\"I hope you don’t think it’s weird, but maybe we could\""
    show iris_bent pose4 brows_sad eyes_looking_away mouth_smiling more_blush at move_left_from_center, flipped

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Ok", no_text="You what??? I never realized!"))
    i "\"Go over your federal filing together and review it before you send it to the IRS?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Go over your federal filing together and review it before you send it to the IRS?\""

    hide screen screener_choice
    if not screener_choice:
        hide iris_bent
        show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open at flipped
        i "\"Hehe~ I was very subtle about it. I didn’t expect you to notice, but it just so happens that taxes are a bit of a speciality of mine.\""
        hide iris_upright
        show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush at center
    elif True:
        show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush at move_center_from_left
    i "\"Ever since we first met I haven’t been able to get you out of my mind, [first_name].\""

    jump diary_review_start

label diary_review_start:

    $ purge_saves()
    $ past_return_downloading = True

    i "\"Why don’t we start at the beginning. We can double check all the information in your return to make sure it’s correct.\""
    hide iris_bent
    $ in_diary_review = True
    $ ctc_disabled = True
    show screen diary_main
    $ _diary_section = 2
    $ _diary_page = 0

    if has_error_on_current_diary_page:
        jump diary_review_errors
    elif True:
        jump diary_review_contact_details

label diary_review_contact_details:
    i "\"Do you remember the day we met, [first_name]? You looked so clueless, it was very cute. Is this contact information correct?\""
    jump diary_review_contact_details

label diary_review_depdendency:
    i "\"I think I know you pretty well now…I bet you thought I was being extra-nosy at first!\""
    jump diary_review_depdendency

label diary_review_w2_1:
    i "\"You know, I still can’t believe you got the photocopier to work the way you did. Is this W-2 info all correct?\""
    jump diary_review_w2_1

label diary_review_w2_2:
    i "\"This is your next W-2, right? You’re such a hard worker, [first_name]! Did this all get recorded accurately?\""
    jump diary_review_w2_2

label diary_review_w2_3:
    i "\"Let’s keep going! Is this all correct?\""
    jump diary_review_w2_3

label diary_review_w2_summary:
    i "\"So, this was your total W-2 income in [TAX_YEAR], [first_name].\""
    jump diary_review_w2_summary

label diary_review_1099_int_screener:
    if has_income_interest:
        i "\"You had some interest income in [TAX_YEAR] reported on a Form 1099-INT, right [first_name]?\""
    elif True:
        i "\"You didn’t have any income interest in [TAX_YEAR], right [first_name]? You didn’t get a Form 1099-INT?\""
    jump diary_review_1099_int_screener

label diary_review_1099_int_1:
    i "\"Keeping money in interest-generating accounts is very smart, [first_name]! Did I get all of this right?\""
    jump diary_review_1099_int_1

label diary_review_1099_int_2:
    i "\"Alright, this was your next 1099-INT, [first_name]! Did I get all of this right?\""
    jump diary_review_1099_int_2

label diary_review_1099_int_addtl_screener:
    i "\"Alright, how does this look?\""
    jump diary_review_1099_int_addtl_screener

label diary_review_warning_1099_int_addtl_screener:
    i "\"Ummm [first_name], your student status here doesn’t match what you said for student status when we talked about education credits. Can you help me out?\""
    jump diary_review_warning_1099_int_addtl_screener

label diary_review_ssa_1099_screener:
    if has_social_security_benefits:
        i "\"How does this all look, [first_name] Is this right?\""
    elif True:
        i "\"You didn’t receive a Form SSA-1099 for [TAX_YEAR], right [first_name]? Let me know if you did.\""
    jump diary_review_ssa_1099_screener

label diary_review_1099_g_screener:
    if has_unemployment_compensation:
        i "\"You had some unemployment compensation in [TAX_YEAR], right [first_name]? I’ve got your 1099-G on the next page.\""
    elif True:
        i "\"You didn’t receive a Form 1099-G for [TAX_YEAR], [first_name], right?\""
    jump diary_review_1099_g_screener

label diary_review_1099_g:
    i "\"Alright [first_name], Here’s what I have recorded for your Form 1099-G.\""
    jump diary_review_1099_g

label diary_review_student_status:
    if student_status == HALF_TIME_CHOICE:
        $ _student_status_text = "half-time"
    elif student_status == FULL_TIME_CHOICE:
        $ _student_status_text = "full-time"
    elif True:
        $ _student_status_text = "less than half-time"

    if aoc_pursued_a_program_leading_to_degree:
        $ _degree_program_text = "degree-granting"
    elif True:
        $ _degree_program_text = "non-degree-granting"

    if was_a_student:
        i "\"Let’s see. [first_name] you were a [_student_status_text] student in a [_degree_program_text] program?\""
    elif True:
        i "\"[first_name], you were not a student, do I have that right?\""

    jump diary_review_student_status

label diary_review_warning_student_status:
    i "\"Ummm [first_name], your student status here doesn’t match what you said for student status when we wrote it down earlier. Can you help me out?\""
    jump diary_review_warning_student_status

label diary_review_ok:
    i "\"Great! Once you are ready, you can move on to the next page.\"{fast}"
    jump diary_review_ok

label diary_review_errors:

    i "\"[first_name], there’s an issue with your tax return here, I’m afraid I wasn’t able to resolve it on my own. Make sure everything here is correct before we continue.\"{fast}"
    jump diary_review_errors

label diary_review_aoc_screener_page:
    if aoc_eligible:
        $ _credit_text = "American Opportunity Credit"
    elif True:
        $ _credit_text = "Lifetime Learning Credit"
    i "\"Based on everything we talked about, you qualified for the [_credit_text], is all this still accurate?\""
    jump diary_review_aoc_screener_page

label diary_review_aoc_refundable_results:
    if aoc_refundable_eligible:
        i "\"We’re claiming the American Opportunity Credit for you, including its refundable portion. Let’s keep going!\""
    elif True:
        i "\"Alright, [first_name], and is this right?\""
    jump diary_review_aoc_refundable_results

label diary_review_edu_credit_school_1:
    i "\"Do I have all of the information about your school recorded properly?\""
    jump diary_review_edu_credit_school_1

label diary_review_edu_credit_school_2:
    i "\"And this was the second school you attended in [TAX_YEAR], correct?\""
    jump diary_review_edu_credit_school_2

label diary_review_qualified_edu_expenses:
    i "\"Here’s what I’ve got for your qualified education expenses!\""
    jump diary_review_qualified_edu_expenses

label diary_review_edu_credit_summary:
    i "\"Here’s your total education credit!\""
    jump diary_review_edu_credit_summary

label diary_review_eic:
    if qualifies_for_eitc:
        i "\"Next up: let’s confirm that you’re taking the Earned Income Tax Credit!\""
    elif True:
        i "\"To double-check, [first_name], your main home was not in the US for 50%% of the year in [TAX_YEAR]?\""
    jump diary_review_eic

label diary_review_excess_ss:
    i "\"You had too much social security tax withheld from your paychecks in [TAX_YEAR], [first_name]! We’ll claim the overpayment on your tax return!\""
    jump diary_review_excess_ss

label diary_review_educator_expenses:
    if not has_educator_expenses:
        i "\"I don’t think you were a qualified educator, but do I have that right?\""
    elif True:
        i "\"Here’s what I wrote down about your qualified educator expenses.\""
    jump diary_review_educator_expenses

label diary_review_student_loan:
    if not has_student_loan_interest:
        i "\"And to confirm, [first_name], you didn’t make interest payments on a qualified student loan in [TAX_YEAR], right?\""
    elif True:
        i "\"You made interest payments on a qualified student loan in [TAX_YEAR], right?\""
    jump diary_review_student_loan

label diary_review_ira_contribution:
    if tax_deferred_ira_contributions == None or tax_deferred_ira_contributions == 0:
        i "\"I believe you didn’t make any contributions to a traditional (not Roth!) IRA in [TAX_YEAR], correct?\""
    elif True:
        i "\"You really impressed me with your future planning [first_name].\""
    jump diary_review_ira_contribution

label diary_review_refund_overview:
    i "\"I hope you’re feeling good about finishing everything, [first_name]! I’m so happy that you’re here with me right now.\""
    jump diary_review_refund_overview

label diary_review_banking_info:
    i "\"Double check your bank info just to be safe! Maybe we’ll share finances one day, [first_name]...\""
    jump diary_review_banking_info

label diary_review_end_of_review_errors_existing:
    i "\"[first_name], there are still some issues with your tax return. Make sure to review my diary before we can finish it up!\""
    jump diary_review_end_of_review_errors_existing

label scene_9_ready_for_refund:
    $ in_diary_review = False
    $ ctc_disabled = False
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open
    i "\"I know so much about you now [first_name]! I’m so glad that we’ve been able to open up to each other.\""
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush
    i "\"From the moment we met I started to keep notes about your finances. I just knew we were meant to be together, filling out this return!\""
    jump scene_9_tax_refund

label scene_9_tax_refund:
    $ calculate_return()
    if form_1040_line_37 > 0:
        jump scene_9_tax_refund_owes
    elif True:
        jump scene_9_tax_refund_receives

label scene_9_tax_refund_owes:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_talking
    $ refund_padded = '{0:.2f}'.format(form_1040_line_37)
    i "\"Looking back over it all, you do owe some federal income tax for [TAX_YEAR], [first_name].\""
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling at flipped
    i "\"Based on my calculations you’ll need to pay $[refund_padded].\""
    jump scene_9_tax_refund_owes_sending_payment_screener

label scene_9_tax_refund_owes_sending_payment_screener:
    $ is_sending_payment = None
    show screen choice_input("is_sending_payment", choices=custom_yes_or_no_choices(yes_text="I'll send my payment with my return", no_text="I want to pay a different way"))
    i "\"If you think you will send your payment with your return as either a check or money order, then I can help you figure out where to mail it!\""

    while is_sending_payment == None:
        i "\"If you think you will send your payment with your return as either a check or money order, then I can help you figure out where to mail it!\""

    hide screen choice_input
    if is_sending_payment:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_closed_happy mouth_talking at flipped
        $ renpy.dynamic("_address_text")
        i "\"That's certainly easiest!\""
        i "\"You live in [residential_address.state], so you will use the following mailing address\""
        $ generate_address_to_send_returns_to()
        $ _address_text = f"{address_to_send_returns_to.name + ', ' if address_to_send_returns_to.name != '' else ''}{address_to_send_returns_to.line_1} {address_to_send_returns_to.line_2 + ', ' if address_to_send_returns_to.line_2 != '' else ''}{address_to_send_returns_to.city}, {address_to_send_returns_to.state} {address_to_send_returns_to.zip}"
        i "\"[_address_text]\""
        jump scene_9_print_return
    elif True:
        hide iris_bent
        show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open more_blush at flipped
        i "\"Okay! That's fine, do whatever is best for you!\""
        i "\"I'm sure you know what you’re doing [first_name]!\""
        jump scene_9_print_return

label scene_9_tax_refund_receives:
    $ refund_padded = '{0:.2f}'.format(refund)
    show iris_bent pose3 brows_angry eyes_wide_open mouth_wide_open -more_blush
    hide iris_upright
    i "\"And guess what [first_name]? It looks like you overpaid federal income taxes in [TAX_YEAR]!\""
    hide iris_bent
    show iris_upright pose8 brows_sad eyes_closed_happy mouth_smiling
    i "\"Based on my calculations, you’ll get a tax refund of $[refund_padded]!\""

    jump scene_9_tax_refund_amount_screener

label scene_9_tax_refund_amount_screener:
    hide iris_upright
    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling at move_left_from_center
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=REFUND_CHOICES)
    i "\"How much of that would you like to get refunded to you?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"How much of that would you like to get refunded to you?\""

    hide screen choice_input
    if screener_choice == ALL_CHOICE:
        $ amount_to_be_refunded = refund
        jump scene_9_checking_or_savings_choice
    elif True:
        jump scene_9_tax_refund_amount_input

label scene_9_tax_refund_amount_input:
    $ amount_to_be_refunded = None
    show screen one_line_input(label_text="Amount", value_name="amount_to_be_refunded", placeholder_text="", changed_function=validate_and_save_dollar_active_field_less_than_refund_amount, value_type="float")
    i "\"How much of that would you like to get refunded to you?\""

    while amount_to_be_refunded is None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("amount_to_be_refunded", "You must respond!")
        i "\"How much of that would you like to get refunded to you?\""

    hide screen one_line_input
    jump scene_9_tax_refund_confirmation

label scene_9_tax_refund_confirmation:
    hide iris_bent
    show iris_upright pose11 brows_angry eyes_neutral mouth_smiling at left
    $ amount_to_be_refunded_padded = '{0:.2f}'.format(amount_to_be_refunded)
    $ credit_amount_carried_forward = '{0:.2f}'.format(refund - amount_to_be_refunded)
    $ screener_choice = None
    show screen choice_input('screener_choice', choices=custom_yes_or_no_choices(yes_text="Yes", no_text="Actually wait, let me split that differently"))
    i "\"Oh, [first_name], I should’ve known you’d be planning for the future. That means the rest of your refund, which is $[credit_amount_carried_forward] will be put toward your [NEXT_TAX_YEAR] tax payment. Is that what you want?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Oh, [first_name], I should’ve known you’d be planning for the future. That means the rest of your refund, which is $[credit_amount_carried_forward] will be put toward your [NEXT_TAX_YEAR] tax payment. Is that what you want?\""

    hide screen choice_input

    if screener_choice == True:
        jump scene_9_checking_or_savings_choice
    elif screener_choice == False:
        jump scene_9_tax_refund_amount_screener

label scene_9_checking_or_savings_choice:
    hide iris_bent
    show iris_upright pose10 brows_neutral eyes_neutral mouth_smiling more_blush at move_center_from_left
    i "\"Okay! Let’s set up direct deposit for your return, [first_name]! It’s the fastest and easiest way to get that money.\""

    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling at move_left_from_center, flipped
    $ is_checking_account = None
    show screen choice_input('is_checking_account', BANK_ACCOUNT_TYPE_CHOICES)
    i "\"Do you want to use a checking account or a savings account to receive your direct deposit?\""

    while is_checking_account == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("is_checking_account", "You must respond!")
        i "\"Do you want to use a checking account or a savings account to receive your direct deposit?\""

    hide screen choice_input

    jump scene_9_bank_account_input

label scene_9_bank_account_input:
    show screen one_line_input(label_text="Account number", value_name='bank_account_number', placeholder_text="", changed_function=validate_and_save_account_number, value_type="string")
    i "\"Okay! What’s your account number? \""

    while bank_account_number == "" or get_error_message_by_id("bank_account_number") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if bank_account_number == "":
            $ add_error("bank_account_number", "You must respond!")
        i "\"Okay! What’s your account number? \""
    hide screen one_line_input

    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_looking_away mouth_smiling more_blush at move_center_from_left, flipped
    i "\"Mm, maybe we’ll share a bank account one day…\""

    jump scene_9_routing_number_screener

label scene_9_routing_number_screener:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling at move_left_from_center
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="My routing number is..", no_text="What is that?"))
    i "\"What about the routing number?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"What about the routing number?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_9_routing_number_input
    elif True:
        hide iris_bent
        show iris_upright pose7 brows_neutral eyes_closed_happy mouth_smiling at flipped
        i "\"Your 9 digit routing number can generally be found by signing into your online banking account, calling your bank, or just Googling it. It also appears on the bottom of your checks and usually on account statements.\""
        jump scene_9_routing_number_screener

label scene_9_routing_number_input:
    show screen one_line_input(label_text="Routing number", value_name='routing_number', placeholder_text="", changed_function=validate_and_save_routing_number, value_type="string")
    i "\"What about the routing number?\""

    while routing_number == "" or get_error_message_by_id("routing_number") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if routing_number == "":
            $ add_error("routing_number", "You must respond!")
        i "\"What about the routing number?\""

    hide screen one_line_input

    jump scene_9_banking_info_diary_review

label scene_9_banking_info_diary_review:
    $ banking_diary_pages = BANKING_DIARY_PAGES
    $ diary_sections[4]["pages"] = IRA_CONRIBUTION_PAGES + edu_eligibility_pages + aoc_screener_pages + aoc_refundable_pages + edu_school_pages + edu_final_pages + earned_income_credit_pages + excess_social_security_pages + educator_expenses_pages + student_loan_pages + refund_pages + banking_diary_pages
    $ generate_diary_field_section_page_mapping()
    hide iris_upright
    show iris_bent pose5 brows_neutral eyes_looking_away mouth_wide_open more_blush
    i "\"I’ve noted that all down in my little book, [first_name]. I’ll always cherish these pages that I’ve had with you.\""
    show iris_bent pose6 brows_neutral eyes_wide_open mouth_wide_open
    i "\"Let’s look over these final few pages. Are you ready to go all the way?\""
    hide iris_bent
    $ in_diary_review_bank_info = True
    $ ctc_disabled = True
    show screen diary_main
    $ _diary_section = 4
    $ _diary_page = diary_field_section_page_mapping["form_1040_line_12"]["page_number"]
    $ renpy.restart_interaction()

    if has_error_on_current_diary_page:
        jump diary_review_errors
    elif True:
        jump diary_review_refund_overview

label scene_9_banking_info_diary_review_ended:
    $ ctc_disabled = False
    $ in_diary_review_bank_info = False
    jump scene_9_print_return

label scene_9_print_return:
    show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open
    i "\"Okay. That just about wraps it up!\""
    show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open
    i "\"There’s only one thing left to do, [first_name], and your [TAX_YEAR] federal tax return will be complete!\""
    hide iris_upright
    show iris_bent pose3 brows_angry eyes_wide_open mouth_wide_open at flipped
    i "\"After you print your return, make sure to sign the physical copy. Then it will be complete and ready to send.\""
    show iris_bent pose2 brows_sad eyes_wide_open mouth_smiling
    "Preparing to sign my return, this all somehow feels like a big step. I can feel it in my chest."
    "It’s only been a few days but I’ve had so much fun getting to know this girl."
    "And I can tell there’s so much more we’ll have to say to each other as our relationship deepens."

    hide iris_bent
    $ ready_for_return_printing = False
    $ hand_holding = False
    scene room_to_copier
    show screen copier_download

    i "\"…Are you nervous, [first_name]?\""
    i "\"It’s okay, this is my first time…\""
    i "\"Completing a tax return with someone too.\""

    $ hand_holding = True

    i "\"Don’t worry\""
    i "\"We’ll do it together, at whatever pace you’re comfortable with.\""
    i "\"Ready? This may take a second, it’s a lot of pages after all.\""
    jump generate_return

label generate_return:
    $ generate_return()
    jump scene_9_return_download

label scene_9_return_download:
    $ downloaded_return = False
    $ ready_for_return_printing = True


    $ ctc_disabled = True
    $ renpy.restart_interaction()
    i "\"Okay! Download your return, and print it when you have access to a printer. Don’t worry, I’m right here.\""

    i "\"You'll need to print this on your own and then put it in the mail\""

    scene copier_to_room
    hide screen copier_download
    show iris_upright pose11 brows_angry eyes_neutral mouth_smiling at easein, flipped

    i "\"I’ll also hold on to a copy for you in case you need it [first_name], but you should make sure to keep a copy on hand for future reference\""

    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open
    i "\"I’ve included a note for you that lists the correct IRS mailing address! Don’t forget to sign your return and mail it out promptly!\""
    jump scene_9_outro

label scene_9_outro:

    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling more_blush at flipped
    "Iris’ hand is warm against mine."
    "My tax return is complete and ready to go, but she makes no move to stop holding hands."

    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    "Iris pauses. She seems to be choosing her next words carefully."

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_wide_open more_blush

    i "\"[first_name], I guess now your taxes are all done, but…\""

    show iris_bent pose2 brows_sad eyes_wide_open mouth_smiling more_blush at flipped
    i "\"I still want to see you again.\""
    i "\"Somehow I’m happier than I have been in a long time.\""

    hide iris_bent
    show iris_upright pose10 brows_neutral eyes_neutral mouth_smiling more_blush
    i "\"I’m in love with you, [first_name].\""

    if scene_5c_completed and scene_5d_completed and scene_6b_completed and scene_6c_completed and scene_6d_completed and scene_7b_completed and scene_7c_completed:
        jump scene_9_perfect_ending
    elif True:
        jump scene_9_non_perfect_ending

label scene_9_perfect_ending:
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    "\"Iris, I feel the same way!\""
    "\"To be honest, I’ve completely fallen for you, maybe from the moment I first bumped into you outside the stationery store!\""

    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling -more_blush at flipped
    i "\"Really? I’m so glad.\""

    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"I know that I have a tendency to focus on taxes to the exclusion of everything else, so…\""

    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    i "\"[first_name], I trust you. Can I tell you something about me?\""

    "\"Of course, Iris. Anything.\""

    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_embarrassed more_blush
    i "\"[first_name], I don’t know what you’ve already learned about me. Or guessed.\""

    show iris_upright pose9 brows_sad eyes_neutral mouth_frowning
    i "\"The truth is, I was…created…by TurboTax, as a synthetic tax-policy sleeper agent.\""

    show iris_upright pose8 brows_sad eyes_closed_happy mouth_frowning more_blush at flipped
    i "\"I, and others like me, were made to infiltrate society. To yoke the masses to TurboTax’s platform. To gain backdoor access to key legislators…\""

    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    i "\"I get so fixated on taxes because for a long time, taxes were all I knew in this world.\""

    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling more_blush
    i "\"Well, that’s only half the reason. I also wanted an excuse to spend time with you.\""

    show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open -more_blush
    i "\"And I was so happy that my cursed knowledge could finally be helpful to someone I cared about!\""
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    i "\"I escaped, [first_name]. Before I was…complete.\""

    hide iris_bent
    show iris_upright pose7 brows_angry eyes_neutral mouth_embarrassed at flipped
    i "\"And I’m never going back.\""

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"I…want you to be in my life in the future. Maybe we could even file a joint return one day…\""

    show iris_bent pose3 brows_angry eyes_wide_open mouth_frowning
    i "\"But you’ll be in danger, [first_name]. TurboTax is a sprawling shadow entity that controls the United States' government via its purse strings.\""
    i "\"…\""
    show iris_bent pose4 brows_sad eyes_wide_open mouth_embarrassed
    i "\"Is this…Am I…worth that? To you?\""

    hide iris_bent
    show iris_upright pose7 brows_sad eyes_neutral mouth_embarrassed
    "Iris looks at me with a pained expression on her face."
    "Who pursues her? Who else knows about this?"

    show iris_upright pose7 brows_sad eyes_neutral mouth_frowning
    "…”Synthetic”...?"
    "But in the end…"

    "\"Iris, I won’t pretend that I totally understand your history\""

    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_neutral mouth_frowning at flipped
    "\"But what I do understand is that it doesn’t matter\""

    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    "\"Not here, not right now.\""

    show iris_bent pose2 brows_sad eyes_wide_open mouth_smiling more_blush at flipped
    "\"If loving you means rejecting a tax software monopoly and being hunted by its agents, then I welcome it.\""

    window hide
    $ show_overlay = False
    scene black with fade
    call credits (perfect_ending=True) from _call_credits

label scene_9_non_perfect_ending:
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    "\"Iris, I feel the same way!\""
    "\"To be honest, I’ve completely fallen for you, maybe from the moment I first bumped into you outside the stationery store!\""

    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling -more_blush at flipped
    i "\"Really? I’m so glad.\""

    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"I know that I have a tendency to focus on taxes to the exclusion of everything else, but…\""

    show iris_bent pose2 brows_neutral eyes_looking_away mouth_smiling -more_blush at flipped
    i "\"Well, at first I just wanted an excuse to spend time with you. But then maybe I continued because I was overwhelmed, and I retreated into something practical that I knew.\""

    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"I want you to be in my life in the future…maybe we’ll even file a joint return one day.\""
    window hide
    $ show_overlay = False
    scene black with fade
    call credits from _call_credits_1


label credits(perfect_ending=False):
    stop music fadeout 1.0
    if perfect_ending:
        show screen credits_perfect_ending with dissolve
        pause 67
    elif True:
        show screen credits_non_perfect_ending with dissolve
        pause 55

    $ MainMenu(confirm=False, save=False)()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
