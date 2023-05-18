label scene_3_intro:
    $ show_overlay = False
    scene bg coffee
    pause 1.0
    play music "audio/main_theme.ogg" fadein 0.5
    jump scene_3_intro_dialogue

label scene_3_intro_dialogue:
    "Here’s the local coffee shop. It’s cute!"
    "Nothing too fancy going on here with their coffee offerings, but definitely a step above your average chain."
    i "\"Hey [first_name]! Over here!\""
    "Iris is waving at me enthusiastically from the corner table."
    "I recognize her little notebook on the table. She really must take it everywhere."

    show iris_bent pose2 brows_neutral eyes_wide_open mouth_wide_open at easein_fast

    i "\"I got here a little early!\""
    i "\"I’m glad you came! It’s so exciting meeting a new person in a new place, don’t you think?\""

    jump scene_3_filing_jointly

label scene_3_filing_jointly:
    $ screener_choice = None
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_smiling more_blush
    i "\"Especially when you’re a single– um. Well, actually [first_name], are you filing singly or jointly on your [TAX_YEAR] federal tax return?\""
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_smiling more_blush at move_left_from_center
    show screen screener_choice(choices=FILING_STATUS_CHOICES)
    "Is she trying to ask whether I'm single or not? This is a weird way to do it, but I guess I'm not in a position to judge the first person I've met in a new town."
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Is she trying to ask whether I'm single or not? This is a weird way to do it, but I guess I'm not in a position to judge the first person I've met in a new town."

    hide screen screener_choice
    if screener_choice == FILING_SINGLY_CHOICE:
        jump scene_3_filing_singly_married
    elif screener_choice == MARRIED_FILING_JOINTLY_CHOICE:
        show iris_bent pose2 brows_sad eyes_looking_away mouth_embarrassed more_blush at move_center_from_left
        i "\"Oh, I see... you already have someone in your life\""
        "She looks away"
        show iris_bent pose3 brows_angry eyes_wide_open mouth_frowning
        i "\"Maybe I had the wrong idea, [first_name]. I'm looking for someone special and I thought...well. Maybe it's better if we go our separate ways.\""
        call screen game_over_modal(jump_back_to="scene_3_filing_jointly", message="{i}Tax Heaven 3000{/i} only supports filers with a marital status of single")
    elif screener_choice == SURVIVING_SPOUSE_CHOICE:
        show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed at flipped, move_center_from_left
        i "\"Oh, [first_name]... I'm sorry.\""
        "She looks away"
        hide iris_bent
        show iris_upright pose10 brows_sad eyes_neutral mouth_embarrassed more_blush at flipped
        i "\"That's... I'm not sure I'm ready for that tax situation.\""
        i "\"Maybe it's better if we go our separate ways.\""
        call screen game_over_modal(jump_back_to="scene_3_filing_jointly", message="{i}Tax Heaven 3000{/i} only supports single filers")
    elif True:
        jump scene_3_hoh_qualifying_dependents

label scene_3_filing_singly_married:
    $ screener_choice = None
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling -more_blush at left
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Nope, I'm not married!", no_text="Oh wait, no, I'm actually not filing singly", has_what=True, what_text="Well, I am actually married, just filing separately"))
    i "\"Oh, that's great! You're a single filer! And ummm, you're not married are you?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Oh, that's great! You're a single filer! And ummm, you're not married are you?\""

    hide screen screener_choice
    if screener_choice == True:
        jump scene_3_single_filer_interstitial
    elif screener_choice == False:
        show iris_bent pose2 brows_sad eyes_looking_away mouth_embarrassed more_blush at flipped, move_center_from_left
        i "\"Oh you're…you're not?\""
        jump scene_3_filing_status_generic_game_over
    elif True:
        show iris_bent pose2 brows_sad eyes_looking_away mouth_embarrassed more_blush at flipped, move_center_from_left
        i "\"Oh, I see... you already have someone in your life.\""
        "She looks away"
        show iris_bent pose3 brows_angry eyes_wide_open mouth_frowning
        i "\"Maybe I had the wrong idea, [first_name]. I'm looking for someone special and I thought...well. Maybe it's better if we go our separate ways.\""
        call screen game_over_modal(jump_back_to="scene_3_filing_jointly", message="{i}Tax Heaven 3000{/i} only supports filers with a marital status of single")

label scene_3_hoh_qualifying_dependents:
    $ screener_choice = None
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_looking_away mouth_talking more_blush at flipped, left
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="That's right, I have a qualifying child or dependent", no_text="Umm. No, I don't. I guess that means I\'m actually just filing singly.", has_what=True, what_text="What does that mean?"))

    i "\"Umm, I see [first_name]. And you have a qualifying child or dependent? That's the only way you qualify as head of household, you know.\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Umm, I see [first_name]. And you have a qualifying child or dependent? That's the only way you qualify as head of household, you know.\""

    hide screen screener_choice
    if screener_choice == True:
        hide iris_bent
        show iris_upright pose11 brows_sad eyes_looking_away mouth_embarrassed at flipped, move_center_from_left
        i "\"Oh! You do?\""
        i "\"Um, I'm sorry [first_name] but I think that's a little more than I bargained for.\""
        i "\"I'm not ready to see someone who has dependents' tax implications, let alone the dependents themselves!\""
        call screen game_over_modal(jump_back_to="scene_3_hoh_qualifying_dependents", message="{i}Tax Heaven 3000{/i} only supports filers without dependents")
    elif screener_choice == False:
        call scene_3_single_filer_interstitial ("scene_3_birthday") from _call_scene_3_single_filer_interstitial
    elif True:
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_talking -more_blush at move_center_from_left
        i "\"Dependents are either a qualifying child or a qualifying relative. For example, a child, stepchild, brother, sister, or parent.\""
        "Wow, you really know a lot about this stuff don’t you?"
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush
        i "\"Well, I don’t know everything. But I try my best!\""
        jump scene_3_hoh_qualifying_dependents

label scene_3_filing_status_generic_game_over:
    "She looks away"
    show iris_bent pose3 brows_angry eyes_wide_open mouth_frowning
    i "\"Maybe I had the wrong idea, [first_name]. I'm looking for someone special and I thought...well. Maybe it's better if we go our separate ways.\""
    call screen game_over_modal(jump_back_to="scene_3_filing_jointly", message="{i}Tax Heaven 3000{/i} only supports single filers")

label scene_3_single_filer_interstitial(next_label="scene_3_dependents"):
    hide iris_bent
    show iris_upright pose10 brows_neutral eyes_neutral mouth_wide_open more_blush at flipped, move_center_from_left

    i "\"Yay~ Umm, I’m single too, you know. I could give you a hand with your taxes if you want, [first_name]!\""
    show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open -more_blush
    i "\"Oh! I mean…only if you want to. You know, we could compare notes as we go.\""

    hide iris_upright
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    "Iris seems a bit flustered by her own sudden rush of enthusiasm."
    "I’m not sure it’s my first choice of activity…but I could use all the help I can get when it comes to taxes."

    call expression (next_label) from _call_expression_1

label scene_3_dependents:
    $ screener_choice = None
    hide iris_bent
    show iris_upright pose11 brows_sad eyes_neutral mouth_talking -more_blush at left, flipped
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Yes, I do", has_what=True, what_text="Any what?"))
    i "\"So…you’re a single filer, [first_name]. Do you have any dependents?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"So…you’re a single filer, [first_name]. Do you have any dependents?\""

    hide screen screener_choice
    if screener_choice == True:
        jump scene_3_dependents_generic_game_over
    elif screener_choice == False:
        jump scene_3_dependents_2
    elif True:
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_talking at move_center_from_left
        i "\"Dependents are either a qualifying child or a qualifying relative. For example, a child, stepchild, brother, sister, or parent.\""
        "\"Wow, you really know a lot about this stuff don’t you?\""
        show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush
        i "\"Well, I don’t know everything but I try my best!\""
        jump scene_3_dependents

label scene_3_dependents_2:
    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="No", no_text="Wait, actually yes, I do."))
    i "\"I see. You don't have any qualifying children or relatives as dependents?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"I see. You don't have any qualifying children or relatives as dependents?\""

    hide screen screener_choice
    if screener_choice == True:
        jump scene_3_birthday
    elif screener_choice == False:
        jump scene_3_dependents_generic_game_over

label scene_3_birthday:
    $ birth_date = None
    hide iris_bent
    show iris_upright pose10 brows_neutral eyes_neutral mouth_wide_open -more_blush at flipped, center

    i "\"No dependents… [first_name] you come without any strings attached, then.\""
    i "\"Haha, I’m also doing my best to avoid any complicated situations.\""

    hide iris_upright
    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling at move_left_from_center, flipped

    show screen one_line_input(label_text="Your birthdate", value_name="birth_date", placeholder_text="MM/DD/YYYY", changed_function=validate_and_save_birth_date)
    i "\"How old are you %(first_name)s?\""
    while birth_date == None or get_error_message_by_id("birth_date") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if get_error_message_by_id("birth_date") is None:
            $ add_error("birth_date", "You must respond!")
        i "\"How old are you %(first_name)s?\""

    hide screen one_line_input
    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling at flipped
    $ _age_today = get_age_today_from_birth_date(birth_date)
    i "\"[_age_today], huh? Hmmm, I see.\""
    jump scene_3_types_of_income

label scene_3_dependents_generic_game_over:
    hide iris_bent
    show iris_upright pose7 brows_sad eyes_neutral mouth_embarrassed at move_center_from_left
    i "\"Oh! You do?\""
    i "\"Um, I'm sorry [first_name] but I think that's a little more than I bargained for.\""
    i "\"I'm not ready to see someone who has dependents' tax implications, let alone the dependents themselves!\""
    call screen game_over_modal(jump_back_to="scene_3_dependents", message="{i}Tax Heaven 3000{/i} only supports people without dependents")

label scene_3_types_of_income:
    hide iris_upright
    show iris_bent pose4 brows_neutral eyes_looking_away mouth_smiling more_blush
    i "\"What if we…\""
    hide iris_bent
    show iris_upright pose10 brows_sad eyes_neutral mouth_wide_open
    i "\"Got to know each other’s financial situation a little better, [first_name]?\""
    jump scene_3_types_of_income_screener

label scene_3_types_of_income_screener:
    $ screener_choices = []
    show screen screener_multi_choice(choices=INCOME_TYPE_CHOICES, ypos=400)
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_wide_open more_blush at move_left_from_center
    i "\"For [TAX_YEAR], what types of income did you have? There are lots of types, so maybe the easiest thing to do is to just look at what forms you have received.\""

    while screener_choices == []:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choices", "You must respond!")
        i "\"For [TAX_YEAR], what types of income did you have? There are lots of types, so maybe the easiest thing to do is to just look at what forms you have received.\""

    hide screen screener_multi_choice
    if OTHER_FORMS_CHOICE in screener_choices:
        jump scene_3_types_of_income_generic_game_over
    elif INT_1099_CHOICE in screener_choices:
        jump scene_3_1099_int_double_check
    elif WHAT_CHOICE in screener_choices:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at move_center_from_left
        $ rollback_enabled = False
        i "\"Well, so, a Form W-2 is issued by a full or part-time employer. It reports your income for the year, as well as the amount of tax withheld from your paychecks.\""
        $ rollback_enabled = True
        i "\"You should receive one of these from any job where you’re an official employee– as opposed to freelance, gig work, or self-employment.\""
        i "\"A Form 1099-G reports income you receive from unemployment compensation.\""
        i "\"A Form SSA-1099 reports income you receive from social security benefits.\""
        i "\"A Form 1099-INT reports interest income from a bank account, CD, or a few other cases.\""
        i "\"In general, if you have any of these types of income, you will have received the appropriate form!\""
        $ rollback_enabled = False
        "How do you know all this?"
        show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open
        i "\"I just try my best! There’s always more to learn!\""
        jump scene_3_types_of_income_screener
    elif True:
        hide iris_bent
        show iris_upright pose7 brows_neutral eyes_wink mouth_wide_open at move_center_from_left
        i "Got it! I think I can handle you, [first_name]."
        jump scene_3_pre_crypto_dialogue

label scene_3_1099_int_double_check:
    $ screener_choice = None
    show screen screener_choice(choices=YES_OR_NO_CHOICES)
    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_neutral mouth_talking at left, flipped
    i "\"I see. I have to ask...At any time during [TAX_YEAR], did you have a financial interest in or signature authority over a financial account (such as a bank account, securities account, or brokerage account) located outside the United States?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"I see. I have to ask...At any time during [TAX_YEAR], did you have a financial interest in or signature authority over a financial account (such as a bank account, securities account, or brokerage account) located outside the United States?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_3_types_of_income_foreign_game_over
    elif True:
        jump scene_3_foreign_trust_check

label scene_3_foreign_trust_check:
    $ screener_choice = None
    show screen screener_choice(choices=YES_OR_NO_CHOICES)
    show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at left
    i "\"Oh, alright then! And just in case, during [TAX_YEAR], did you receive a distribution from, or were you the grantor of, or transferor to, a foreign trust?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Oh, alright then! And just in case, during [TAX_YEAR], did you receive a distribution from, or were you the grantor of, or transferor to, a foreign trust?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_3_types_of_income_foreign_game_over
    elif True:
        show iris_upright pose9 brows_neutral eyes_closed_happy mouth_wide_open more_blush at move_center_from_left
        i "\"That's a relief! [first_name] I have to admit you're a little intimidating, but I think I can handle you.\""
        jump scene_3_pre_crypto_dialogue

label scene_3_types_of_income_foreign_game_over:
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed at move_center_from_left
    i "\"Oh, wow!\""
    i "\"Don't take this the wrong way, but your finances are a little intimidating...\""
    hide iris_bent
    show iris_upright pose8 brows_sad eyes_neutral mouth_frowning
    i "\"I'm not really looking for something that serious right now.\""
    i "\"Maybe it's better if we go our separate ways.\""
    call screen game_over_modal(jump_back_to="scene_3_types_of_income_screener", message="{i}Tax Heaven 3000{/i} does not currently support filers with foreign income") 

label scene_3_types_of_income_generic_game_over:
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_looking_away mouth_embarrassed at move_center_from_left
    i "\"Oh, wow!\""
    i "\"Don't take this the wrong way, but your finances are a little intimidating...\""
    hide iris_bent
    show iris_upright pose8 brows_sad eyes_neutral mouth_frowning
    i "\"I'm not really looking for something that serious right now.\""
    i "\"Maybe it's better if we go our separate ways.\""
    call screen game_over_modal(jump_back_to="scene_3_types_of_income_screener", message="{i}Tax Heaven 3000{/i} does not currently support one or more of your income types") 

label scene_3_pre_crypto_dialogue:
    hide iris_upright
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush
    i "\"Hehe~ isn’t it great to meet people who are in a place in their life that is similar to yours?\""
    i "\"Of course anyone can relate to anyone\""
    show iris_bent pose4 brows_sad eyes_wide_open mouth_wide_open more_blush
    i "\"But there’s a certain chemistry that exists when your situations are similar, wouldn’t you say, [first_name]?\""

    "Iris sure has a certain starry-eyed energy about her."
    "But I understand that feeling! When you don’t have a lot of pre-existing attachments in life it can be easy and enjoyable to try new things."
    show iris_bent pose2 brows_sad eyes_closed_happy mouth_smiling more_blush
    "\"Iris you keep asking me about my financial situation– how about you? What do you do for work?\""

    show iris_bent pose5 brows_neutral eyes_wide_open mouth_wide_open -more_blush
    i "\"I work at the library! I love being surrounded by books all day. I can learn so much.\""

    i "\"Like how yarn is made, and what coral is. \""
    show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open
    i "\"But not just facts you know– also what it’s like to love a parent, or to be lonely, or how people who’ve never met can become close from a chance meeting.\""

    show iris_bent pose5 brows_sad eyes_wide_open mouth_wide_open
    "Iris seems to realize she’s waxing on a bit. I feel like most people learn these things naturally just by growing up, and not by reading?"
    "Still, she smiles happily. She really does seem to enjoy this thought."

    show iris_bent pose6 brows_sad eyes_closed_happy mouth_wide_open more_blush
    i "\"Why don’t you come find me there sometime? I’m usually at a desk writing in my notebook when I’m not off in the stacks someplace.\""
    i "\"It’s also nice and private most of the time…\""

    show iris_bent pose5 brows_neutral eyes_looking_away mouth_smiling more_blush
    "The library, huh? Not necessarily the first place I’d go to hang out."
    "Hang on though– I guess that’s an invitation to see each other again?"
    "In that case, bury me in books, baby!"

    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open
    i "\"I guess you could say I’m an analog girl at heart.\""

    jump scene_3_crypto

label scene_3_crypto:
    $ screener_choice = None
    hide iris_bent
    show iris_upright pose9 brows_neutral eyes_neutral mouth_wide_open
    i "\"You don't let your finances get too digital do you, [first_name]? Did you sell, trade, gift, or receive any cryptocurrency in [TAX_YEAR]?\""

    show iris_upright pose7 brows_neutral eyes_neutral mouth_wide_open at move_left_from_center, flipped
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="No, I didn't", no_text="Yesss lol gm frens! Wagmi!", has_what=True, what_text="Did I do what?"))
    i "\"I guess I don't mind too much if you just own some though.\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"I guess I don't mind too much if you just own some though.\""

    hide screen screener_choice
    if screener_choice == True:
        show iris_upright pose7 brows_neutral eyes_neutral mouth_wide_open at move_center_from_left, flipped
        i "\"Oh! You seem pretty savvy [first_name], so I’m glad you aren’t taken in by a pyramid scheme like that.\""
        i "\"[first_name] it’s really nice to talk with you, I have a good feeling about the two of us.\""
        jump scene_3_phone_screener
    elif screener_choice == False:
        hide iris_bent
        show iris_upright pose10 brows_angry eyes_crazy mouth_embarrassed more_blush at flipped, move_center_from_left
        i "\"Oh.\""
        "It's astonishing how quickly her expression changes."
        hide iris_upright
        show iris_bent pose3 brows_neutral eyes_closed_happy mouth_wide_open
        i "\"Umm. [first_name]...I think I'm going to go.\""
        call screen game_over_modal(jump_back_to="scene_3_crypto", message="{i}Tax Heaven 3000{/i} does not support filers with income from digital assets")
    elif True:
        hide iris_bent
        show iris_upright pose11 brows_neutral eyes_neutral mouth_talking at move_center_from_left
        $ rollback_enabled = False
        i "\"Well let’s see. If you don’t know what cryptocurrency is, this probably doesn’t apply to you.\""
        $ rollback_enabled = True
        i "\"Tell me if you received any crypto– either for free, as payment, from an airdrop, through mining, or through staking.\""
        i "\"Also, let me know if you sold any crypto for fiat currency, or exchanged crypto/tokens, or if you gifted crypto to another person.\""
        $ rollback_enabled = False
        jump scene_3_crypto

label scene_3_phone_screener:
    $ screener_choice = None
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush at move_left_from_center
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Yeah, for sure!", no_text="I'm not sure...why?"))
    i "\"Hey, will you give me your phone number?\""

    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        i "\"Hey, will you give me your phone number?\""

    hide screen screener_choice
    if screener_choice:
        jump scene_3_phone_email
    elif True:
        jump scene_3_phone_screener_2

label scene_3_phone_screener_2:
    hide iris_bent
    show iris_upright pose10 brows_neutral eyes_crazy mouth_wide_open more_blush
    i "\"Well, what if I want to call you so we can see each other again, silly?\""
    hide iris_upright
    show iris_bent pose3 brows_neutral eyes_looking_away mouth_wide_open at flipped
    i "\"Or, what if the IRS needs your contact information, and I need to provide it to them because you've…become mysteriously unreachable?\""
    show iris_bent pose4 brows_neutral eyes_looking_away mouth_smiling more_blush
    i "\"Hmm or maybe I want to send you a picture...?\""
    "Well...okay"
    jump scene_3_phone_email

label scene_3_phone_email:
    hide iris_upright
    show iris_bent pose4 brows_sad eyes_closed_happy mouth_smiling more_blush at left
    show screen one_line_input(label_text="Your phone number", value_name="phone_number", placeholder_text="XXX-XXX-XXXX", changed_function=validate_and_save_phone_number)
    i "\"%(first_name)s, what is your phone number?\""
    while phone_number == "" or get_error_message_by_id("phone_number") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if get_error_message_by_id("phone_number") is None:
            $ add_error("phone_number", "You must respond!")
        i "\"%(first_name)s, what is your phone number?\""
    hide screen one_line_input

    show iris_bent pose2 brows_neutral eyes_wide_open mouth_smiling at move_center_from_left
    "Iris puts her number into my phone. She’s one of those people who uses her forefinger instead of her thumbs to type on a phone."
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush at move_left_from_center

    show screen one_line_input(label_text="Your email", value_name="email", placeholder_text="you@example.com", changed_function=validate_and_save_email)
    i "\"%(first_name)s, will you give me your email too? I want to be in full contact with you, hehe.\""
    while email == "" or get_error_message_by_id("email") is not None:
        play sound "audio/error_beep.ogg" volume 0.3
        if get_error_message_by_id("email") is None:
            $ add_error("email", "You must respond!")
        i "\"%(first_name)s, will you give me your email too? I want to be in full contact with you, hehe.\""

    hide screen one_line_input
    show iris_bent pose4 brows_neutral eyes_wide_open mouth_wide_open more_blush at move_center_from_left
    "Iris is an exceptionally odd conversationalist, but her earnest enthusiasm is charming, despite the fact that she has an acute interest in my tax status."
    "After drinking our coffee the date with Iris concludes smoothly."

    hide iris_bent
    show iris_upright pose8 brows_neutral eyes_neutral mouth_wide_open
    i "\"Gotta run! I’ll see you tomorrow, right? Come by the library and find me!\""
    $ purge_saves()
    $ add_personal_diary_page(PERSONAL_DIARY_PAGE_2)
    jump new_day_2

label new_day_2:
    stop music fadeout 1.0
    scene black with fade
    window hide
    play sound "audio/new_day.ogg"
    pause 3
    "Up and at ‘em! Today is another lovely day."
    "The fact that I still haven’t started my taxes this year is nibbling at the back of my mind a little…"
    "But the sun is shining, and I’m meeting Iris at the library!"
    "Let’s figure out where that is…"
    call scene_transition ("scene_4a") from _call_scene_transition
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
