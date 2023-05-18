label scene_8_intro:
    window hide
    scene bg library
    play music "audio/main_theme.ogg" fadein 0.5
    jump scene_8_screener

label scene_8_screener:
    "I’m getting a little bit of deja vu trying to meet Iris at the library again…"
    "Still, she said she’d make sure to be here this time."
    "Glancing over at her desk I see the familiar little notebook…"

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Talk to Iris", no_text="I kind of want to peek at her diary. Wait for her to get up?"), variant="narrator")
    "And also Iris sitting there! I think that’s the first time she’s been at her desk."

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "And also Iris sitting there! I think that’s the first time she’s been at her desk."

    hide screen screener_choice
    if screener_choice:
        jump scene_8_pre_date
    elif True:
        jump scene_8_pre_diary

label scene_8_pre_diary:
    "I’ll hang back for a second. Maybe she’ll need to go re-shelve some books? I don’t really know what people do in libraries."
    "..."
    "Aha! There we go. She’s getting up."

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Edit Iris' notebook", no_text="Nevermind. Go talk to Iris"), variant="narrator")
    "This is my chance to peek at her notebook."

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "This is my chance to peek at her notebook."

    hide screen screener_choice
    if screener_choice:
        jump scene_5_diary
    elif True:
        "\"Iris, wait up!\""
        jump scene_8_pre_date

label scene_8_diary_segue:
    "..."
    "..."

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Talk to Iris", no_text="Wait, I actually want to look at her diary again. Wait for her to get up one more time?"), variant="narrator")
    "Aha! She’s coming back. Perfect."

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Aha! She’s coming back. Perfect."

    hide screen screener_choice

    if screener_choice:
        jump scene_8_pre_date
    elif True:
        jump scene_5_diary

label scene_8_pre_date:
    "\"Hi Iris! Looks like I was able to catch you this time.\""

    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open at easein_fast
    i "\"Oh, hello [first_name]. Yes, I’ve been waiting for you.\""

    show iris_bent pose4 brows_sad eyes_looking_away mouth_wide_open more_blush at flipped
    i "\"I said I wanted to do something for you as thanks for keeping me company the other day.\""
    i "\"Well…\""

    show iris_bent pose2 brows_sad eyes_wide_open mouth_smiling
    "Iris glances around and leans in. We’re secluded behind bookshelves. It’s very warm in the library."

label scene_8_pre_aoc:
    if form_1040_line_11 >= 90000 or someone_can_claim_as_dependent:
        $ claiming_aoc = False
        $ claiming_lllc = False
        $ aoc_refundable_eligible = False
        $ aoc_schools = []
        jump scene_8_eic
    elif True:
        hide iris_bent
        show iris_upright pose10 brows_angry eyes_crazy mouth_wide_open more_blush
        i "\"Why don’t we see if you qualify for any tax credits?\""
        show iris_upright pose7 brows_neutral eyes_neutral mouth_smiling -more_blush
        "\"Well, I, uh..\""
        "\"…sure, Iris, I’d love to look into tax credits with you. \""
        show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open
        i "\"Don’t worry, [first_name], I’ll guide you through it. Plus I get to learn more about you as we go! I’m looking forward to getting even closer~\""

        hide iris_upright
        show iris_bent pose4 brows_neutral eyes_looking_away mouth_smiling more_blush at flipped
        i "\"I think you’re pretty smart [first_name]. I’d love to learn more about your educational background.\""

        jump scene_8_aoc_student_screener_branching

label scene_8_aoc_student_screener_branching:
    if was_full_time_student_one_term:
        $ was_a_student = True
        i "\"[first_name], I remember you said you were a full time student. I think intellectual compatibility is really important in a relatio– ummm I mean, friendship!\""
        jump scene_8_already_full_time_student
    elif was_full_time_student_one_term == False:
        i "\"I think intellectual compatibility is really important in a relatio– ummm I mean, friendship!\""
        jump scene_8_aoc_was_not_full_time_student_screener
    elif True:
        i "\"I think intellectual compatibility is really important in a relatio– ummm I mean, friendship!\""
        jump scene_8_aoc_student_screener

label scene_8_already_full_time_student:
    $ school_number_being_entered = 0
    $ screener_choice = None
    hide iris_bent
    show iris_upright pose8 brows_angry eyes_neutral mouth_wide_open at left
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(has_what=True, what_text="What counts as \"qualified\" here?"))
    i "\"In %(TAX_YEAR)s, did you pay tuition or other qualified expenses for an academic period beginning in %(TAX_YEAR)s, or beginning in the first three months of %(NEXT_TAX_YEAR)s?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"In %(TAX_YEAR)s, did you pay tuition or other qualified expenses for an academic period beginning in %(TAX_YEAR)s, or beginning in the first three months of %(NEXT_TAX_YEAR)s?\""
    hide screen choice_input
    if screener_choice == True:
        $ paid_tuition_or_qualified_expenses = True
        jump scene_8_aoc_find_out_if_eligible
    elif screener_choice == False:
        $ paid_tuition_or_qualified_expenses = False
        jump scene_8_eic
    elif True:
        show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open at flipped, move_center_from_left
        i "\"Qualified education expenses are tuition and certain related expenses required for enrollment or attendance.\""
        show iris_upright pose8 brows_angry eyes_squinted mouth_wide_open at move_left_from_center
        jump scene_8_already_full_time_student

label scene_8_aoc_was_not_full_time_student_screener:
    $ screener_choice = None
    $ school_number_being_entered = 0
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open -more_blush at move_left_from_center

    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="I was a student enrolled less than half-time", no_text="I was a student enrolled half-time", has_what=True, what_text=f"I was a not a a student in {TAX_YEAR}"))
    i "\"[first_name], you previously said you were not a full time student. I just wanted to check - were you a student enrolled half time or less than half time in [TAX_YEAR]?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"[first_name], you previously said you were not a full time student. I just wanted to check - were you a student enrolled half time or less than half time in [TAX_YEAR]?\""


    hide screen choice_input
    if screener_choice == True and not someone_can_claim_as_dependent:
        $ was_a_student = True
        $ student_status = LESS_THAN_HALF_CHOICE
        jump scene_8_lllc_intro
    elif screener_choice == False and not someone_can_claim_as_dependent:
        $ was_a_student = True
        $ student_status = HALF_TIME_CHOICE
        jump scene_8_aoc_tuition_screener
    elif True:
        $ was_a_student = False
        $ paid_tuition_or_qualified_expenses = False
        jump scene_8_eic

label scene_8_aoc_student_screener:
    $ screener_choice = None
    $ school_number_being_entered = 0
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open -more_blush at move_left_from_center

    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="I was a student!", no_text="No", has_what=True, what_text="What counts as \"qualified\" here?"))
    i "\"%(first_name)s, were you a student enrolled at a qualified educational institution at %(TAX_YEAR)s?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"%(first_name)s, were you a student enrolled at a qualified educational institution at %(TAX_YEAR)s?\""


    hide screen choice_input
    if screener_choice == True and not someone_can_claim_as_dependent:
        $ was_a_student = True
        jump scene_8_aoc_tuition_screener
    elif screener_choice == False:
        $ was_a_student = False
        $ paid_tuition_or_qualified_expenses = False
        jump scene_8_eic
    elif True:
        show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at flipped, move_center_from_left
        $ rollback_enabled = False
        i "\"An eligible educational institution is generally any accredited public, nonprofit, or private college, university, vocational school, or other postsecondary institution.\""
        $ rollback_enabled = True
        i "\"Also, the institution must be eligible to participate in a student aid program run by the U.S. Department of Education.\""
        $ rollback_enabled = False
        jump scene_8_aoc_student_screener

label scene_8_aoc_tuition_screener:
    $ screener_choice = None
    show iris_upright pose8 brows_angry eyes_neutral mouth_wide_open at left
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(has_what=True, what_text="What counts as \"qualified\" here?"))
    i "\"Awesome! In %(TAX_YEAR)s, did you pay tuition or other qualified expenses for an academic period beginning in %(TAX_YEAR)s, or beginning in the first three months of %(NEXT_TAX_YEAR)s?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Awesome! In %(TAX_YEAR)s, did you pay tuition or other qualified expenses for an academic period beginning in %(TAX_YEAR)s, or beginning in the first three months of %(NEXT_TAX_YEAR)s?\""
    hide screen choice_input
    if screener_choice == True:
        $ paid_tuition_or_qualified_expenses = True
        jump scene_8_aoc_find_out_if_eligible
    elif screener_choice == False:
        $ paid_tuition_or_qualified_expenses = False
        jump scene_8_eic
    elif True:
        show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open at flipped, move_center_from_left
        i "\"Qualified education expenses are tuition and certain related expenses required for enrollment or attendance.\""
        show iris_upright pose8 brows_angry eyes_squinted mouth_wide_open at move_left_from_center
        jump scene_8_aoc_tuition_screener

label scene_8_aoc_find_out_if_eligible:
    $ screener_choice = None
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open at left, flipped

    show screen choice_input("screener_choice", choices=ELIGIBILITY_CHOICES)
    i "\"Ooh really, [first_name]? That’s great! In that case, maybe you qualify for the American Opportunity Credit or the Lifetime Learning Credit! Why don’t we find out?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Ooh really, [first_name]? That’s great! In that case, maybe you qualify for the American Opportunity Credit or the Lifetime Learning Credit! Why don’t we find out?\""

    hide screen choice_input
    if screener_choice == True:
        jump scene_8_aoc_pursuing_a_degree_screener
    elif screener_choice == False:
        jump scene_8_eic
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_wink mouth_wide_open at move_center_from_left
        i "\"I'm glad you asked [first_name]! The American Opportunity Credit and the Lifetime Learning Credit are tax credits that help with the cost of higher education. Certain criteria have to be met in order to qualify for these credits.\""
        jump scene_8_aoc_find_out_if_eligible

label scene_8_aoc_pursuing_a_degree_screener:
    hide iris_upright
    show iris_bent pose2 brows_neutral eyes_wide_open mouth_talking -more_blush at left
    $ aoc_pursued_a_program_leading_to_degree = None
    show screen choice_input("aoc_pursued_a_program_leading_to_degree", choices=custom_yes_or_no_choices(yes_text="Yes", no_text="No, I was not working towards a degree or other recognized credential"))
    i "\"Were you pursuing a program leading to a degree or other recognized education credential, %(first_name)s?\""

    while aoc_pursued_a_program_leading_to_degree == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_pursued_a_program_leading_to_degree", "You must respond!")
        i "\"Were you pursuing a program leading to a degree or other recognized education credential, %(first_name)s?\""

    hide screen choice_input
    if aoc_pursued_a_program_leading_to_degree:
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush at left
        i "\"You must be a serious student, [first_name]\""
        if student_status == None:
            jump scene_8_aoc_attendance_status_screener
        elif True:
            jump scene_8_aoc_first_four_years_completed_before_this_year
    elif True:
        jump scene_8_lllc_intro

label scene_8_aoc_attendance_status_screener:
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=ATTENDANCE_STATUS_CHOICES)
    i "\"In %(TAX_YEAR)s, what was your attendance status for at least one academic period?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"In %(TAX_YEAR)s, what was your attendance status for at least one academic period?\""

    hide screen choice_input
    if screener_choice == LESS_THAN_HALF_CHOICE:
        $ student_status = LESS_THAN_HALF_CHOICE

        jump scene_8_lllc_intro
    elif screener_choice == HALF_TIME_CHOICE:
        $ student_status = HALF_TIME_CHOICE
        jump scene_8_aoc_first_four_years_completed_before_this_year
    elif True:
        $ student_status = FULL_TIME_CHOICE
        jump scene_8_aoc_first_four_years_completed_before_this_year

label scene_8_aoc_first_four_years_completed_before_this_year:
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open more_blush at left
    show screen choice_input("aoc_first_four_years_completed_before_this_year", choices=YES_OR_NO_CHOICES)
    i "\"You seem really smart, [first_name]. Did you complete the first 4 years of your post-secondary education prior to 2022?\""

    while aoc_first_four_years_completed_before_this_year == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_first_four_years_completed_before_this_year", "You must respond!")
        i "\"You seem really smart, [first_name]. Did you complete the first 4 years of your post-secondary education prior to 2022?\""

    hide screen choice_input
    if aoc_first_four_years_completed_before_this_year:
        jump scene_8_lllc_intro
    elif True:
        i "\"I see! It's really impressive that you're pursuing a degree now!\""
        jump scene_8_aoc_claimed_last_four_years

label scene_8_aoc_claimed_last_four_years:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_talking -more_blush at left
    $ aoc_claimed_last_four_years = None
    show screen choice_input("aoc_claimed_last_four_years", choices=custom_yes_or_no_choices(yes_text="I have claimed the American Opportunity Credit 4 times", no_text="I have {b}not{/b} claimed the American Opportunity Credit 4 times", has_what=True, what_text="How would I know if I've done that?"))
    i "\"[first_name], have you claimed the American Opportunity Credit in the past? If you've already claimed it 4 times, you can't claim it again.\""

    while aoc_claimed_last_four_years == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_claimed_last_four_years", "You must respond!")
        i "\"[first_name], have you claimed the American Opportunity Credit in the past? If you've already claimed it 4 times, you can't claim it again.\""

    hide screen choice_input
    if aoc_claimed_last_four_years == True:
        jump scene_8_lllc_intro
    elif aoc_claimed_last_four_years == False:
        hide iris_upright
        show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed more_blush at left, flipped
        i "\"Okay [first_name], this next question might sound like a weird one.\""
        i "\"I’ve never experimented with drugs much myself but…I wouldn’t mind experimenting a little if you wanted to.\""
        jump scene_8_aoc_has_been_convicted
    elif True:
        show iris_upright pose11 brows_neutral eyes_neutral mouth_smiling
        $ rollback_enabled = False
        i "\"If you think you might have claimed this credit before [first_name], or are unsure how many times you may have claimed it, you should check your prior year's tax returns.\""
        $ rollback_enabled = True
        i "\"If you claimed the credit on any of those returns, you would see it listed on Form 8863.\""
        i "\"That said [first_name], if you parents claimed you as a dependent during any of those years, the American Opportunity Credit would be reflected on their tax returns, not yours.\""
        $ rollback_enabled = False
        jump scene_8_aoc_claimed_last_four_years

label scene_8_aoc_has_been_convicted:
    show screen choice_input("aoc_has_been_convicted", choices=YES_OR_NO_CHOICES)
    i "\"At the end of [TAX_YEAR], had you been convicted of a felony for possession or distribution of a controlled substance?\""

    while aoc_has_been_convicted == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_has_been_convicted", "You must respond!")
        i "\"At the end of [TAX_YEAR], had you been convicted of a felony for possession or distribution of a controlled substance?\""

    hide screen choice_input
    if aoc_has_been_convicted:
        jump scene_8_lllc_intro
    elif True:
        hide iris_upright
        show iris_bent pose2 brows_neutral eyes_looking_away mouth_smiling -more_blush at flipped
        i "\"Haha, well, me neither [first_name]!\""
        hide iris_bent
        show iris_upright pose7 brows_neutral eyes_neutral mouth_smiling -more_blush at flipped
        i "\"I feel like I’ve gotten to know you so much better today.\""

        $ claiming_aoc = True
        $ aoc_eligible = True
        $ claiming_lllc = False
        jump scene_8_aoc_school_entry

label scene_8_lllc_intro:
    $ aoc_eligible = False
    $ claiming_aoc = False
    $ claiming_lllc = True
    i "\"I feel like I've gotten to know you so much better today.\""
    hide iris_bent
    show iris_upright pose10 brows_angry eyes_crazy mouth_wide_open more_blush at flipped
    i "\"It looks like you are eligible to claim the Lifetime Learning Credit, %(first_name)s!\""
    jump scene_8_aoc_school_entry

label scene_8_aoc_school_entry:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_smiling -more_blush at move_left_from_center, flipped
    $ aoc_schools.append(School())
    show screen one_line_input(label_text="Your school", value_name=f"aoc_schools[{school_number_being_entered}].name", placeholder_text="", changed_function=validate_and_save_active_input_required_array_property, value_type="arr_prop_string")
    if school_number_being_entered == 0:
        i "\"Where did you attend school in %(TAX_YEAR)s %(first_name)s? If you attended more than one school, just start with one of them.\""
        while aoc_schools[school_number_being_entered].name == "":
            play sound "audio/error_beep.ogg" volume 0.3
            $ add_error(f"aoc_schools[{school_number_being_entered}].name", "You must respond!")
            i "\"Where did you attend school in %(TAX_YEAR)s %(first_name)s? If you attended more than one school, just start with one of them.\""
    elif True:
        i "\"All right, tell me about the next one! What was the name of your second school?\""
        while aoc_schools[school_number_being_entered].name == "":
            play sound "audio/error_beep.ogg" volume 0.3
            $ add_error(f"aoc_schools[{school_number_being_entered}].name", "You must respond!")
            i "\"All right, tell me about the next one! What was the name of your second school?\""

    hide screen one_line_input
    jump scene_8_aoc_school_address

label scene_8_aoc_school_entry_start_over:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_smiling at left, flipped
    $ aoc_schools[0] = School()
    show screen one_line_input(label_text="Your school", value_name=f"aoc_schools[0].name", placeholder_text="", changed_function=validate_and_save_active_input_required_array_property, value_type="arr_prop_string")
    i "\"Okay! Tell me about that school first, okay? What was the name of the school that did issue you a 1098-T?\""
    while aoc_schools[0].name == "":
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_schools[0].name", "You must respond!")
        i "\"Okay! Tell me about that school first, okay? What was the name of the school that did issue you a 1098-T?\""

    hide screen one_line_input
    jump scene_8_aoc_school_address

label scene_8_aoc_school_address:
    $ renpy.dynamic("_current_school_name", "_current_school_state")
    $ _current_school_name = aoc_schools[school_number_being_entered].name

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_wide_open more_blush at left, flipped
    if school_number_being_entered == 0:
        show screen multi_line_input(SCHOOL_0_ADDRESS_VALUES)
        i "\"You went to [_current_school_name]? That's great! What is that institution's full address?\""

        while aoc_schools[school_number_being_entered].line_1 == "" or  aoc_schools[school_number_being_entered].city == "" or  aoc_schools[school_number_being_entered].state == "" or  aoc_schools[school_number_being_entered].zip == "" or get_error_message_by_id(f"aoc_schools[{school_number_being_entered}].state") is not None or get_error_message_by_id(f"aoc_schools[{school_number_being_entered}].zip") is not None:
            play sound "audio/error_beep.ogg" volume 0.3
            if aoc_schools[school_number_being_entered].line_1 == "" and aoc_schools[school_number_being_entered].city == "" and aoc_schools[school_number_being_entered].state == "" and aoc_schools[school_number_being_entered].zip == "":
                $ add_error(f"aoc_schools[{school_number_being_entered}].line_1", "You must respond!")
                $ add_error(f"aoc_schools[{school_number_being_entered}].city", "You must respond!")
                $ add_error(f"aoc_schools[{school_number_being_entered}].state", "You must respond!")
                $ add_error(f"aoc_schools[{school_number_being_entered}].zip", "You must respond!")
            i "\"You went to [_current_school_name]? That's great! What is that institution's full address?\""
    elif True:
        show screen multi_line_input(SCHOOL_1_ADDRESS_VALUES)
        i "\"You went to [_current_school_name]? That's great! What is that institution's full address?\""

        while aoc_schools[school_number_being_entered].line_1 == "" or  aoc_schools[school_number_being_entered].city == "" or  aoc_schools[school_number_being_entered].state == "" or  aoc_schools[school_number_being_entered].zip == "" or get_error_message_by_id(f"aoc_schools[{school_number_being_entered}].state") is not None or get_error_message_by_id(f"aoc_schools[{school_number_being_entered}].zip") is not None:
            play sound "audio/error_beep.ogg" volume 0.3
            if aoc_schools[school_number_being_entered].line_1 == "" and aoc_schools[school_number_being_entered].city == "" and aoc_schools[school_number_being_entered].state == "" and aoc_schools[school_number_being_entered].zip == "":
                $ add_error(f"aoc_schools[{school_number_being_entered}].line_1", "You must respond!")
                $ add_error(f"aoc_schools[{school_number_being_entered}].city", "You must respond!")
                $ add_error(f"aoc_schools[{school_number_being_entered}].state", "You must respond!")
                $ add_error(f"aoc_schools[{school_number_being_entered}].zip", "You must respond!")
            i "\"You went to [_current_school_name]? That's great! What is that institution's full address?\""

    hide screen multi_line_input
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush at move_center_from_left
    $ _current_school_state = aoc_schools[school_number_being_entered].state
    i "\"[_current_school_state] huh? I've never been, maybe I'll visit someday.\""

    jump scene_8_aoc_1098t

label scene_8_aoc_1098t:
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush at move_left_from_center
    $ aoc_schools[school_number_being_entered].did_receive_1098t_this_year = None
    show screen choice_input(f"aoc_schools[{school_number_being_entered}].did_receive_1098t_this_year", choices=custom_yes_or_no_choices(yes_text="Oh, yeah, I did get one of those", no_text="No, I didn't get one", has_what=True, what_text="What is that form?"), value_type="arr_prop_bool")
    i "\"By the way, did you receive a form 1098-T from [_current_school_name] for [TAX_YEAR]?\""

    while aoc_schools[school_number_being_entered].did_receive_1098t_this_year == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error(f"aoc_schools[{school_number_being_entered}].did_receive_1098t_this_year", "You must respond!")
        i "\"By the way, did you receive a form 1098-T from [_current_school_name] for [TAX_YEAR]?\""

    hide screen choice_input

    if aoc_schools[school_number_being_entered].did_receive_1098t_this_year == "what":
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open -more_blush at move_center_from_left
        $ rollback_enabled = False
        i "\"A form 1098-T is a statement that colleges and universities are required to issue to certain students.\""
        $ rollback_enabled = True
        i "\"The form lists the total dollar amount paid by the student for qualified tuition and related expenses in a single tax year.\""
        $ rollback_enabled = False
        jump scene_8_aoc_1098t
    elif aoc_schools[school_number_being_entered].did_receive_1098t_this_year == False:
        if claiming_aoc and school_number_being_entered == 0:

            hide iris_bent
            show iris_upright pose11 brows_sad eyes_looking_away mouth_embarrassed -more_blush at left, flipped
            $ screener_choice = None
            show screen screener_choice(choices=custom_yes_or_no_choices(yes_text=f"Actually yes! I did attend a second school that did give me a Form 1098-T for {TAX_YEAR}", no_text=f"No, I didn't get any Forms 1098-T in {TAX_YEAR}"))
            i "\"I see. It's not 100%% essential, but before we move forward [first_name], did you attend a second eligible school in 2022 that DID issue a 1098-T? If so, we should do that school first\""
            while screener_choice == None:
                i "\"I see. It's not 100%% essential, but before we move forward [first_name], did you attend a second eligible school in 2022 that DID issue a 1098-T? If so, we should do that school first\""
            hide screen screener_choice
            if screener_choice:
                jump scene_8_aoc_school_entry_start_over
            elif True:
                show iris_upright pose8 brows_sad eyes_closed_happy mouth_smiling at flipped
                i "\"Alright [first_name] no worries, it's not 100%% essential!\""
        elif True:
            i "\"That's okay, it's not 100%% essential\""

    jump scene_8_aoc_1098t_previous_year

label scene_8_aoc_1098t_previous_year:
    $ aoc_schools[school_number_being_entered].did_receive_1098t_previous_year_box_7 = None
    show screen choice_input(f"aoc_schools[{school_number_being_entered}].did_receive_1098t_previous_year_box_7", choices=custom_yes_or_no_choices(yes_text=f"I did get a 1098-T for {PREVIOUS_TAX_YEAR} with Box 7 checked", no_text="Nope"), value_type="arr_prop_bool")
    i "\"What about for [PREVIOUS_TAX_YEAR], [first_name], did you receive a form 1098-T from [_current_school_name] for [PREVIOUS_TAX_YEAR], and if so, was Box 7 checked on it?\""
    while aoc_schools[school_number_being_entered].did_receive_1098t_previous_year_box_7 == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error(f"aoc_schools[{school_number_being_entered}].did_receive_1098t_previous_year_box_7", "You must respond!")
        i "\"What about for [PREVIOUS_TAX_YEAR], [first_name], did you receive a form 1098-T from [_current_school_name] for [PREVIOUS_TAX_YEAR], and if so, was Box 7 checked on it?\""

    hide screen choice_input
    jump scene_8_aoc_ein_screener

label scene_8_aoc_ein_screener:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_talking at left
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="I attended an educational institution that doesn't have an EIN", no_text="My school's EIN was..."))
    i "\"Okay, %(first_name)s, last piece of information about [_current_school_name] - what is its employer identification number (EIN)? That’s normally printed on a form 1098-T, but you should also be able to look it up or ask your school.\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Okay, %(first_name)s, last piece of information about [_current_school_name] - what is its employer identification number (EIN)? That’s normally printed on a form 1098-T, but you should also be able to look it up or ask your school.\""

    hide screen choice_input
    if screener_choice and (claiming_lllc or (claiming_aoc and school_number_being_entered == 0)):
        $ claiming_aoc = False
        $ claiming_lllc = True
        $ aoc_eligible = False
        i "\"We can skip it if you're sure your school doesn't have one.\""

        if school_number_being_entered == 0:
            jump scene_8_aoc_second_school_screener
        elif True:
            if claiming_aoc:
                jump scene_8_aoc_age_eligibility
            elif True:
                jump scene_8_lllc_eligible_expenses_screener

    elif screener_choice and (claiming_aoc and school_number_being_entered == 1):
        jump scene_8_aoc_ein_second_school_no_ein_are_you_sure
    elif True:
        jump scene_8_aoc_ein

label scene_8_aoc_ein_second_school_no_ein_are_you_sure:
    hide iris_bent
    show iris_upright pose7 brows_angry eyes_crazy mouth_talking more_blush at left, flipped
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="I found it! My school\'s EIN was...", no_text="It really doesn\'t  have one, guess I can\'t count it"))
    i "\"Hmmm, %(first_name)s, to claim the American Opportunity Credit, you must provide the educational institution's EIN. Are you sure you don't have this info?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Hmmm, %(first_name)s, to claim the American Opportunity Credit, you must provide the educational institution's EIN. Are you sure you don't have this info?\""

    hide screen choice_input
    if screener_choice:
        jump scene_8_aoc_ein
    elif True:

        show iris_upright pose8 brows_neutral eyes_closed_happy mouth_talking -more_blush at left
        $ aoc_schools.pop(1)
        i "\"That's okay! We can just continue with your first school.\""
        jump scene_8_aoc_age_eligibility

label scene_8_aoc_ein:

    show screen one_line_input(label_text="EIN of your school", value_name=f"aoc_schools[{school_number_being_entered}].ein", placeholder_text="", changed_function=validate_and_save_ein_active_field_array_prop, value_type="arr_prop_string")
    i "\"What is the EIN of [_current_school_name]? You should be able to find it on form 1098-T, or look it up.\""

    while aoc_schools[school_number_being_entered].ein == "" or get_error_message_by_id(f"aoc_schools[{school_number_being_entered}].ein") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if aoc_schools[school_number_being_entered].ein == "":
            $ add_error(f"aoc_schools[{school_number_being_entered}].ein", "You must respond!")
        i "\"What is the EIN of [_current_school_name]? You should be able to find it on form 1098-T, or look it up.\""

    hide screen one_line_input

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_wide_open mouth_smiling more_blush at flipped
    i "\"Hehe, I'm imagining your idyllic campus life, [first_name]. Were you popular with your classmates?\""
    if school_number_being_entered == 0:
        jump scene_8_aoc_second_school_screener
    elif True:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open -more_blush at left
        i "\"That just about does it for [_current_school_name]. You've got quite the educational track record, [first_name].\""
        jump scene_8_aoc_age_eligibility

label scene_8_aoc_second_school_screener:
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="I did", no_text="No, just the one"))
    i "\"That just about does it for [_current_school_name]. Did you attend a second educational institution in [TAX_YEAR], [first_name]?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"That just about does it for [_current_school_name]. Did you attend a second educational institution in [TAX_YEAR], [first_name]?\""

    if screener_choice:
        hide screen choice_input
        $ school_number_being_entered = 1
        jump scene_8_aoc_school_entry
    elif True:
        hide screen choice_input
        if claiming_aoc:
            jump scene_8_aoc_age_eligibility
        elif True:
            jump scene_8_lllc_eligible_expenses_screener

label scene_8_aoc_age_eligibility:
    $ age = get_age_at_end_of_tax_year_from_birth_date(birth_date)
    if age >= 24:
        hide screen choice_input
        jump scene_8_aoc_refundable_eligible
    elif age >= 19:
        hide screen choice_input
        if student_status == FULL_TIME_CHOICE:
            jump scene_8_aoc_earned_income_eligibility
        elif True:
            jump scene_8_aoc_refundable_eligible
    elif age == 18:
        hide screen choice_input
        jump scene_8_aoc_earned_income_eligibility
    elif True:
        hide screen choice_input
        jump scene_8_aoc_parents_alive_eligibility

label scene_8_aoc_earned_income_eligibility:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_talking -more_blush at left, flipped
    $ aoc_refundable_earned_income_half_of_support = None
    $ total_amount_w2_box_1 = '{0:.2f}'.format(get_total_w2_box_1())
    show screen choice_input("aoc_refundable_earned_income_half_of_support", choices=custom_yes_or_no_choices(yes_text="My earned income was at least half of my total support", no_text="No, I had other sources of support. My earned income was less than half of my total support", has_what=True, what_text="What do you ean by \"total support\" Iris?"))
    i "\"Was your earned income (I believe you said %(total_amount_w2_box_1)s earlier, right %(first_name)s?) less than or more than half of your total financial support in %(TAX_YEAR)s?\""

    while aoc_refundable_earned_income_half_of_support == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_refundable_earned_income_half_of_support", "You must respond!")
        i "\"Was your earned income (I believe you said %(total_amount_w2_box_1)s earlier, right %(first_name)s?) less than or more than half of your total financial support in %(TAX_YEAR)s?\""

    hide screen choice_input
    if aoc_refundable_earned_income_half_of_support == True:
        $ interest_income_earned_income_half_of_support = True
        jump scene_8_aoc_refundable_eligible
    elif aoc_refundable_earned_income_half_of_support == False:
        $ interest_income_earned_income_half_of_support = False
        jump scene_8_aoc_parents_alive_eligibility
    elif True:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_neutral mouth_talking at move_center_from_left
        $ rollback_enabled = False
        i "\"Support includes food, shelter, clothing, medical and dental care, education, and the like.\""
        $ rollback_enabled = True
        i "\"To figure out your total support, count support provided by you, your parents, and others. A scholarship received by you, however, isn't considered support if you were a full-time student.\""
        $ rollback_enabled = False
        hide screen choice_input
        jump scene_8_aoc_earned_income_eligibility

label scene_8_aoc_parents_alive_eligibility:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at left
    $ aoc_refundable_parents_alive = None
    show screen choice_input("aoc_refundable_parents_alive", choices=custom_yes_or_no_choices(yes_text=f"Yes one or both of my parents were alive on Dec 31, {TAX_YEAR}", no_text=f"No, neither of my parents were alive on Dec 31, {TAX_YEAR}"))
    i "\"It’s great to have people in your life who will support you. [first_name], were one or both of your parents alive on Dec 31, [TAX_YEAR]?\""

    while aoc_refundable_parents_alive == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("aoc_refundable_parents_alive", "You must respond!")
        i "\"It’s great to have people in your life who will support you. [first_name], were one or both of your parents alive on Dec 31, [TAX_YEAR]?\""

    hide screen choice_input
    if aoc_refundable_parents_alive:
        jump scene_8_aoc_refundable_ineligible
    elif True:
        show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed at flipped
        i "\"Ohhhh, %(first_name)s, I'm so sorry to hear that!\""
        jump scene_8_aoc_refundable_eligible

label scene_8_aoc_refundable_ineligible:
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush at center
    $ aoc_refundable_eligible = False
    i "\"Based on the info you've provided, [first_name], you qualify for the American Opportunity Credit. Though you're not eligible for the refundable portion of this credit, it's still pretty exciting!\""
    i "\"There’s so many things that you need when you’re learning.\""
    jump scene_8_aoc_eligible_expenses_screener

label scene_8_aoc_refundable_eligible:
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush at center
    $ aoc_refundable_eligible = True
    i "\"Based on the info you've provided [first_name], you qualify for the American Opportunity Credit, and you're even eligible to claim up to 40%% of it as a refundable credit- that's so exciting!\""
    i "\"There’s so many things that you need when you’re learning.\""
    jump scene_8_aoc_eligible_expenses_screener

label scene_8_lllc_eligible_expenses_screener:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_talking at left
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="My expenses were...", no_text="Adjusted? Qualified? What counts and what doesn't?"))
    i "\"What were your adjusted, qualified education expenses in [TAX_YEAR]? One note %(first_name)s, the maximum amount of expenses that can be factored into the Lifetime Learning Credit calculation is $10,000, so don't enter more than that amount.\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"What were your adjusted, qualified education expenses in [TAX_YEAR]? One note %(first_name)s, the maximum amount of expenses that can be factored into the Lifetime Learning Credit calculation is $10,000, so don't enter more than that amount.\""

    hide screen choice_input
    if screener_choice:
        jump scene_8_lllc_eligible_expenses
    elif True:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at flipped, move_center_from_left
        $ rollback_enabled = False
        i "\"Adjusted, qualified education expenses are tuition and other fees required for enrollment minus any tax-free education assistance.\""
        $ rollback_enabled = True
        i "\"Examples of tax-free education assistance include the tax-free part of any scholarship, fellowship grant, employer-provided education assistance, veterans’ educational assistance...\""
        i "\"...and any other education assistance that is excludable from gross income (tax free), other than as a gift, bequest, devise, or inheritance.\""
        $ rollback_enabled = False
        jump scene_8_lllc_eligible_expenses_screener

label scene_8_lllc_eligible_expenses:
    show screen one_line_input(label_text="Qualified expenses", value_name="aoc_qualified_educational_expenses", placeholder_text="", changed_function=validate_and_save_dollar_active_field_less_than_10000, value_type="float")
    i "\"What were your adjusted, qualified education expenses in 2022? One note %(first_name)s, the maximum amount of expenses that can be factored into the Lifetime Learning Credit calculation is $10,000, so don't enter more than that amount.\""
    while aoc_qualified_educational_expenses == None or get_error_message_by_id("aoc_qualified_educational_expenses") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if aoc_qualified_educational_expenses == None:
            $ add_error("aoc_qualified_educational_expenses", "You must respond!")
        i "\"What were your adjusted, qualified education expenses in 2022? One note %(first_name)s, the maximum amount of expenses that can be factored into the Lifetime Learning Credit calculation is $10,000, so don't enter more than that amount.\""
    hide screen one_line_input
    jump scene_8_aoc_calculations

label scene_8_aoc_eligible_expenses_screener:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_talking -more_blush at move_left_from_center
    $ screener_choice = None
    show screen choice_input("screener_choice", choices=custom_yes_or_no_choices(yes_text="My expenses were...", no_text="Adjusted? Qualified? What counts and what doesn't?"))
    i "\"What were your adjusted, qualified education expenses in 2022? One note %(first_name)s, the maximum amount of expenses that can be factored into the American Opportunity Credit calculation is $4,000, so don't enter more than that amount.\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"What were your adjusted, qualified education expenses in 2022? One note %(first_name)s, the maximum amount of expenses that can be factored into the American Opportunity Credit calculation is $4,000, so don't enter more than that amount.\""

    hide screen choice_input
    if screener_choice:
        jump scene_8_aoc_eligible_expenses
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at flipped, move_center_from_left
        $ rollback_enabled = False
        i "\"Adjusted, qualified education expenses are tuition and other fees required for enrollment minus any tax-free education assistance.\""
        $ rollback_enabled = True
        i "\"For the American Opportunity Credit, expenses for books, supplies, and equipment needed for a course of study also count as qualified education expenses.\""
        i "\"Examples of tax-free education assistance include the tax-free part of any scholarship, fellowship grant, employer-provided education assistance, veterans’ educational assistance...\""
        i "\"...and any other education assistance that is excludable from gross income (tax free), other than as a gift, bequest, devise, or inheritance.\""
        $ rollback_enabled = False
        jump scene_8_aoc_eligible_expenses_screener

label scene_8_aoc_eligible_expenses:
    show screen one_line_input(label_text="Qualified expenses", value_name="aoc_qualified_educational_expenses", placeholder_text="", changed_function=validate_and_save_dollar_active_field_less_than_4000, value_type="float")
    i "\"What were your adjusted, qualified education expenses in 2022? One note %(first_name)s, the maximum amount of expenses that can be factored into the American Opportunity Credit calculation is $4,000, so don't enter more than that amount.\""
    while aoc_qualified_educational_expenses == "" or get_error_message_by_id("aoc_qualified_educational_expenses") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if aoc_qualified_educational_expenses == "":
            $ add_error("aoc_qualified_educational_expenses", "You must respond!")
        i "\"What were your adjusted, qualified education expenses in 2022? One note %(first_name)s, the maximum amount of expenses that can be factored into the American Opportunity Credit calculation is $4,000, so don't enter more than that amount.\""
    hide screen one_line_input
    jump scene_8_aoc_calculations

label scene_8_aoc_calculations:
    $ calculate_return_up_to_8863()
    $ education_tax_credit_str = '{0:.2f}'.format(education_tax_credit)
    $ refundable_education_tax_credit = '{0:.2f}'.format(form_8863_line_8)
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open at move_center_from_left
    i "\"I think it’s so admirable that you take education seriously, [first_name].\""

    if claiming_aoc and aoc_refundable_eligible:
        i "\"You’re able to claim a credit of $[education_tax_credit_str]! Plus, $[refundable_education_tax_credit] of it is refundable, so it’s actually money you get back, not just less tax you owe.\""
    elif True:
        i "\"You’re able to claim a credit of $[education_tax_credit_str]! That’s great.\""

    jump scene_8_eic

label scene_8_eic:
    $ calculate_return_up_to_agi()
    scene library_to_sunset
    if form_1040_line_11 >= 90000:
        jump scene_8_made_too_much_for_credits
    if age >= 65 or age < 25 or form_1040_line_11 >= 16480 or someone_can_claim_as_dependent:

        jump scene_8_standard_deduction
    elif True:
        jump scene_8_eic_prompt

label scene_8_eic_prompt:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open more_blush
    if claiming_aoc or claiming_lllc:
        i "\"Hmm, there’s one more credit we can look at in addition to your education credits, [first_name]!\""
        i "\"I just need to double check a couple things though–\""
    elif True:
        i "\"You might not be eligible for educational credits, but there could be another option!\""

    jump scene_8_nontaxable_combat_pay

label scene_8_nontaxable_combat_pay:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_wide_open mouth_talking at left
    $ had_nontaxable_combat_pay = None
    show screen choice_input("had_nontaxable_combat_pay", choices=custom_yes_or_no_choices(yes_text="I did", no_text="I did not", has_what=True, what_text="A what?"))
    i "\"First off, did you have non-taxable combat pay in 2022, %(first_name)s? That would be listed on your W-2 in box 12 with code Q\""

    while had_nontaxable_combat_pay == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("had_nontaxable_combat_pay", "You must respond!")
        i "\"First off, did you have non-taxable combat pay in 2022, %(first_name)s? That would be listed on your W-2 in box 12 with code Q\""

    hide screen choice_input
    if had_nontaxable_combat_pay == True:
        show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush at move_center_from_left
        i "\"Wow, really? Hmmm, I bet you look great in uniform!\""
        jump scene_8_nontaxable_combat_pay_input
    elif had_nontaxable_combat_pay == False:
        jump scene_8_eic_main_question
    elif True:
        hide iris_bent
        show iris_upright pose7 brows_neutral eyes_neutral mouth_talking
        i "\"Nontaxable combat pay is military pay that you received while you were deployed to a combat zone. This pay is not taxable and is excluded from your taxable income. The pay is typically reported on a W-2 in box 12, with accompanying code Q.\""
        jump scene_8_nontaxable_combat_pay

label scene_8_nontaxable_combat_pay_input:
    hide iris_bent
    show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at move_left_from_center
    show screen one_line_input(label_text="Amount", value_name="nontaxable_combat_pay_election", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"How much income did you elect to classify as nontaxable combat pay?\""
    while get_error_message_by_id("nontaxable_combat_pay_election") is not None or nontaxable_combat_pay_election == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if nontaxable_combat_pay_election == None:
            $ add_error("nontaxable_combat_pay_election", "You must respond!")
        i "\"How much income did you elect to classify as nontaxable combat pay?\""
    hide screen one_line_input
    jump scene_8_eic_main_question

label scene_8_eic_main_question:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_wide_open mouth_talking -more_blush at left

    $ resided_in_us_for_more_than_half_the_year = None
    show screen choice_input("resided_in_us_for_more_than_half_the_year", choices=custom_yes_or_no_choices(yes_text="Yeah", no_text="No, it wasn't", has_what=True, what_text="What does \"main home\" mean, exactly?"))
    i "\"Okay, second question! Was your main home in the United States for 50%% or more of [TAX_YEAR]?\""

    while resided_in_us_for_more_than_half_the_year == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("resided_in_us_for_more_than_half_the_year", "You must respond!")
        i "\"Okay, second question! Was your main home in the United States for 50%% or more of [TAX_YEAR]?\""

    hide screen choice_input
    if resided_in_us_for_more_than_half_the_year != True and resided_in_us_for_more_than_half_the_year != False:
        hide iris_bent
        show iris_upright pose9 brows_neutral eyes_neutral mouth_talking at flipped
        i "\"[first_name] your main home or principal residence is the home where you live most of the time. It’s also the address you use to receive mail and file your tax returns.\""
        jump scene_8_eic_main_question

    $ determine_if_eligible_for_eitc()
    if qualifies_for_eitc:
        hide iris_bent
        show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open more_blush at center
        i "\"Amazing! Okay, [first_name], I believe you qualify for the Earned Income Tax Credit!\""
    elif True:
        show iris_bent pose4 brows_sad eyes_wink mouth_wide_open more_blush at flipped, center
        i "\"Oh, I see. You’re quite the international mystery, aren’t you? Unfortunately that will mean you don’t qualify for the Earned Income Tax Credit.\""

    jump scene_8_standard_deduction

label scene_8_made_too_much_for_credits:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
    i "\"Hmm [first_name], you know, with your income situation, you actually don’t qualify for the American Opportunity Credit, the Lifetime Learning Credit, or the Earned Income Tax Credit.\""
    i "\"You made a bit too much money to qualify for these tax credits.\""
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open
    i "\"I know that might be a little frustrating, but..it is kind of attractive in a person, you know.\""
    jump scene_8_standard_deduction

label scene_8_standard_deduction:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open at center
    $ calculate_return()

    if age < 65 and not someone_can_claim_as_dependent and not is_blind:
        jump scene_8_standard_deduction_simple
    elif not someone_can_claim_as_dependent:
        if age >= 65 and not is_blind:
            jump scene_8_standard_deduction_no_dep_over_65_not_blind
        elif age < 65 and is_blind:
            jump scene_8_standard_deduction_no_dep_under_65_blind
        elif True:
            jump scene_8_standard_deduction_no_dep_over_65_blind
    elif True:
        jump scene_8_standard_deduction_can_be_claimed


label scene_8_standard_deduction_simple:
    i "\"Based on the fact that your income comes from simple sources [first_name], I’d say you can take the standard deduction. In your case that’s $[form_1040_line_12:,.2f]!\""
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open
    i "\"Simple is good, you know?\""
    jump scene_8_standard_deduction_outro

label scene_8_standard_deduction_no_dep_over_65_not_blind:
    i "\"Based on the information you’ve provided [first_name], I’d say you can take the standard deduction. In your case that’s $12,950. Plus, you’re over 65 so you can claim an additional $1,750, bringing your total standard deduction amount to $[form_1040_line_12:,.2f].\""
    i "\"Hehe, [first_name] I may be biased but I have to say you’ve aged like a fine wine… and I’d drink you up any day!\""
    jump scene_8_standard_deduction_outro

label scene_8_standard_deduction_no_dep_under_65_blind:
    i "\" Based on the information you’ve provided [first_name], I’d say you can take the standard deduction. In your case that’s $12,950!\""
    i "\"I remember you mentioned that you were legally blind on the last day of [TAX_YEAR], so you can claim an additional $1,750, bringing your total standard deduction amount to $[form_1040_line_12:,.2f].\""
    jump scene_8_standard_deduction_outro

label scene_8_standard_deduction_no_dep_over_65_blind:
    i "\"Based on the information you’ve provided [first_name], I’d say you can take the standard deduction. In your case that’s $12,950.\""
    i "\"Plus, since you were legally blind on the last day of [TAX_YEAR] and you’re over 65, you can claim an additional $3,500, bringing your total standard deduction amount to $[form_1040_line_12:,.2f].\""
    jump scene_8_standard_deduction_outro

label scene_8_standard_deduction_can_be_claimed:
    i "\"Based on the information you’ve provided [first_name], you’re eligible to claim a standard deduction of $[form_1040_line_12:,.2f].\""
    jump scene_8_standard_deduction_outro

label scene_8_standard_deduction_outro:
    i "\"But we should check on a few other things, just in case you’re eligible to make some adjustments to your income.\""
    i "\"Always do your best! That’s my motto!\""
    jump scene_8_has_educator_expenses


label scene_8_has_educator_expenses:
    hide iris_upright
    show iris_bent pose2 brows_neutral eyes_looking_away mouth_smiling at left
    $ has_educator_expenses = None
    show screen choice_input("has_educator_expenses", choices=custom_yes_or_no_choices(has_what=True, what_text="I'm not sure, define \"qualified\""))
    i "\"I know you said your occupation is [occupation], right [first_name]? But to check just in case, are you a qualified educator at a qualified school?\""

    while has_educator_expenses == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_educator_expenses", "You must respond!")
        i "\"I know you said your occupation is [occupation], right [first_name]? But to check just in case, are you a qualified educator at a qualified school?\""

    hide screen choice_input
    if has_educator_expenses is True:
        jump educator_expenses_screener
    elif has_educator_expenses is False:
        hide iris_upright
        show iris_bent pose4 brows_sad eyes_looking_away mouth_smiling more_blush at move_center_from_left, flipped
        i "\"Well, it’s always good to check. Still, [first_name] I’ll be your student sometime…I bet you could probably teach me a thing or two, hehe. \""
        jump scene_8_has_tax_deferred_ira_contributions
    elif True:
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at move_center_from_left
        $ rollback_enabled = False
        i "\"No problem [first_name]! A “qualified educator” is someone who was a kindergarten through grade 12 teacher, instructor, counselor, principal, or aid, for at least 900 hours during the [TAX_YEAR] school year...\""
        $ rollback_enabled = True
        i "\"...at a school that provides elementary or secondary education as determined under state law.\""
        $ rollback_enabled = False
        jump scene_8_has_educator_expenses

label educator_expenses_screener:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_closed_happy mouth_smiling at left, flipped

    $ has_educator_expenses = None
    show screen choice_input("has_educator_expenses", choices=custom_yes_or_no_choices(yes_text="Yes, I did", no_text="No, I didn't", has_what=True, what_text="What are qualified educator expenses?"))
    i "\"Great! In [TAX_YEAR], did you have any qualified educator expenses that you paid for out of your own pocket?\""
    while has_educator_expenses == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_educator_expenses", "You must respond!")
        i "\"Great! In [TAX_YEAR], did you have any qualified educator expenses that you paid for out of your own pocket?\""

    hide screen choice_input
    if has_educator_expenses is True:
        hide iris_bent
        show iris_upright pose8 brows_angry eyes_neutral mouth_wide_open at move_center_from_left, flipped
        i "\"Wow [first_name]! That’s so selfless, I bet your students really appreciate it!\""
        jump scene_8_has_educator_expenses_input
    elif has_educator_expenses is False:
        hide iris_bent
        show iris_upright pose8 brows_neutral eyes_closed_happy mouth_talking at move_center_from_left
        i "\"Okay! It’s unfortunate that the American education system requires so many educators to pay for classroom supplies out of pocket, I’m glad you weren’t put in that position.\""
        jump scene_8_has_tax_deferred_ira_contributions
    elif True:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at move_center_from_left
        $ rollback_enabled = False
        i "\"Qualified expenses are amounts you paid or incurred for books, supplies, computer equipment, professional development courses, and other supplementary materials that you use in the classroom.\""

        jump educator_expenses_screener

label scene_8_has_educator_expenses_input:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_smiling more_blush at move_left_from_center
    show screen one_line_input(label_text="Educator expenses", value_name="educator_expenses", placeholder_text="", changed_function=validate_and_save_dollar_active_field_less_than_equal_to_limit, value_type="float")
    i "\"How much were your expenses? Unfortunately [first_name], only up to $300 of educator expenses can be factored into this income adjustment.\""

    while educator_expenses == None or get_error_message_by_id("educator_expenses") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if educator_expenses == None:
            $ add_error("educator_expenses", "You must respond!")
        i "\"How much were your expenses? Unfortunately [first_name], only up to $300 of educator expenses can be factored into this income adjustment.\""

    hide screen one_line_input
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush at move_center_from_left, flipped
    i "\"Hehe~ you must be such a good teacher, [first_name]. I wonder if you’d like to give me some special tutoring sometime <3\""
    jump scene_8_has_tax_deferred_ira_contributions

label scene_8_has_tax_deferred_ira_contributions:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open at left
    $ has_tax_deferred_ira_contributions = None
    show screen choice_input("has_tax_deferred_ira_contributions", choices=custom_yes_or_no_choices(has_what=True, what_text="What is a traditional IRA?"))
    i "\"Next question, [first_name]. Let’s see…Did you make any contributions to a traditional IRA in 2022? Remember, [first_name] don’t include {b}Roth{/b} IRA contributions here, they work differently.\""

    while has_tax_deferred_ira_contributions == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_tax_deferred_ira_contributions", "You must respond!")
        i "\"Next question, [first_name]. Let’s see…Did you make any contributions to a traditional IRA in 2022? Remember, [first_name] don’t include {b}Roth{/b} IRA contributions here, they work differently.\""

    hide screen choice_input
    if has_tax_deferred_ira_contributions is True:
        show iris_bent pose4 brows_sad eyes_looking_away mouth_smiling more_blush at move_center_from_left, flipped
        i "\"You’re so proactive, [first_name]! You seem like you’re really good with money. \""
        jump scene_8_ira_covered_by_work_retirement_plan
    elif has_tax_deferred_ira_contributions is False:
        hide iris_upright
        show iris_bent pose2 brows_angry eyes_wide_open mouth_wide_open more_blush at move_center_from_left, flipped
        $ tax_deferred_ira_contributions = 0
        i "\"Okay, no problem [first_name]. I hope you don’t think I’m not asking too many questions. It’s always better to check than to miss something, right?\""
        jump scene_8_has_student_loan_interest_intro
    elif True:
        hide iris_bent
        show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open at move_center_from_left, flipped
        i "\"With a traditional IRA, the contributions you make are tax-deferred: you pay tax when the money comes back out of the account, not when you put it in. In contrast, Roth IRAs are funded with after-tax money, and the distributions in the future are tax free.\""
        jump scene_8_has_tax_deferred_ira_contributions

label scene_8_ira_covered_by_work_retirement_plan:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open -more_blush at left, flipped
    $ is_covered_by_employer_retirement_plan = None
    show screen choice_input('is_covered_by_employer_retirement_plan', choices=custom_yes_or_no_choices(has_what=True, what_text="I'm not sure"))

    i "\"[first_name], are you covered by a retirement plan at work?\""

    while is_covered_by_employer_retirement_plan == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("is_covered_by_employer_retirement_plan", "You must respond!")
        i "\"[first_name], are you covered by a retirement plan at work?\""

    hide screen choice_input
    if is_covered_by_employer_retirement_plan == True:
        $ calculate_return_up_to_agi()
        if form_1040_line_11 > 68000:
            i "\"Hmmm, I see. [first_name], based on the income information you’ve provided, your IRA contributions are either ineligible to be deducted or the amount you can deduct is subject to “phase out,” meaning you can only deduct a portion of those contributions.\""
            i "\"Non deductible IRA contributions have to be handled a little differently [first_name], and reported on a Form 8606. Those calculations are a little too complicated for me.\""
            call screen game_over_modal(jump_back_to="scene_8_ira_covered_by_work_retirement_plan", message="{i}Tax Heaven 3000{/i} does not  currently support certain filers who made traditional IRA contributions whilst covered by an employer-sponsored retirement plan")
        elif True:
            jump scene_8_tax_deferred_ira_contributions_input
    elif is_covered_by_employer_retirement_plan == False:
        hide iris_upright
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling at flipped
        i "\"Good for you to have your own IRA running [first_name]! Saving for the future is important! Foresight is an attractive quality you know.\""
        jump scene_8_tax_deferred_ira_contributions_input
    elif True:
        hide iris_bent
        show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open at flipped
        i "\"If you’re not sure if you’re covered by an employer retirement plan [first_name], just look at Box 13 on your W-2. If there is a checkbox in the “retirement plan” box, you are covered! If you’re still not sure, check with your employer.\""
        jump scene_8_ira_covered_by_work_retirement_plan

label scene_8_tax_deferred_ira_contributions_input:
    hide iris_bent
    show iris_upright pose11 brows_neutral eyes_neutral mouth_smiling at left, flipped
    show screen one_line_input(label_text="IRA Contributions", value_name="tax_deferred_ira_contributions", placeholder_text="", changed_function=validate_and_save_ira_contribution_active_field, value_type="float")
    $ renpy.dynamic("max_ira_contribution")
    $ max_ira_contribution = MAX_IRA_CONTRIBUTION_UNDER_50 if age < 50 else MAX_IRA_CONTRIBUTION_50_OR_OVER
    i "\"What was the total amount of 2022 IRA contributions you made? Remember [first_name] this value shouldn’t be more than $[max_ira_contribution:,] - that was the maximum allowable contribution in [TAX_YEAR] for someone your age.\""

    while get_error_message_by_id("tax_deferred_ira_contributions") is not None or tax_deferred_ira_contributions == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if tax_deferred_ira_contributions == None:
            $ add_error("tax_deferred_ira_contributions", "You must respond!")
        i "\"What was the total amount of 2022 IRA contributions you made? Remember [first_name] this value shouldn’t be more than $[max_ira_contribution:,] - that was the maximum allowable contribution in [TAX_YEAR] for someone your age.\""
    hide screen one_line_input
    jump scene_8_ira_deduction

label scene_8_ira_deduction:
    $ calculate_return()
    hide iris_bent
    show iris_upright pose10 brows_angry eyes_neutral mouth_wide_open more_blush at move_center_from_left
    i "\"Okay, let’s see now… Based on the information you’ve told me, you are eligible to claim a deduction of $[form_schedule1_line_20:,.2f]!\""
    jump scene_8_has_student_loan_interest_intro

label scene_8_has_student_loan_interest_intro:
    if calculate_form_schedule1_magi() >= 85000 or someone_can_claim_as_dependent:
        $ has_student_loan_interest = False
        jump scene_8_estimated_tax_payments
    elif True:
        hide iris_bent
        show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open more_blush
        i "\"Let’s keep checking for a few more deductions, [first_name]!\""
        jump scene_8_has_student_loan_interest

label scene_8_has_student_loan_interest:
    $ has_student_loan_interest = None
    hide iris_upright
    show iris_bent pose3 brows_sad eyes_wide_open mouth_talking at move_left_from_center
    show screen choice_input("has_student_loan_interest", choices=custom_yes_or_no_choices(has_what=True, what_text="What is a qualified student loan?"))
    i "\"Did you make any interest payments on a qualified student loan (or loans) in [TAX_YEAR]??\""

    while has_student_loan_interest == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("has_student_loan_interest", "You must respond!")
        i "\"Did you make any interest payments on a qualified student loan (or loans) in [TAX_YEAR]??\""

    hide screen choice_input
    if has_student_loan_interest is True:
        jump scene_8_student_loan_interest_input_screener
    elif has_student_loan_interest is False:
        hide iris_upright
        show iris_bent pose2 brows_neutral eyes_closed_happy mouth_wide_open at move_center_from_left, flipped
        i "\"Student loans can be such a heavy burden [first_name]! I got my education in the lab– I mean, I didn’t go to college, so I don’t know what it’s like, but it’s a lucky thing to be debt free!\""
        jump scene_8_estimated_tax_payments
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_closed_happy mouth_talking at flipped
        $ rollback_enabled = False
        i "\"A qualified student loan is a loan you took out solely to pay for qualified education expenses, within a reasonable amount of time, for education provided during an academic period for an eligible student.\""
        $ rollback_enabled = True
        i "\"[first_name], if you paid at least $600 in student loan interest in 2022, the lender should have issued you a 1098-E form.\""
        i "\"If you paid less than $600, the lender might not have issued you a 1098-E, but you can still report these payments.\""
        i "\"If you’re unsure what the amount you paid in 2022 was, you should call the lender and request this information.\""
        $ rollback_enabled = False
        jump scene_8_has_student_loan_interest

label scene_8_student_loan_interest_input_screener:
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open at left
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text='I paid this much...', no_text='How would I find out how much I paid in total?'))
    i "\"Great! What was the total amount of interest you paid across all of your loans?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Great! What was the total amount of interest you paid across all of your loans?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_8_student_loan_interest_input
    elif True:
        hide iris_bent
        show iris_upright pose7 brows_neutral eyes_closed_happy mouth_smiling at move_center_from_left, flipped
        $ rollback_enabled = False
        i "\"The amount of interest you paid on a student loan can be found in Box 1 of Form 1098-E, which is a tax form the loan lender should have issued you if you paid them more than $600 in [TAX_YEAR].\""
        $ rollback_enabled = True
        i "\"If you didn’t receive a 1098-E from your loan lender, you can contact them and request that information.\""
        i "\"If you had loans from multiple lenders you’ll need to add your payments together to get the total amount.\""
        $ rollback_enabled = False
        jump scene_8_student_loan_interest_input_screener

label scene_8_student_loan_interest_input:
    show screen one_line_input(label_text="Your contributions", value_name="student_loan_interest", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"Great! What was the total amount of interest you paid across all of your loans?\""

    while student_loan_interest == None or get_error_message_by_id("student_loan_interest") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if student_loan_interest == None:
            $ add_error("student_loan_interest", "You must respond!")
        i "\"Great! What was the total amount of interest you paid across all of your loans?\""

    hide screen one_line_input
    if student_loan_interest > 2500:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_neutral mouth_talking at move_center_from_left
        i "\"I see! Unfortunately [first_name], $2,500 is the maximum amount of interest payment that can be factored into this income adjustment, so we’ll just have to bring that down as $2,500.\""
        show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped
        i "\"I don’t make the rules! I’d let you deduct more if I could, [first_name].\""
        $ student_loan_interest = 2500
        $ calculate_return()
        hide iris_bent
        show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open more_blush at flipped
        i "\"Based on the information you’ve told me [first_name], you are eligible to claim a deduction of $[form_schedule1_line_21:,.2f]\""
    elif True:
        $ calculate_return()
        hide iris_bent
        show iris_upright pose10 brows_sad eyes_crazy mouth_wide_open more_blush at flipped
        i "\"Amazing! Based on the information you’ve told me [first_name], you are eligible to claim a deduction of $[form_schedule1_line_21:,.2f]\""
    jump scene_8_estimated_tax_payments

label scene_8_estimated_tax_payments:
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open more_blush
    i "\"I think that just about covers adjustments to your income for [TAX_YEAR].\""
    show iris_upright pose10 brows_neutral eyes_wink mouth_wide_open -more_blush
    i "\"You’re very organized with all your information, even if you don’t think so!\""
    show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open at flipped
    i "\"Speaking of which…\""
    jump scene_8_estimated_tax_payments_screener

label scene_8_estimated_tax_payments_screener:
    hide iris_upright
    show iris_bent pose4 brows_angry eyes_closed_happy mouth_wide_open at move_left_from_center
    $ made_estimated_tax_payments_this_year = None
    show screen choice_input("made_estimated_tax_payments_this_year", choices=custom_yes_or_no_choices(yes_text="I did make estimated tax payments in [TAX_YEAR]", no_text="I didn't", has_what=True, what_text="What does that mean?"))
    i "\"Did you make any estimated tax payments during %(TAX_YEAR)s?\""

    while made_estimated_tax_payments_this_year == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("made_estimated_tax_payments_this_year", "You must respond!")
        i "\"Did you make any estimated tax payments during %(TAX_YEAR)s?\""

    hide screen choice_input
    if made_estimated_tax_payments_this_year is True:
        jump scene_8_estimated_tax_payments_input
    elif made_estimated_tax_payments_this_year is False:
        $ estimated_tax_payments = 0
        jump scene_8_applying_previous_year_payments
    elif True:
        hide iris_bent
        show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open more_blush at move_center_from_left
        i "\"Estimated tax is a quarterly payment of taxes for the year based on the filer’s reported income for the period. Generally, the folks required to pay quarterly taxes are small business owners, freelancers, and independent contractors.\""
        jump scene_8_estimated_tax_payments_screener

label scene_8_estimated_tax_payments_input:
    show screen one_line_input(label_text="Estimated payments", value_name="estimated_tax_payments", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"What amount of estimated tax payments did you make for [TAX_YEAR]?\""
    while get_error_message_by_id("estimated_tax_payments") is not None or estimated_tax_payments == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if estimated_tax_payments == None:
            $ add_error("estimated_tax_payments", "You must respond!")
        i "\"What amount of estimated tax payments did you make for [TAX_YEAR]?\""
    hide screen one_line_input
    jump scene_8_applying_previous_year_payments

label scene_8_applying_previous_year_payments:
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_closed_neutral mouth_talking more_blush at left
    $ applying_previous_year_payments = None
    show screen choice_input("applying_previous_year_payments", choices=custom_yes_or_no_choices(yes_text=f"I did apply money from my {PREVIOUS_TAX_YEAR} refund towards this year’s payment", no_text="I didn’t apply any payment forward", has_what=True, what_text="What? How would I know if I did that?"))
    i "\"I see! What about any amount from your {b}[PREVIOUS_TAX_YEAR]{/b} tax refund that you chose to apply to this year’s filing? You’re so thoughtful I wonder if you did anything like that last year.\""

    while applying_previous_year_payments == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("applying_previous_year_payments", "You must respond!")
        i "\"I see! What about any amount from your {b}[PREVIOUS_TAX_YEAR]{/b} tax refund that you chose to apply to this year’s filing? You’re so thoughtful I wonder if you did anything like that last year.\""

    hide screen choice_input
    if applying_previous_year_payments == True:
        jump scene_8_applying_previous_year_payments_input
    elif applying_previous_year_payments == False:
        $ amount_applied_from_previous_year = 0
        jump scene_8_outro
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_sad eyes_neutral mouth_talking at move_center_from_left, flipped
        i "\"You would need to look at your [PREVIOUS_TAX_YEAR] tax return! If you had a tax refund last year but you chose not to receive all of the money, then the balance is waiting to be applied to your return this year.\""
        jump scene_8_applying_previous_year_payments

label scene_8_applying_previous_year_payments_input:
    show screen one_line_input(label_text="Amount", value_name="amount_applied_from_previous_year", placeholder_text="", changed_function=validate_and_save_dollar_active_field, value_type="float")
    i "\"What amount from your {b}[PREVIOUS_TAX_YEAR]{/b} tax refund did you choose to apply to this year’s filing?\""
    while get_error_message_by_id("amount_applied_from_previous_year") is not None or amount_applied_from_previous_year == None:
        play sound "audio/error_beep.ogg" volume 0.3
        if amount_applied_from_previous_year == None:
            $ add_error("amount_applied_from_previous_year", "You must respond!")
        i "\"What amount from your {b}[PREVIOUS_TAX_YEAR]{/b} tax refund did you choose to apply to this year’s filing?\""
    hide screen one_line_input
    jump scene_8_outro

label scene_8_outro:
    hide iris_bent
    show iris_upright pose7 brows_neutral eyes_neutral mouth_wide_open at move_center_from_left
    i "\"Say, [first_name]. You know I didn’t really just want to talk to you about tax credits.\""
    i "\"Sometimes when I get nervous I just default to things that are familiar.\""

    show iris_upright pose8 brows_neutral eyes_closed_happy mouth_talking
    "Iris takes a deep breath. I get the feeling that she hadn’t quite planned out what to say next."

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_smiling more_blush at flipped
    i "\"Why don’t we meet…in my room next time?\""
    stop music fadeout 1.0
    jump scene_8_end_scene

label scene_8_end_scene:
    $ library_visited = True
    $ update_completed_dates()
    $ calculate_return()
    $ add_personal_diary_page(PERSONAL_DIARY_PAGE_8)
    $ purge_saves()
    jump new_day_4

label new_day_4:
    scene black with fade
    window hide
    play sound "audio/new_day.ogg"
    pause 3
    call scene_transition ("scene_4c") from _call_scene_transition_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
