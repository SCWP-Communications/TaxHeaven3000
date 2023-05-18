define turbo = Character("Turbo", window_background=Image("gui/textbox-iris.png", xalign=0.4, yalign=1.0), color="#FFFFFF", who_outlines=[ (2, "#640C35"), (2, "#640C35", 2, 2) ], what_outlines=[ (2, "#FFFFFF") ])
define barista = Character("Barista", window_background=Image("gui/textbox-iris.png", xalign=0.4, yalign=1.0), color="#FFFFFF", who_outlines=[ (2, "#640C35"), (2, "#640C35", 2, 2) ], what_outlines=[ (2, "#FFFFFF") ])
define yolanda = DynamicCharacter("library_patron_name", window_background=Image("gui/textbox-iris.png", xalign=0.4, yalign=1.0), color="#FFFFFF", who_outlines=[ (2, "#640C35"), (2, "#640C35", 2, 2) ], what_outlines=[ (2, "#FFFFFF") ])
define pedestrian = Character("Pedestrian", window_background=Image("gui/textbox-iris.png", xalign=0.4, yalign=1.0), color="#FFFFFF", who_outlines=[ (2, "#640C35"), (2, "#640C35", 2, 2) ], what_outlines=[ (2, "#FFFFFF") ])
define unknown = Character("???", window_background=Image("gui/textbox-iris.png", xalign=0.4, yalign=1.0), color="#FFFFFF", who_outlines=[ (2, "#640C35"), (2, "#640C35", 2, 2) ], what_outlines=[ (2, "#FFFFFF") ])




label scene_6b_intro:

    scene bg coffee
    play music "audio/main_theme.ogg" fadein 0.5

    "I'll stop by the cafe and get something to drink"
    "It's definitely a cafe chain, but I can see that the small town regulars transform it into something a little bit more personal."
    "I can imagine that if I come here enough it will start to feel homey."

    show barista at center, easein
    barista "\"Hi, welcome to Café de Ductions!\""

    $ screener_choice = None
    show screen screener_choice(choices=COFFEE_CHOICES)
    barista "\"What can I get you?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "Pick one!")
        barista "\"What can I get you?\""
    hide screen screener_choice

    "\"Yeah, can I get uhhhh, [screener_choice]?\""
    barista "\"Yep! I’ll get that started for you.\""
    "The girl behind the counter tucks my order slip next to some others."

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Ask about it", no_text="Ignore it"), variant="narrator")
    "There’s a note on one of the order slips with the name of a drink I’ve never seen."
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "There’s a note on one of the order slips with the name of a drink I’ve never seen."
    hide screen screener_choice

    if screener_choice:
        $ knows_iris_favorite_drink = True
        jump scene_6b_ask_about_drink
    elif True:
        jump scene_6b_drink_ready

label scene_6b_ask_about_drink:
    "\"Hey, what is “Ventichagomacchiucci?” I can’t help but notice it written there, and I’ve never heard of anything like that.\""
    barista "\"Where did you see that?\""
    barista "\"Ohhh hahaha! I see, it’s on the receipt there.\""
    barista "\"That’s not a real menu item– there’s this pink-haired girl who orders the craziest thing I’ve ever seen a human drink.\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="What all is in it?", no_text="Damn, can I change my order and try it?"), variant="narrator")
    barista "\"We made up a name for it so we don’t have to write all the ingredients down as a custom order.\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        barista "\"We made up a name for it so we don’t have to write all the ingredients down as a custom order.\""
    hide screen screener_choice

    if screener_choice:
        jump scene_6b_whats_all_in_it
    elif True:
        jump scene_6b_change_order_and_try

label scene_6b_whats_all_in_it:
    "Pink hair, huh? That sounds familiar…"
    "\"How crazy are we talking here? What goes into it?\""
    barista "\"Oh my god everything. It’s got a half-dozen espresso shots, milk, condensed milk, EVERY nut milk, matcha powder…\""
    barista "\"Boba pearls, protein powder, turmeric, this new-age-y mushroom powder…and don’t even get me started on the flavor shots.\""
    barista "\"It’s something like 2200 calories. If you wanted to feel insane I think you could probably survive off of this stuff.\""

    jump scene_6b_drink_ready

label scene_6b_change_order_and_try:
    "Pink hair, huh? That sounds familiar…"
    "\"You know I consider myself something of a connoisseur of coffee drinks, can I get one?\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="I'm sure!", no_text="How bad can it be?"), variant="narrator")
    barista "\"Umm if you're really sure...\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        barista "\"Umm if you're really sure...\""
    hide screen screener_choice

    barista "\"Alright, but don’t say I didn’t warn you.\""
    "She starts mixing a drink."

    "Six shots of espresso go in."
    "Almond milk, oat milk, soy milk…condensed milk? Why do they even have that here?"
    "Protein powder? Boba pearls? Does that canister say “Mushroom Powder?”"
    "At some point I stop registering each new ingredient. I have a sinking feeling that I’m in too deep."

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Take a gulp", no_text="Accept the drink but don't drink it"), variant="narrator")
    barista "\"It’s ready. Here you go!\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        barista "\"It’s ready. Here you go!\""
    hide screen screener_choice

    if screener_choice:
        "\"Thank you! Here goes nothing.\""
        "*GULP*" with vpunch
        "Almost immediately my head starts to buzz and the liquid sits like a brick in my stomach."
        "Not only is this a full day’s worth of calories, but it gets you absolutely wired."
        "It’s like something out of science fiction - Soylent Green - or a nutrient sludge you’d use to grow a creature in a lab."
        "I need to throw this away and get out of the cafe. I need fresh air."
        barista "\"Have a nice day!\""
        jump scene_6b_ending
    elif True:
        "\"...Thank you!\""
        "The barista visibly smirks. I’m sure my face clearly indicates that I regret my decision to order this."
        "This is clearly borderline undrinkable."
        "It’s like something out of science fiction - Soylent Green - or a nutrient sludge you’d use to grow a creature in a lab."
        "I think my quest for a drink ends in a loss."
        jump scene_6b_ending

label scene_6b_drink_ready:
    barista "\"Here you go!\""
    "\"Thank you!\""
    "Just what I neeed! I'll sit for a minute and sip this."

    jump scene_6b_ending

label scene_6b_ending:

    if not scene_6b_completed:
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_1)
    $ scene_6b_completed = True
    if first_diary_visit_completed:
        call scene_transition from _call_scene_transition_8
    elif True:
        call scene_transition ("scene_4a") from _call_scene_transition_12




label scene_6c_intro:
    scene bg sidewalk sunset
    play music "audio/main_theme.ogg" fadein 0.5

    "What’s this? There’s a guy blocking the entrance to the queue at the cafe."
    "He looks frustrated… I wonder if something’s up."

    show pedestrian at center, easein
    pedestrian "\"Ugh…what a terrible experience…\""

    "\"What’s wrong? You look like you’ve been through the wringer.\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="No, not yet", no_text="I’m a bit late but I’m working on it"))
    pedestrian "\"What? Oh…nothing to worry about…just – have you filed your taxes yet this year?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        pedestrian "\"What? Oh…nothing to worry about…just – have you filed your taxes yet this year?\""
    hide screen screener_choice

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Why?", no_text="I wasn’t planning to…"))
    pedestrian "\"Okay well, trust me on this: if you’re going to use a tax prep service don’t use TurboTax!\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        pedestrian "\"Okay well, trust me on this: if you’re going to use a tax prep service don’t use TurboTax!\""
    hide screen screener_choice

    if screener_choice:
        "\"They’re just tax filing software, right? What happened to you?\""
    elif True:
        pedestrian "\"Good.\""

    pedestrian "\"Listen to me, those guys seem nice but there’s something off about them.\""
    pedestrian "\"It’s fishy for an industry to build itself up specifically around gating a public branch of the government\""
    pedestrian "\"They’re deliberately establishing themselves as a bottleneck\""
    pedestrian "\"If you ask me that’s a crazy amount of leverage– and not just to force us ordinary folks to pay for their services.\""
    pedestrian "\"They say whoever controls the money controls the world…and that means Big Tax Software has the government’s primary revenue stream by the balls.\""
    pedestrian "\"That’s supervillain stuff right there!\""
    pedestrian "\"They–!!\""
    pedestrian "\"Ok, Ok. I’m calm. I shouldn’t even be talking about this. I don’t mean to hold you from getting your coffee.\""

    "\"All good. I’m going to go order my drink now though\""
    pedestrian "\"Go for it. Thanks for letting me vent a little!\""

    if not scene_6c_completed:
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_5)
    $ scene_6c_completed = True
    call scene_transition ("scene_6d_intro") from _call_scene_transition_9






label scene_6d_intro:
    scene bg coffee
    play music "audio/main_theme.ogg" fadein 0.5

    $ random_thought = random.choice([
        "Mmmmm the smell of fresh coffee",
        "Gosh I need a good cup of java",
        "I’m in the mood for some single origin bean juice",
        "I could use some caffeine",
        "Always smells nice in here"
    ])

    "[random_thought]"

    show barista at center, easein
    barista "\"Hi, welcome to Café de Ductions!\""

    $ screener_choice = None
    show screen screener_choice(choices=COFFEE_CHOICES)
    barista "\"What can I get you?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        barista "\"What can I get you?\""
    hide screen screener_choice

    "\"Yeah, can I get uhhhh, [screener_choice]?\""
    barista "\"Yep! I’ll get that started for you.\""
    "She begins to prep the drink."
    barista "\"Here you go!\""

    $ scene_6d_completed = True
    if not first_diary_visit_completed:
        call scene_transition ("scene_4a") from _call_scene_transition_13
    elif cafe_visited and office_visited and library_visited and not iris_home_visited:
        call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_14
    elif True:
        call scene_transition from _call_scene_transition_17





label scene_7b_intro:
    scene bg office on
    play music "audio/main_theme.ogg" fadein 0.5

    "The library branch office must also serve some kind of public-facing purpose, because you can just walk in here."
    "It doesn’t look like there’s much pressing business going on in this office…"
    "There’s a stack of yellow cards in a filing box here. It looks like they might be interlibrary loan requests."
    "Presumably this is how the library handles requests for books they don’t have on their shelves."
    "Physical paper slips. Downright archaic. On the other hand, quaint."
    "I can’t help but look at what books have been requested…"
    "{i}“Synthetic Human Biology,” “Brainwashing From A Psychological Viewpoint,” “A History Of The IRS,” “How To Win Friends And Influence People”{/i}"
    "This is a kind of unpleasant list of books. Also…it looks like these have all been requested by the same guy?"

    play music "audio/diary_remix.ogg" fadein 0.5
    show turbo pose1 brows_angry at turbo_2_up, center, easein
    turbo "\"Hey! You there. Do you work here?\""
    "Who the heck is this? He’s got all the hallmarks of a predatory finance guy."
    show turbo pose2 brows_angry mouth_open more_angry
    turbo "\"What kind of outdated joint uses paper filing requests? Can’t you move on this quicker?\""
    turbo "\"I’m a busy guy here!\""
    "\"Hey calm down, I don’t work here in any case.\""
    show turbo pose1 brows_angry eyes_closed mouth_open more_desperate -more_angry
    turbo "\"Ugh. Of course you don’t. It’s too much to assume there would be an available employee.\""
    turbo "\"Public institutions are so inefficient.\""
    show turbo pose1 brows_angry -eyes_closed -mouth_open -more_desperate
    turbo "\"My name’s Turbo. Hey, are you from around here?\""
    "\"I am, but I’m new to the area.\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Introduce yourself", no_text="Nah"), variant="narrator")
    "Should I introduce myself? I’m getting a bad vibe from this guy."
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Should I introduce myself? I’m getting a bad vibe from this guy."
    hide screen screener_choice

    if screener_choice:
        "\"My name's %(first_name)s\""
        show turbo pose1 eyes_closed -brows_angry
        turbo "\" %(first_name)s, eh?\""
        turbo "\"Tell me something, %(first_name)s. You look like a law-abiding individual.\""
    elif True:
        show turbo pose1 -brows_angry
        turbo "\"…I see.\""
        turbo "\"Well, it’s always nice to see new faces in town.\""

    show turbo pose2 -eyes_closed -brows_angry
    turbo "\"Have you filed your taxes yet? It’s about that time of the year.\""
    turbo "\"I always pride myself on being able to help out someone new, and it just so happens that I represent a certain organization that could help you there.\""
    show turbo pose1
    turbo "\"Why don’t I tell you more over a cup of coffee.\""
    "Uhhh. This guy is definitely a narc."
    "And with a moniker like “Turbo” I can imagine which organization he represents."
    "\"I’m good, thanks. But I appreciate the offer.\""

    show turbo pose2 eyes_closed mouth_open
    turbo "\"Taxes are complicated, you know. I’m sure I don’t have to tell you that.\""
    turbo "\"Any sensible person confronts taxes with fear, uncertainty, and doubt.\""
    turbo "\"I’d strongly recommend that you consider my services\""
    "\"I actually feel quite confident in my taxes. It just so happens that I’ve got a friend who is helping me out, and I trust her.\""
    show turbo pose2 brows_angry -mouth_open -eyes_closed
    turbo "\"...\""
    show turbo pose2 brows_angry mouth_open more_angry more_desperate
    turbo "\"Wait. A friend. \""
    turbo "\"She’s helping you with your taxes.\""
    turbo "\"That’s highly unusual, you know. Do your friends often help you with your taxes?\""
    "\"Well, maybe but I–\""
    show turbo pose2 brows_angry mouth_open more_angry -more_desperate
    turbo "\"You just moved here.\""
    turbo "\"You haven’t even known her that long, have you?\""
    "\"Whoah whoah, slow down here, I think you’ve got the wrong–\""
    show turbo pose1 -brows_angry -mouth_open -more_angry
    turbo "\"Tell me. What is her name?\""
    turbo "\"Tell me. What color is her hair?\""
    show turbo pose2 brows_angry mouth_open more_angry more_desperate
    turbo "\"TELL ME.\""

    "Hoooooly shit"
    "He’s insane."
    "Is this usual for TurboTa–"

    show turbo at turbo_2_up, move_left_from_center
    show yolanda at yolanda_2_up, right, easein
    yolanda "\"Yoohoo, excuse me!\""

    show turbo pose1 brows_angry eyes_closed mouth_open more_desperate -more_angry at turbo_2_up, left, focus
    turbo "\"What do you–\""
    show turbo pose2 -brows_angry -eyes_closed -mouth_open -more_desperate
    turbo "\"…excuse me.\""
    show turbo pose1 brows_angry
    turbo "\"Can I help you?\""
    show turbo pose2 eyes_closed mouth_open -brows_angry
    turbo "\"We’re kind of in the middle of something here.\""
    show turbo pose2 eyes_closed mouth_open -brows_angry at turbo_2_up, left, unfocus

    show yolanda at yolanda_2_up, right, focus
    yolanda "\"Ummmm. Are these your interlibrary loan slips?\""
    "She gestures at the yellow slips on the desk."
    show yolanda at yolanda_2_up, right, unfocus

    show turbo pose2 brows_angry -eyes_closed -mouth_open at turbo_2_up, left, focus
    turbo "\"They are.\""
    turbo "\"Ah, finally. Are you an employee here?\""
    show turbo pose2 brows_angry -eyes_closed -mouth_open at turbo_2_up, left, unfocus

    show yolanda at yolanda_2_up, right, focus
    yolanda "\"Nope. I just spend a lot of time using the library.\""
    yolanda "\"I wanted to let you know that you’ve dropped them in the wrong box.\""
    yolanda "\"The right one is over there.\""
    show yolanda at yolanda_2_up, right, unfocus

    show turbo pose2 at turbo_2_up, left, focus
    turbo "\"The wrong…\""
    show turbo pose1 brows_angry eyes_closed mouth_open more_desperate
    turbo "\"…\""
    show turbo pose2 brows_angry mouth_open more_angry -eyes_closed -more_desperate
    turbo "\"….Thank you…\""
    show turbo at turbo_2_up, left, easeout
    stop music fadeout 2.0
    "He stalks off"
    play music "audio/main_theme.ogg" fadein 0.5
    hide turbo

    "There is something deeply weird about that guy."

    show yolanda at yolanda_2_up, move_center_from_right
    yolanda "\"You looked like you needed a little help, I hope you didn’t mind me cutting in.\""
    "\"You really saved me there!\""
    "\"Thank you!\""
    yolanda "\"You know who he works for, right?\""
    yolanda "\"Be careful…I’ve heard a lot of bad things about that one.\""
    yolanda "\"Well, I’ve got things to do. See you!\""
    show yolanda at easeout, center

    "Whew. What a reprieve."
    hide yolanda
    "So, there’s a resident creep who requests books about “synthetic human biotechnology,” is a TurboTax zealot, and is definitely stalking Iris…"
    "I’m not sure what to make of that."
    "But I’m getting out of here before he comes back."

    if not scene_7b_completed:
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_7)
    $ scene_7b_completed = True
    if not first_diary_visit_completed:
        call scene_transition ("scene_4a") from _call_scene_transition_29
    elif cafe_visited and office_visited and library_visited and not iris_home_visited:
        call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_40
    elif True:
        call scene_transition from _call_scene_transition_41





label scene_7c_intro:
    scene bg office on
    play music "audio/main_theme.ogg" fadein 0.5

    "Let’s check in on the library branch office."
    "Nearly deserted as usual…"
    "In some ways I suppose it’s comforting. This public amenity basically runs itself."

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Leave", no_text="Abscond with a small piece of office equipment"), variant="narrator")
    "Not much to see though."
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "Not much to see though."
    hide screen screener_choice

    if screener_choice:
        jump scene_7c_ending
    elif True:
        $ random_item = random.choice([
            "box of paperclips.",
            "BIC pen, only partially chewed.",
            "pack of sticky notes.",
            "red swingline stapler",
            "binder clip. One of the big ones, too!",
            "novelty rubber band in the shape of a dolphin.",
            "2B pencil. Iris would scoff at this pedestrian writing implement.",
            "Sharpie.",
        ])

        "Screw it, let’s do some petty crime."
        "Surreptitiously passing by the reception desk you steal a [random_item]"
        "Alright, time to get out of dodge!"
        "Ah, the thrill of transgression!"

label scene_7c_ending:
    $ scene_7c_completed = True
    if not first_diary_visit_completed:
        call scene_transition ("scene_4a") from _call_scene_transition_42
    elif cafe_visited and office_visited and library_visited and not iris_home_visited:
        call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_43
    elif True:
        call scene_transition from _call_scene_transition_44





label scene_5c_intro:
    window hide
    scene bg library
    play music "audio/main_theme.ogg" fadein 0.5
    menu:
        "Edit Iris' diary" if True:
            window show
            jump scene_5_diary
        "Walk around" if True:
            window show
            jump scene_5c_scene

label scene_5c_scene:
    "Since Iris isn’t at her desk I guess I’ll walk around the library a bit."
    "Maybe I’ll check out a book! Just thinking about it makes me nostalgic. Being a little kid in school is most people’s introduction to libraries. It’s funny to think it probably colors your impression of the space forever after."

    show yolanda at center, easein

    yolanda "\"Hey there! Excuse me!\""
    "Another library patron is waving to me with a friendly expression. She’s loaded down with an armful of books. She appears to be a library power user."
    yolanda "\"Do you think you could help get a book down for me? My hands are a bit full at the moment.\""
    yolanda "\"It’s that red one up on the third shelf.\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Sure, let me grab it for you", no_text="No, I don’t do 'helping people'"), variant="narrator")
    "She points at a thin volume on the shelf in front of where she’s standing."
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "She points at a thin volume on the shelf in front of where she’s standing."
    hide screen screener_choice

    if screener_choice:
        yolanda "\"Thanks so much!\""
        $ library_patron_name = "Yolanda"
        yolanda "\"I’m Yolanda. What’s your name? I don’t think I’ve seen you around before.\""
        "Something about the way she says it makes me think Yolanda spends a lot of time in the library. She sounds like she expects to recognize anyone who comes in here."
        "\"I’m %(first_name)s, I moved into town a few days ago. I just recently met this girl who works here\""
        yolanda "\"…Oh! You must mean Iris! Isn’t she a joy?\""

        $ screener_choice = None
        show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="What do you mean, odd?", no_text="I most certainly do not!"))
        yolanda "\"Although, don’t you think she’s a bit odd, %(first_name)s?\""
        while screener_choice == None:
            play sound "audio/error_beep.ogg" volume 0.3
            $ add_error("screener_choice", "You must respond!")
            yolanda "\"Although, don’t you think she’s a bit odd, %(first_name)s?\""
        hide screen screener_choice

        if screener_choice:
            yolanda "\"Not in a bad way, mind you. Just… she is very peculiar.\""

            $ screener_choice = None
            show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Is that so odd? Some people read faster than others.", no_text="She certainly does seem quite studious."), variant="narrator")
            yolanda "\"For one thing, she’s a voracious reader! She even puts me to shame– the speed she goes through a book, it’s like she’s a machine!\""
            while screener_choice == None:
                play sound "audio/error_beep.ogg" volume 0.3
                $ add_error("screener_choice", "You must respond!")
                yolanda "\"For one thing, she’s a voracious reader! She even puts me to shame– the speed she goes through a book, it’s like she’s a machine!\""
            hide screen screener_choice

            if screener_choice:
                yolanda "\"Trust me, not like this! I spend a lot of time in this library for my research and I’ve never seen anyone who compares.\""

            yolanda "\"I remember when she first started here, it was like she didn’t know how to interact with anyone.\""
            yolanda "\"She would just sit and power through books– all subjects, from the World Almanac to Dickens novels.\""
            yolanda "\"And then all of a sudden it was like she was a new person, friendly, outgoing–\""
            "Yolanda shakes her head, cutting herself off. She clearly didn’t mean to ramble on like this"
            yolanda "\"Oh what am I even saying. She’s a very nice girl, don’t listen to me rambling on.\""
            yolanda "\"Thanks for helping me with my books!\""
        elif True:
            yolanda "\"!!!\"" with vpunch
            yolanda "\"…Hahaha. Oh, don’t listen to me. I didn’t mean to insult your friend, I shouldn’t say something like that in the first place.\""
            yolanda "\"You clearly care about her.\""

            yolanda "\"I remember when she first started here, it was like she didn’t know how to interact with anyone.\""
            yolanda "\"She would just sit and power through books– all subjects, from the World Almanac to Dickens novels.\""
            yolanda "\"And then all of a sudden it was like she was a new person, friendly, outgoing–\""
            yolanda "\"I’m just glad she’s found someone.\""
            yolanda "\"Thanks for helping me with my books!\""


        if not scene_5c_completed:
            $ add_personal_diary_page(PERSONAL_DIARY_PAGE_3)
        jump scene_5c_ending
    elif True:

        yolanda "\"Ummm. Okay. Fuck you too, I guess.\""
        jump scene_5c_ending

label scene_5c_ending:
    $ scene_5c_completed = True
    if not first_diary_visit_completed:
        call scene_transition ("scene_4a") from _call_scene_transition_45
    elif cafe_visited and office_visited and library_visited and not iris_home_visited:
        call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_46
    elif True:
        call scene_transition from _call_scene_transition_47





label scene_5d_intro:
    scene library_to_sunset
    play music "audio/main_theme.ogg" fadein 0.5


    if not scene_6b_completed:
        jump scene_5d_i
    elif True:
        jump scene_5d_ii

label scene_5d_i:
    "Since Iris isn’t at her desk I guess I’ll walk around the library a bit."
    "Heck, maybe I’ll get a library card. I don’t even know how"
    "The main desk must be by the entrance, so I’ll walk back towards there"

    show barista no_cup at center, easein
    barista "\"Hey, excuse me!!\""
    "A very non-library-appropriate voice calls out to me."

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Shhhh", no_text="Say hello"), variant="narrator")
    "It’s the girl from the cafe, carrying a takeout tray of drink orders"
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        "It’s the girl from the cafe, carrying a takeout tray of drink orders"
    hide screen screener_choice

    if screener_choice:
        barista "\"What?\""
        barista "\"Oh!\""
        barista "\"*whispering* Oh right. Library.\""

    $ screener_choice = None
    show screen screener_choice(choices=custom_yes_or_no_choices(yes_text="Yes, I do", no_text="Aren’t you the barista, why are you delivering drinks?"), variant="narrator")
    barista "\"Hey I’ve got a bunch of drink orders here, do you know where the staff desks are?\""
    while screener_choice == None:
        play sound "audio/error_beep.ogg" volume 0.3
        $ add_error("screener_choice", "You must respond!")
        barista "\"Hey I’ve got a bunch of drink orders here, do you know where the staff desks are?\""
    hide screen screener_choice

    if screener_choice == False:
        barista "\"Why am I running delivery?\""
        barista "\"Gee, I wonder.\""
        barista "\"Maybe it’s because management wants to double up roles instead of hiring a proper staff.\""
        barista "\"Hey. Ask me whether we have dental. I’ll give you three guesses, and the first two don’t count.\""
        "She seems a bit harried. I think I know who’ll be on the front lines when when Café de Ductions inevitably unionizes."

    barista "\"Which desk is Iris at? The girl with the pink hair. I’ve got her usual.\""
    "She’s carrying the largest plastic cup I’ve ever seen. The color of the liquid inside is…indeterminate."
    "The drink label says “Ventichagomachiucci.” I see they’ve also misspelled Iris’ name so that it just reads ’IRS’"
    "\"Ventichago-wha? What is that drink?\""
    barista "\"Where did you see that?\""
    barista "\"Ohhh hahaha! I see, it’s on the label.\""
    barista "\"It’s not a real menu item– this girl orders the craziest thing I’ve ever seen a human drink.\""
    barista "\"We made up a name for it at the cafe so we don’t have to write all the ingredients down as a custom order.\""
    "\"How crazy are we talking here? What goes into it?\""
    barista "\"Oh my god everything. It’s got a half-dozen espresso shots, milk, condensed milk, EVERY nut milk, matcha powder…\""
    barista "\"Boba pearls, protein powder, turmeric, this new-age-y mushroom powder…and don’t even get me started on the flavor shots.\""
    barista "\"It’s something like 2200 calories. If you wanted to feel insane I think you could probably survive off of this stuff.\""
    "The liquid in the take-out cup burbles unpleasantly. It’s disturbingly viscous."
    "It’s like something out of science fiction - Soylent Green - or a nutrient sludge you’d use to grow a creature in a lab."
    barista "\"This is Iris’ desk right? I guess I’ll just leave this for her.\""
    barista "\"Thanks! See ya around\""
    show barista no_cup at easeout
    "Does Iris really drink this? It doesn’t seem like her."
    hide barista
    "I’m not entirely sure how a person would develop a taste for something like this. It barely meets the definition of food."
    "I guess I won’t be asking her today though, seems like she’s still occupied elsewhere."

    if not scene_5d_completed and not scene_6c_completed:
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_5)

    jump scene_5d_ending

label scene_5d_ii:
    "Since Iris isn’t at her desk I guess I’ll walk around the library a bit."
    "Hang on a second.."
    "Iris’ normally neat desk is oddly in disarray. Papers are strewn about, books are laid open instead of stacked."
    "The drawers behind the desk have been pulled open as well."
    "Maybe it’s nothing but…I can’t help thinking that someone just rifled through Iris’ stuff behind her back."

    unknown "\"–fitting in better than we expected, but I think I’ve found her. Patch me through.\""
    "Someone’s coming!"
    "If I duck behind the library shelves here I can listen in."

    show turbo pose1 at turbo_2_up, center, easein
    play music "audio/diary_remix.ogg" fadein 0.5

    turbo "\"This is Turbo. I’ve finally found a lead on her.\""
    show turbo pose2
    turbo "\"She blended into society smoothly enough that it wasn’t obvious. I knew the new synths were good but I didn’t realize how good.\""
    "Is he talking on a headset?"
    "Must be."
    "If it weren’t for the fact that we’re in a library I would never be able to hear him."
    turbo "\"Haha, yeah that’s right. She’s helping with a filing. We are all the products of our conditioning aren’t we?\""
    turbo "\"No. I’m sure. I’ve never gotten a human by mistake.\""
    turbo "\"Of course it’s a risk!\""
    show turbo brows_angry -mouth_open
    turbo "\"Don’t insult me, this is what I was made for.\""
    turbo "\"...\""
    show turbo pose2 -brows_angry
    turbo "\"Tell HQ I admire their work. If they’d gotten this one to Washington she would have performed admirably.\""
    turbo "\"Roger that.\""
    turbo "\"I’ll continue to observe. Given her recent activities maybe she’ll–\""

    show turbo at turbo_2_up, move_left_from_center
    show barista no_cup at barista_2_up, right, easein

    show turbo brows_angry mouth_open more_angry more_desperate
    barista "\"Ummm, excuse me!!\""
    barista "\"Are these the staff desks? I’ve got a delivery order for–\""

    show turbo pose2 -brows_angry -more_angry -more_desperate at turbo_2_up, left, focus
    turbo "\"Who’s there–?\""
    turbo "\"Oh.\""
    turbo "\"Yes, they are.\""
    show turbo pose1 -mouth_open
    turbo "\"…tell me, what’s that drink?\""
    show turbo at turbo_2_up, left, unfocus

    "The girl from Cafe de Deductions is holding a massive takeout cup full of what appears to be grey sludge."
    "Clearly this delivery order is Iris’ signature Ventichagomachiucci."
    "It looks even worse as delivery, when it’s had a chance to sit and settle."

    show barista no_cup at barista_2_up, right, focus
    barista "\"Oh, there’s this one girl who orders this crazy sludge drink. It’s got everything in it.\""
    barista "\"To be honest I don’t know how a human can stomach this, but she seems to like it.\""
    show barista no_cup at barista_2_up, right, unfocus

    show turbo pose2 at turbo_2_up, left, focus
    turbo "\"...\""
    turbo "\"...\""
    show turbo pose1
    turbo "\"Ahaha…hahahahaha…\""
    show turbo pose2
    turbo "\"Yes, this is her desk, my dear.\""
    turbo "\"You can leave it for her. A memory of her “childhood”\""
    show turbo pose2 at turbo_2_up, left, unfocus

    show barista no_cup at barista_2_up, right, focus
    barista "\"Oooookay then. Haveanicedaybye!\""
    show barista no_cup at barista_2_up, easeout

    "She sets down the drink and hurries off. Turbo is clearly creeping her out."
    show turbo pose2 at turbo_2_up, move_center_from_left
    hide barista
    "Hell he’s creeping me out."
    "Does Iris know this guy? He’s downright concerning."
    show turbo at turbo_2_up, easeout
    "Looks like he’s leaving."
    hide turbo
    "I’d better sneak out as well. Don’t want to risk bumping into him by accident."

    if not scene_5d_completed:
        $ add_personal_diary_page(PERSONAL_DIARY_PAGE_9)
    jump scene_5d_ending

label scene_5d_ending:
    $ scene_5d_completed = True
    if not first_diary_visit_completed:
        call scene_transition ("scene_4a") from _call_scene_transition_48
    elif cafe_visited and office_visited and library_visited and not iris_home_visited:
        call scene_transition ("scene_4c_map_short_intro") from _call_scene_transition_49
    elif True:
        call scene_transition from _call_scene_transition_50
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
