init python:
    import copy
    global extra_w2_diary_pages, dollar_active_field_limits, DEFAULT_FILE_ERROR_MESSAGE, FILE_IS_ENCRYPTED_ERROR_MESSAGE, personal_diary_pages, CAFE_REQUIRED_FIELDS, object_class_name_mappings, REQUIRED_FIELDS,  DEFAULT_1099_INT_DIARY_PAGE, ADDRESS_VALUES, WHAT_CHOICE, INCOME_TYPE_CHOICES, INT_1099_CHOICE, OTHER_FORMS_CHOICE, FILING_SINGLY_CHOICE, MARRIED_FILING_JOINTLY_CHOICE, SURVIVING_SPOUSE_CHOICE, HOH_CHOICE, NAME_VALUES, TWO_YEARS_PRIOR, START_NEW_GAME_MESSAGE, DUMMY_LAST_NAME, STANDARD_CHOICES, us_states, TAX_YEAR, PREVIOUS_TAX_YEAR, NEXT_TAX_YEAR, W2_FORM_CHOICES, YES_OR_NO_CHOICES, NUMBER_OF_PAGE_FLIP_SOUNDS, ATTENDANCE_STATUS_CHOICES, FULL_TIME_CHOICE, HALF_TIME_CHOICE, LESS_THAN_HALF_CHOICE, ELIGIBILITY_CHOICES, REFUND_CHOICES, ALL_CHOICE, SOME_CHOICE, BANK_ACCOUNT_TYPE_CHOICES, CHECKING_CHOICE, SAVINGS_CHOICE, DEPENDENT_CLAIMER_VALUES, VALUE_DISPLAY_NAMES, SCHOOL_1_ADDRESS_VALUES, SCHOOL_0_ADDRESS_VALUES, MAX_IRA_CONTRIBUTION_UNDER_50, MAX_IRA_CONTRIBUTION_50_OR_OVER, DEFAULT_W2_DIARY_PAGE, STATIC_INCOME_DIARY_PAGES_0, DEFAULT_1099_INT_DIARY_PAGE, SUMMARY_PAGES_1099_INT, DEFAULT_1099_G_DIARY_PAGE, SUMMARY_PAGES_1099_G, STATIC_INCOME_DIARY_PAGES_1, diary_field_section_page_mapping, FILING_STATUS_CHOICES, diary_sections, banking_diary_pages, refund_pages, educator_expenses_pages, excess_social_security_pages, earned_income_credit_pages, edu_final_pages, edu_school_pages, aoc_refundable_pages, aoc_screener_pages, edu_eligibility_pages, diary_pages_1099_g, ssa_1099_pages, diary_pages_1099_int, diary_pages_w2, DEFAULT_DIARY_SECTIONS, BOX_12_CHOICES, BOX_12_RED_CHOICE, BOX_12_YELLOW_CHOICE, BOX_12_GREEN_CHOICE, BOOKS_TO_CHOOSE_FROM
    TAX_YEAR = "2022"
    PREVIOUS_TAX_YEAR = str(int(TAX_YEAR) - 1)
    TWO_YEARS_PRIOR = str(int(TAX_YEAR) - 2)
    NEXT_TAX_YEAR = str(int(TAX_YEAR) + 1)
    MAX_IRA_CONTRIBUTION_UNDER_50 = 6000
    MAX_IRA_CONTRIBUTION_50_OR_OVER = 7000
    DUMMY_LAST_NAME = "CAFE"
    DEFAULT_FILE_ERROR_MESSAGE = "Something went wrong, please try again."
    FILE_IS_ENCRYPTED_ERROR_MESSAGE = "File could not be read. Please try another."
    object_class_name_mappings = {}

    dollar_active_field_limits = {
        'household_empoloyee_wages_not_reported_on_w2': 1900,
        'educator_expenses': 300,
        'student_loan_interest': 2500
    }

    START_NEW_GAME_MESSAGE = "Are you sure you want to start a new game?\n\nAny data associated with your current saved game will be permanently lost."

    STANDARD_CHOICES = [
        {
            "display": "Yes",
            "value": True
        },
        {
            "display": "No",
            "value": False
        },
        {
            "display": "What?!",
            "value": "what"
        }
    ]


    LESS_THAN_HALF_CHOICE = "less_than_half"
    FULL_TIME_CHOICE = "full_time"
    HALF_TIME_CHOICE = "half_time"

    BANK_ACCOUNT_TYPE_CHOICES = [
        {
            "display": "Checking",
            "value": True
        },
        {
            "display": "Savings",
            "value": False
        }
    ]

    ATTENDANCE_STATUS_CHOICES = [
        {
            "display": "I was enrolled less than half the time",
            "value": LESS_THAN_HALF_CHOICE
        },
        {
            "display": "I was enrolled half-time",
            "value": HALF_TIME_CHOICE
        },
        {
            "display": "I was enrolled full time!",
            "value": FULL_TIME_CHOICE
        }
    ]

    ATTENDANCE_STATUS_CHOICES_DIARY = [
        {
            "display": "Less than half time",
            "value": LESS_THAN_HALF_CHOICE
        },
        {
            "display": "Half time or more",
            "value": HALF_TIME_CHOICE
        },
        {
            "display": "Full time",
            "value": FULL_TIME_CHOICE
        }
    ]

    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "email"]
    CAFE_REQUIRED_FIELDS = ["birth_date", "occupation", "social_security_number", "is_blind", "someone_can_claim_as_dependent"]

    BOX_12_RED_CHOICE = "error"

    BOX_12_YELLOW_CHOICE = "warning"

    BOX_12_GREEN_CHOICE = "ok"

    BOX_12_CHOICES = [
        {
            "display": "One or more of: A, B, K, L, M, N, P, R, T, V, W, Y, or Z",
            "value": BOX_12_RED_CHOICE
        },
        {
            "display": "One or more of: D, E, F, G, H, S, AA, BB, or EE",
            "value": BOX_12_YELLOW_CHOICE
        },
        {
            "display": "One or more of: C, J, Q, DD, FF, GG, or HH",
            "value": BOX_12_GREEN_CHOICE
        }
    ]




    CONTACT_DETAILS_PAGE_ID = "contact_details"
    DEPDENDENCY_PAGE_ID = "depdendency"
    FIRST_W2_PAGE_ID = "w2_1"
    SECOND_W2_PAGE_ID = "w2_2"
    THIRD_W2_PAGE_ID = "w2_3"
    W2_SUMMARY_PAGE_ID = "w2_summary"
    INT_1099_SCREENER_PAGE_ID = "1099_int_screener"
    FIRST_INT_1099_PAGE_ID = "1099_int_1"
    SECOND_INT_1099_PAGE_ID = "1099_int_2"
    ADDITIONAL_INT_1099_SCREENER_PAGE_ID = "1099_int_addtl_screener"
    SSA_1099_SCREENER_PAGE_ID = "ssa_1099_screener"
    G_1099_SCREENER_PAGE_ID = "1099_g_screener"
    G_1099_PAGE_ID = "1099_g"
    STUDENT_STATUS_PAGE_ID = "student_status"
    AOC_SCREENER_PAGE_ID = "aoc_screener_page"
    AOC_REFUNDABLE_RESULTS_PAGE_ID = "aoc_refundable_results"
    FIRST_SCHOOL_PAGE_ID = "edu_credit_school_1"
    SECOND_SCHOOL_PAGE_ID = "edu_credit_school_2"
    QUALIFIED_EDU_EXPENSES_PAGE_ID = "qualified_edu_expenses"
    EDU_CREDIT_SUMMARY_PAGE_ID = "edu_credit_summary"
    EIC_PAGE_ID = "eic"
    EXCESS_SS_PAGE_ID = "excess_ss"
    EDUCATOR_EXPENSE_PAGE_ID = "educator_expenses"
    STUDENT_LOAN_PAGE_ID = "student_loan"
    IRA_CONTRIBUTION_PAGE_ID = "ira_contribution"
    REFUND_OVERVIEW = "refund_overview"
    BANKING_INFO = "banking_info"





    PERSONAL_DIARY_PAGE_0 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "Today when I woke up I had orange juice and an English muffin with raspberry jam. I have never had raspberry jam before, and I liked it more than grape jelly, but not as much as orange marmalade. I re-read yesterday's diary entry to confirm I remembered everything accurately.",
                "background": "gui/diary/page_backgrounds/personal_0_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "I ran out of patterned tape, so at 10:36am I left to go to the store. While walking on the sidewalk I passed two inhabitants of the town. I purchased three rolls of tape for a total $7.65: one strawberry patterned, one dotted, and one floral. While exiting the store I walked headlong into someone standing outside!",
                "background": "gui/diary/page_backgrounds/personal_0_1.webp"
            }
        ]
    }

    personal_diary_pages = [PERSONAL_DIARY_PAGE_0]

    PERSONAL_DIARY_PAGE_1 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "Sometimes, when I take the bus to the library, I find myself pretending the other riders are my family members. I never knew my family, Diary, not really, so this is the second-best thing. Today I imagined a man in a bolo tie was my Uncle Rocky. I think it’s a good name for an uncle, especially one in a bolo tie.",
                "background": "gui/diary/page_backgrounds/personal_1_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "Today I tried coffee. I found it a bit boring. But they have all kinds of things behind the counter to put in it, so I tried all of them! It reminded me of the food we used to drink at T.T. Sometimes I get nostalgic for those things even though I’m glad I got out.\n\nIs that bad?",
                "background": "gui/diary/page_backgrounds/personal_1_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_2 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "I met a friend today! I’ve begun creating a comprehensive record of our interactions. There was something different about this person. Sure, they seem a little more clueless than average, but I found it charming.",
                "background": "gui/diary/page_backgrounds/personal_2_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "This all makes me nervous, of course. Having more to care about means having more to lose if TT should ever find out.",
                "background": "gui/diary/page_backgrounds/personal_2_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_3 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "Diary, how far into the future do you think most people can imagine? And how far back can they remember? Today I watched the girls on the bus drinking iced coffee even though it’s not allowed. I think that’s what it means to be human, more than anything.",
                "background": "gui/diary/page_backgrounds/personal_3_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "Diary, today I tried a makeup tutorial. It went quite badly, I must say. No matter how much I try to calculate the perfect ratio of blush to gloss, it always seems wrong. I don’t recognize the face looking back at me!\n\nI just want to look like the girls on the bus. Normal girls. They’re always laughing and having fun. I think finding the perfect foundation will make me happy like that, too.",
                "background": "gui/diary/page_backgrounds/personal_3_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_4 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "Diary. Today I saw a CAT!",
                "background": "gui/diary/page_backgrounds/personal_4_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "People always look at me strangely when I ask them for their address and social security number. Finally, today, someone said to me that it’s not polite. If I’ve just met someone I should only ask “what’s your name?”\n\nDiary, it’s very hard only knowing about one thing. I’m always having to ask people to help me. Maybe one day I will be able to help someone.",
                "background": "gui/diary/page_backgrounds/personal_4_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_5 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "Do you know that birthdays have meanings? People remember them and also say their birth date says something about their personalities. I wish I had one. No one ever mentioned birthdays in the lab. Maybe I can make one up?",
                "background": "gui/diary/page_backgrounds/personal_5_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "At the park today I saw a child who was riding the bus for the first time.\n\nThere are so many foods I’ve never tried. There are so many firsts I haven’t had. What’s the earliest memory that I can remember? I know things from earlier than my notebook, from before I got out. But when did it start?",
                "background": "gui/diary/page_backgrounds/personal_5_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_6 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "I saw a commercial for them today. They lie so much, Diary! “File your taxes for free!” But it’s never free with them. And it would be free for everyone if it WASN’T for them.\n\nIt makes me so angry!\n\nWait.\n\nI feel angry.\n\nDiary… \n\nI FEEL. I FEEL angry!",
                "background": "gui/diary/page_backgrounds/personal_6_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "I went down by the riverbank today, Diary. I saw a tortoise. I’ve never seen a tortoise before, but it’s just like a turtle.\n\nIt got flipped over on its back and was stuck, waving its goofy little legs. But I helped it, Diary! I flipped it back over and it scooted away.",
                "background": "gui/diary/page_backgrounds/personal_6_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_7 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "It’s so hard learning how to live on my own. Everything here is so different from in the lab. I didn’t realize how much T.T. hid from me, and how much they provided.\n\nI’ll never go back.\n\nBut I never knew how hard it would be to use a washing machine, or put a bed frame together.",
                "background": "gui/diary/page_backgrounds/personal_7_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "T.T. always did everything, all I had to focus on was learning what they wanted me to…\n\nThey would have taught me eventually, right? They wanted me to spread their messages, so they would have introduced me to the world at some point.",
                "background": "gui/diary/page_backgrounds/personal_7_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_8 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "I wish there was a simple math calculation to determine how much you should tell a person. Do you think my friend would understand, Diary?",
                "background": "gui/diary/page_backgrounds/personal_8_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "How was I made, Diary? Not the normal way.\n\nBut now when I read about love, and families, I understand what the books talk about. Can I be like that?",
                "background": "gui/diary/page_backgrounds/personal_8_1.webp"
            }
        ]
    }

    PERSONAL_DIARY_PAGE_9 = {
        "sections": [
            {
                "display": None,
                "fields": [],
                "diary_entry": "I stopped by a new store today when I was walking down to Mulberry Press. Diary, it was incredible. They call it a hardware store. I saw an ax, and a hose, and a little camping stove, and so many other things that it took me months to find when I was in T.T.\n\nIf I ever have to get out again it will be so much easier.",
                "background": "gui/diary/page_backgrounds/personal_9_0.webp"
            },
            {
                "display": None,
                "fields": [],
                "diary_entry": "I went to the bank today, Diary. I think I understand what my target was now. All the buildings they showed me looked like that.\n\nOr maybe there’s a city somewhere where all the buildings look like banks.\n\nIf I go there, how many people will be like me? Will anyone know?",
                "background": "gui/diary/page_backgrounds/personal_9_1.webp"
            }
        ]
    }





    DEFAULT_W2_DIARY_PAGE = {
        "sections": [
            {
                "display": None,
                "fields": [
                    {
                        "display": "W-2",
                        "value_name": "w2_objects",
                        "type": "file_empty",
                        "prefix": None,
                        "value_type": None,
                        "changed_function": None,
                        "description": None,
                        "pdf_type": "W2"
                    }
                ]
            }
        ]
    }
    diary_pages_w2 = [DEFAULT_W2_DIARY_PAGE]

    def create_1099_int_page(idx):
        background_index = idx % 2
        page_id = FIRST_INT_1099_PAGE_ID if idx == 0 else SECOND_INT_1099_PAGE_ID
        page = {
            "id": page_id,
            "sections": [
                {
                    "background": f"gui/diary/page_backgrounds/diary_page_1099_int_{background_index}.webp",
                    "display": f"1099-INT #{idx + 1} INCOME",
                    "fields": [
                        {
                            "display": "Payer name",
                            "value_name": f"int_1099_objects[{idx}].payer_name",
                            "type": "input",
                            "prefix": None,
                            "value_type": "arr_prop_string",
                            "changed_function": "validate_and_save_active_input_required_array_property"
                        },
                        {
                            "display": "Total interest income (1099-INT box 1)",
                            "value_name": f"int_1099_objects[{idx}].total_interest",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "arr_prop_number",
                            "changed_function": "validate_and_save_dollar_active_field_array_property"
                        },
                        {
                            "display": "Tax exempt interest income (1099-INT box 8)",
                            "value_name": f"int_1099_objects[{idx}].tax_exempt_interest",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "arr_prop_number",
                            "changed_function": "validate_and_save_dollar_active_field_array_property"
                        },
                        {
                            "display": "Federal income tax witheld (1099-INT box 4)",
                            "value_name": f"int_1099_objects[{idx}].federal_income_tax_witheld",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "arr_prop_number",
                            "changed_function": "validate_and_save_dollar_active_field_array_property"
                        }
                    ]
                },
                {
                    "display": None,
                    "fields": [
                        {
                            "display": "Taxable interest",
                            "value_name": f"int_1099_objects[{idx}].total_interest",
                            "type": "static",
                            "prefix": None,
                            "value_type": "arr_prop_number",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
        if len(int_1099_objects) < 2 and idx == 0:
            page["sections"][1].update(
                {
                    "stickies": {
                        "add": {
                            "value_name": "int_1099_objects",
                            "value_type": "Int1099",
                            "display": "1099-INT",
                            "index": idx
                        }
                    }
                }
            )
        else:
            page["sections"][1].update(
                {
                    "stickies": {
                        "add": {
                            "value_name": "int_1099_objects",
                            "value_type": "Int1099",
                            "display": "1099-INT",
                            "index": idx
                        },
                        "remove": {
                            "value_name": "int_1099_objects",
                            "value_type": "Int1099",
                            "index": idx,
                            "display": "1099-INT"
                        }
                    }
                }
            )
        return page

    EARNED_INCOME_HALF_OF_SUPPORT_PAGE_1099_INT = {
        "id": ADDITIONAL_INT_1099_SCREENER_PAGE_ID,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_9.webp",
                "display": "ADDITIONAL INCOME INFORMATION",
                "fields": [
                    {
                        "display": "In 2022, was {}'s earned income at least half of their support?",
                        "value_name": "interest_income_earned_income_half_of_support",
                        "type": "checkbox",
                        "prefix": None,
                        "value_type": "bool",
                        "changed_function": None
                    }
                ]
            },
            {
                "background": "gui/diary/page_backgrounds/diary_page_9_filler.webp",
                "display": None,
                "fields": []
            }
        ]
    }

    EARNED_INCOME_HALF_OF_SUPPORT_AND_FULL_TIME_STUDENT_1099_INT_PAGE = {
        "id": ADDITIONAL_INT_1099_SCREENER_PAGE_ID,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_9.webp",
                "display": "ADDITIONAL INCOME INFORMATION",
                "fields": [
                    {
                        "display": "Was {} a full time student in 2022, for at least one academic term?",
                        "value_name": "was_full_time_student_one_term",
                        "type": "checkbox",
                        "prefix": None,
                        "value_type": "bool",
                        "changed_function": None
                    },
                    {
                        "display": "In 2022, was {}'s earned income at least half of their support?",
                        "value_name": "interest_income_earned_income_half_of_support",
                        "type": "checkbox",
                        "prefix": None,
                        "value_type": "bool",
                        "changed_function": None
                    }
                ]
            },
            {
                "background": "gui/diary/page_backgrounds/diary_page_9_filler.webp",
                "display": None,
                "fields": []
            }
        ]
    }

    SUMMARY_PAGES_1099_INT = [
        {
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_1099_int_2.webp",
                    "display": "1099-INT INCOME SUMMARY",
                    "fields": [
                        {
                            "display": "2022 total taxable interest income",
                            "value_name": "form_1040_line_2b",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "string",
                            "changed_function": None
                        },
                        {
                            "display": "2022 total tax exempt interest income",
                            "value_name": "form_1040_line_2a",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "string",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ]
    diary_pages_1099_int = []
    DEFAULT_1099_G_DIARY_PAGE = {
        "sections": [
            {
                "display": None,
                "fields": [
                    {
                        "display": "1099-G",
                        "value_name": "unemployment_1099g_file_location",
                        "type": "file_empty",
                        "prefix": None,
                        "value_type": None,
                        "changed_function": None,
                        "description": None,
                        "pdf_type": "PDF"
                    }
                ]
            }
        ]
    }
    diary_pages_1099_g = []

    EXTRA_W2_DIARY_PAGE_WITHOUT_WARNING = {
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_17.webp",
                "display": "HOUSEHOLD WAGES",
                "fields": [
                    {
                        "display": "Household employee wages not reported on Form(s) W-2",
                        "value_name": "household_empoloyee_wages_not_reported_on_w2",
                        "type": "input",
                        "prefix": "$",
                        "value_type": "number",
                        "changed_function": "validate_and_save_dollar_active_field_less_than_limit"
                    }
                ]
            },
            {
                "display": None,
                "fields": [
                    {
                        "display": "Did any of the following codes appear in box 12 of any of {}'s W-2 forms?\n\nA, B, K, L, M, N, P, R, T, V, W, Y, Z",
                        "value_name": "has_unsupported_box_12_codes",
                        "type": "checkbox",
                        "prefix": None,
                        "value_type": "bool",
                        "changed_function": None
                    }
                ]
            }
        ]
    }

    EXTRA_W2_DIARY_PAGE_WITH_WARNING = copy.deepcopy(EXTRA_W2_DIARY_PAGE_WITHOUT_WARNING)
    EXTRA_W2_DIARY_PAGE_WITH_WARNING["sections"][1]["fields"].append(
        {
            "display": "Note: if code D, E, F, G, H, S, AA, BB, or EE appeared in box 12 of any of their W-2 forms, {} may be eligible for additional tax credits that are not being checked for.",
            "value_name": None,
            "type": "plaintext",
            "prefix": None,
            "value_type": None,
            "changed_function": None,
        }
    )

    extra_w2_diary_pages = [EXTRA_W2_DIARY_PAGE_WITHOUT_WARNING]

    STATIC_INCOME_DIARY_PAGES_0 = [           
        {   
            "id": W2_SUMMARY_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_5.webp",
                    "display": "W-2 INCOME SUMMARY",
                    "fields": [
                        {
                            "display": "2022 total W-2 income",
                            "value_name": "form_1040_line_1a",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": "validate_and_save_dollar_active_field"
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_w2_summary_filler.webp",
                    "fields": [],
                    "display": None
                }
            ]
        },
        {   
            "id": INT_1099_SCREENER_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_7.webp",
                    "display": "GENERAL 1099-INT INCOME INFO",
                    "fields": [
                        {
                            "display": "Did {} receive any Form 1099-INTs for 2022?",
                            "value_name": "has_income_interest",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool"
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_8.webp",
                    "fields": [],
                    "display": None
                }
            ]
        }
    ]

    SSA_1099_DIARY_PAGES = [
        {   
            "id": SSA_1099_SCREENER_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_10.webp",
                    "display": "GENERAL SSA-1099 INCOME INFO",
                    "fields": [
                        {
                            "display": "Did {} receive a Form SSA-1099 for 2022?",
                            "value_name": "has_social_security_benefits",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool"
                        }
                    ]
                }
            ]
        },
    ]

    ssa_1099_pages = SSA_1099_DIARY_PAGES

    HAS_SSA_1099_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_11.webp",
        "display": "GENERAL SSA-1099 INCOME",
        "background_image": "",
        "fields": [
            {
                "display": "Income from Social Security benefits (SSA-1099 box 5)",
                "value_name": "social_security_taxable_amount",
                "type": "input",
                "prefix": "$",
                "value_type": "number",
                "changed_function": "validate_and_save_dollar_active_field"
            },
            {
                "display": "Taxable portion of 2022 Social Security benefits",
                "value_name": "form_1040_line_6b",
                "type": "static",
                "prefix": "$",
                "value_type": "number",
                "changed_function": None
            }
        ]
    }

    STATIC_INCOME_DIARY_PAGES_1 = [
        {
            "id": G_1099_SCREENER_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_13.webp",
                    "display": "GENERAL 1099-G INCOME INFO",
                    "fields": [
                        {
                            "display": "Did {} receive a 1099-G for 2022?",
                            "value_name": "has_unemployment_compensation",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool"
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_14.webp",
                    "display": None,
                    "fields": []
                }
            ]
        }
    ]


    STATIC_CREDITS_PAGES_0 = [
        {   
            "id": STUDENT_STATUS_PAGE_ID,
            "sections": [
                {
                    "display": "STUDENT STATUS",
                    "fields": [
                        {
                            "display": "In 2022, was {} a student enrolled at an eligible educational institution?",
                            "value_name": "was_a_student",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        },
                        {
                            "display": "In 2022, did {} pay tuition or other qualified education expenses for an academic period beginning in 2022, or beginning in the first three months of 2023?",
                            "value_name": "paid_tuition_or_qualified_expenses",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        },
                        {
                            "display": "In 2022, was {} pursuing a program leading to a degree or other recognized education credential?",
                            "value_name": "aoc_pursued_a_program_leading_to_degree",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        }
                    ]
                }, 
                {
                    "background": "gui/diary/page_backgrounds/diary_page_16.webp",
                    "display": None,
                    "fields": [
                        {
                            "display": "For at least one academic period in 2022, what was {}'s enrollment status?",
                            "value_name": "student_status",
                            "type": "checkbox",
                            "options": ATTENDANCE_STATUS_CHOICES_DIARY,
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ]

    AOC_SCREENER_PAGES = [
        {
            "id": AOC_SCREENER_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_17.webp",
                    "display": "APPLICABLE EDUCATIONAL CREDIT",
                    "fields": [
                        {
                            "display": "Has {} claimed the American Opportunity Credit for any four previous tax years?",
                            "value_name": "aoc_claimed_last_four_years",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        },
                        {
                            "display": "At the start of 2022, had {} already completed the first four years of their postsecondary education?",
                            "value_name": "aoc_first_four_years_completed_before_this_year",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        }
                    ]
                },
                {
                    "display": None,
                    "fields": [
                        {
                            "display": "At the end of 2022, did {} have a felony drug conviction for possessing or distributing a controlled substance?",
                            "value_name": "aoc_has_been_convicted",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        },
                        {
                            "display": None,
                            "value_name": None,
                            "type": "results_edu_credit_option",
                            "prefix": None,
                            "value_type": None,
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ]


    AOC_REFUNDABLE_ELIGIBLE_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_18.webp",
        "display": None,
        "fields": [
            {
                "display": "{} is eligible to claim the American Opportunity Credit and is eligible to receive up to 40% of it as a refundable credit!",
                "value_name": None,
                "type": "results_text",
                "prefix": None,
                "value_type": None,
                "changed_function": None
            }
        ]
    }

    AOC_REFUNDABLE_INELIGIBLE_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_18.webp",
        "display": None,
        "fields": [
            {
                "display": "{} is eligible to claim the American Opportunity Credit but cannot claim any part of it as a refundable credit.",
                "value_name": None,
                "type": "results_text",
                "prefix": None,
                "value_type": None,
                "changed_function": None
            }
        ]
    }

    EARNED_INCOME_FIELD = {
        "display": "In 2022, was {}'s earned income at least half of their support?",
        "value_name": "aoc_refundable_earned_income_half_of_support",
        "type": "checkbox",
        "prefix": None,
        "value_type": "bool",
        "changed_function": None
    }

    PARENTS_ALIVE_FIELD = {
        "display": "At the end of 2022, was one or both of {}'s parents alive?",
        "value_name": "aoc_refundable_parents_alive",
        "type": "checkbox",
        "prefix": None,
        "value_type": "bool",
        "changed_function": None
    }

    AOC_REFUNDABLE_ELIGIBLE_SECTION_WITH_DISPLAY = copy.deepcopy(AOC_REFUNDABLE_ELIGIBLE_SECTION)
    AOC_REFUNDABLE_ELIGIBLE_SECTION_WITH_DISPLAY.update({"display": "REFUNDABLE CREDIT STATUS"})

    AOC_REFUNDABLE_ELIGIBLE_OVER_24_PAGES = [
        {
            "id": AOC_REFUNDABLE_RESULTS_PAGE_ID,
            "sections": [
                AOC_REFUNDABLE_ELIGIBLE_SECTION_WITH_DISPLAY,
                {
                    "background": "gui/diary/page_backgrounds/diary_page_19.webp",
                    "display": None,
                    "fields": []
                }
            ]
        }
    ]

    AOC_REFUNDABLE_ELIGIBLE_UNDER_18_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_20.webp",
        "display": "REFUNDABLE CREDIT STATUS",
        "fields": [PARENTS_ALIVE_FIELD]
    }

    AOC_REFUNDABLE_BETWEEN_18_AND_24_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_21.webp",
        "display": "REFUNDABLE CREDIT STATUS",
        "fields": [EARNED_INCOME_FIELD, PARENTS_ALIVE_FIELD]
    }

    def generate_school_page(idx):
        page_id = FIRST_SCHOOL_PAGE_ID if idx == 0 else SECOND_SCHOOL_PAGE_ID
        edu_school_page = {
            "id": page_id,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_23.webp",
                    "display": f"SCHOOL #{idx + 1} INFORMATION",
                    "fields": [
                        {
                            "display": "Name of first education institution",
                            "value_name": f"aoc_schools[{idx}].name",
                            "type": "input",
                            "prefix": None,
                            "value_type": "arr_prop_string",
                            "changed_function": "validate_and_save_active_input_required_array_property"
                        },
                        {
                            "display": "Did {} receive a form 1098-T from this institution in 2022?",
                            "value_name": f"aoc_schools[{idx}].did_receive_1098t_this_year",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "arr_prop_bool",
                            "changed_function": None
                        },
                        {
                            "display": "Did {} receive a form 1098-T from this institution for 2021 with box 7 checked?",
                            "value_name": f"aoc_schools[{idx}].did_receive_1098t_previous_year_box_7",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "arr_prop_bool",
                            "changed_function": None
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_aoc_school.webp",
                    "display": None,
                    "fields": [
                        {
                            "display": "EIN of School",
                            "value_name": f"aoc_schools[{idx}].ein",
                            "type": "input",
                            "prefix": None,
                            "value_type": "arr_prop_string",
                            "changed_function": "validate_and_save_ein_active_field_array_prop"
                        },
                        {
                            "display": "Address of school",
                            "value_name": f"aoc_schools[{idx}]",
                            "type": "address_input",
                            "prefix": None,
                            "value_type": "arr_prop",
                            "changed_function": None
                        }
                    ]
                },

            ]

        }
        
        return edu_school_page

    EDU_SCHOOL_PAGE_1 = generate_school_page(0)
    EDU_SCHOOL_PAGE_2 = generate_school_page(1)

    AOC_SUMMARY_PAGE = {
        "id": EDU_CREDIT_SUMMARY_PAGE_ID,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_26.webp",
                "display": "SUMMARY OF EDUCATIONAL CREDITS",
                "fields": [
                    {
                        "display": "{} is eligible to claim an American Opportunity Credit of",
                        "value_name": "education_tax_credit",
                        "type": "static",
                        "prefix": "$",
                        "value_type": "number",
                        "changed_function": None
                    }
                ]
            },
            {
                "background": "gui/diary/page_backgrounds/diary_page_27.webp",
                "display": None,
                "fields": []
            }
        ]
    }

    LLLC_SUMMARY_PAGE = {
        "id": EDU_CREDIT_SUMMARY_PAGE_ID,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_26.webp",
                "display": "SUMMARY OF EDUCATIONAL CREDITS",
                "fields": [
                    {
                        "display": "{} is eligible to claim a Lifetime Learning Credit of",
                        "value_name": "education_tax_credit",
                        "type": "static",
                        "prefix": "$",
                        "value_type": "number",
                        "changed_function": None
                    }
                ]
            },
            {
                "background": "gui/diary/page_backgrounds/diary_page_27.webp",
                "display": None,
                "fields": []
            }
        ]
    }

    STATIC_CREDITS_PAGES_1_AOC = [
        {
            "id": QUALIFIED_EDU_EXPENSES_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_24.webp",
                    "display": "QUALIFIED EDUCATION EXPENSES",
                    "fields": [
                        {
                            "display": "{}’s total qualified education expenses in 2022",
                            "value_name": "aoc_qualified_educational_expenses",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": "validate_and_save_dollar_active_field_less_than_4000"
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_25.webp",
                    "display": None,
                    "fields": []
                }
            ]

        }
    ]

    STATIC_CREDITS_PAGES_1_LLLC = [
        {
            "id": QUALIFIED_EDU_EXPENSES_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_24.webp",
                    "display": "QUALIFIED EDUCATION EXPENSES",
                    "fields": [
                        {
                            "display": "{}’s total qualified education expenses in 2022",
                            "value_name": "aoc_qualified_educational_expenses",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": "validate_and_save_dollar_active_field_less_than_10000"
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_25.webp",
                    "display": None,
                    "fields": []
                }
            ]

        }
    ]

    edu_eligibility_pages = []
    aoc_screener_pages = []
    aoc_refundable_pages = []
    edu_school_pages = []
    edu_final_pages = []

    EARNED_INCOME_CREDIT_PAGES = [
        {
            "id": EIC_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_28.webp",
                    "display": "EARNED INCOME TAX CREDIT",
                    "fields": [
                        {
                            "display": "Was {}'s main home in the United States for 50% or more of 2022?",
                            "value_name": "resided_in_us_for_more_than_half_the_year",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        },
                        {
                            "display": "Did {} have any nontaxable combat pay in 2022?",
                            "value_name": "had_nontaxable_combat_pay",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_29.webp",
                    "display": None,
                    "fields": [
                        {
                            "display": "Earned Income Tax Credit amount",
                            "value_name": "form_1040_line_27",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "string",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ]
    earned_income_credit_pages = []

    NONTAXABLE_COMBAT_PAY_FIELD = {
        "display": "Amount of {}'s 2022 nontaxable combat pay",
        "value_name": "nontaxable_combat_pay_election",
        "type": "input",
        "prefix": "$",
        "value_type": "number",
        "changed_function": "validate_and_save_dollar_active_field"
    }


    EXCESS_SOCIAL_SECURITY_PAGES = [
        {
            "id": EXCESS_SS_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_30.webp",
                    "display": "EXCESS SOCIAL SECURITY TAX WITHELD",
                    "fields": [
                        {
                            "display": "{}'s total social security tax paid in 2022",
                            "value_name": "w2_box_4_totals",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": None
                        },
                        {
                            "display": "2022 maximum social security tax applicable",
                            "value_name": "max_social_security_tax_this_year",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": None
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_31.webp",
                    "display": None,
                    "fields": [
                        {
                            "display": "{}'s refundable excess social security withheld in 2022",
                            "value_name": "form_schedule3_line_11",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ]
    excess_social_security_pages = []

    EARNED_INCOME_CREDIT_PAGES_WITH_NONTAXABLE_COMBAT_PAY_INPUT = copy.deepcopy(EARNED_INCOME_CREDIT_PAGES)
    EARNED_INCOME_CREDIT_PAGES_WITH_NONTAXABLE_COMBAT_PAY_INPUT[0]["sections"][0]["fields"].append(NONTAXABLE_COMBAT_PAY_FIELD)

    EDUCATOR_EXPENSE_SCREENER_PAGE = {
        "id": EDUCATOR_EXPENSE_PAGE_ID,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_32.webp",
                "display": "EDUCATOR EXPENSE DEDUCTION",
                "fields": [
                    {
                        "display": "{} was a qualified educator at a qualified school, and taught at least 900 hours in the 2022 school year",
                        "value_name": "has_educator_expenses",
                        "type": "checkbox",
                        "prefix": None,
                        "value_type": "bool",
                        "changed_function": None
                    }
                ]
            }
        ]
    }


    EDUCATOR_EXPENSE_VALUES_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_33.webp",
        "display": None,
        "fields": [
                {
                    "display": "{}’s 2022 qualified educator expenses",
                    "value_name": "educator_expenses",
                    "type": "input",
                    "prefix": "$",
                    "value_type": "number",
                    "changed_function": "validate_and_save_dollar_active_field_less_than_equal_to_limit"
                },
                {
                    "display": "{}’s 2022 educator expense deduction",
                    "value_name": "form_schedule1_line_11",
                    "type": "static",
                    "prefix": "$",
                    "value_type": "number",
                    "changed_function": "validate_and_save_dollar_active_field"
                }
        ]
    }

    EDUCATOR_EXPENSE_VALUES_PAGE = copy.deepcopy(EDUCATOR_EXPENSE_SCREENER_PAGE)
    EDUCATOR_EXPENSE_VALUES_PAGE["sections"].append(EDUCATOR_EXPENSE_VALUES_SECTION)

    educator_expenses_pages = []


    STUDENT_LOAN_SCREENER_PAGE = {
        "id": STUDENT_LOAN_PAGE_ID,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_34.webp",
                "display": "STUDENT LOAN PAYMENT DEDUCTION",
                "fields": [
                    {
                        "display": "{} paid interest on a qualified student loan in 2022?",
                        "value_name": "has_student_loan_interest",
                        "type": "checkbox",
                        "prefix": None,
                        "value_type": "bool",
                        "changed_function": None
                    }
                ]
            }
        ]
    }

    STUDENT_LOAN_VALUES_SECTION = {
        "background": "gui/diary/page_backgrounds/diary_page_35.webp",
        "display": None,
        "fields": [
                {
                    "display": "The total amount of interest {} paid on their student loan(s) in 2022",
                    "value_name": "student_loan_interest",
                    "type": "input",
                    "prefix": "$",
                    "value_type": "number",
                    "changed_function": "validate_and_save_dollar_active_field_less_than_equal_to_limit"
                },
                {
                    "display": "{}'s 2022 student loan interest deduction",
                    "value_name": "form_schedule1_line_21",
                    "type": "static",
                    "prefix": "$",
                    "value_type": "number",
                    "changed_function": None
                }
        ]
    }

    STUDENT_LOAN_VALUES_PAGE = copy.deepcopy(STUDENT_LOAN_SCREENER_PAGE)
    STUDENT_LOAN_VALUES_PAGE["sections"].append(STUDENT_LOAN_VALUES_SECTION)

    student_loan_pages = []

    IRA_CONRIBUTION_PAGES = [
        {
            "id": IRA_CONTRIBUTION_PAGE_ID,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_36.webp",
                    "display": "IRA CONTRIBUTION DEDUCTION",
                    "fields": [
                        {
                            "display": "{}'s total contribution to their traditional IRA in 2022",
                            "value_name": "tax_deferred_ira_contributions",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": "validate_and_save_ira_contribution_active_field"
                        },
                        {
                            "display": "Is {} covered by an employer sponsored retirement account?",
                            "value_name": "is_covered_by_employer_retirement_plan",
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_37.webp",
                    "display": None,
                    "fields": [
                        {
                            "display": "{}'s 2022 IRA deduction",
                            "value_name": "form_schedule1_line_20",
                            "type": "static",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ] 

    REFUND_OVERVIEW_PAGE = {
        "id": REFUND_OVERVIEW,
        "sections": [
            {
                "background": "gui/diary/page_backgrounds/diary_page_38.webp",
                "display": "REFUND OVERVIEW",
                "fields": [
                    {
                        "display": "Standard Deduction",
                        "value_name": "form_1040_line_12",
                        "type": "static",
                        "prefix": "$",
                        "value_type": "number",
                        "changed_function": None
                    },
                    {
                        "display": "Estimated tax payments already made in 2022",
                        "value_name": "estimated_tax_payments",
                        "type": "input",
                        "prefix": "$",
                        "value_type": "number",
                        "changed_function": "validate_and_save_dollar_active_field"
                    },
                    {
                        "display": "Amount from 2021 tax refund that {} chose to apply to this year's filing",
                        "value_name": "amount_applied_from_previous_year",
                        "type": "input",
                        "prefix": "$",
                        "value_type": "number",
                        "changed_function": "validate_and_save_dollar_active_field"
                    }
                ]
            }
        ]
    }
    refund_pages = []

    BANKING_DIARY_PAGES = [
        {
            "id": BANKING_INFO,
            "sections": [
                {
                    "background": "gui/diary/page_backgrounds/diary_page_40.webp",
                    "display": "BANKING INFORMATION",
                    "fields": [
                        {
                            "display": "Amount of refund {} wants refunded",
                            "value_name": "amount_to_be_refunded",
                            "type": "input",
                            "prefix": "$",
                            "value_type": "number",
                            "changed_function": "validate_and_save_dollar_active_field_less_than_refund_amount"
                        }
                    ]
                },
                {
                    "background": "gui/diary/page_backgrounds/diary_page_41.webp",
                    "display": None,
                    "fields": [
                        {
                            "display": "{}'s account number",
                            "value_name": "bank_account_number",
                            "type": "input",
                            "prefix": None,
                            "value_type": "string",
                            "changed_function": "validate_and_save_account_number"
                        },
                        {
                            "display": "{}'s routing number",
                            "value_name": "routing_number",
                            "type": "input",
                            "prefix": None,
                            "value_type": "string",
                            "changed_function": "validate_and_save_routing_number"
                        },
                        {
                            "display": "Type of account",
                            "value_name": "is_checking_account",
                            "options": BANK_ACCOUNT_TYPE_CHOICES,
                            "type": "checkbox",
                            "prefix": None,
                            "value_type": "bool",
                            "changed_function": None
                        }
                    ]
                }
            ]
        }
    ]

    banking_diary_pages = []

    diary_sections = [
        {
            "id": "first_page",
            "display": None,
            "pages": [
                {
                    "sections": [
                        {
                            "display": None,
                            "fields": []
                        }
                    ]
                }
            ]
        },
        {
            "id": "personal_entries",
            "display": None,
            "pages": personal_diary_pages
        },
        {
            "id": "personal_details",
            "display": "PERSONAL DETAILS",
            "pages": [
                { 
                    "id": CONTACT_DETAILS_PAGE_ID,  
                    "sections": [
                        {
                            "background": "gui/diary/page_backgrounds/diary_page_0.webp",
                            "display": "CONTACT DETAILS",
                            "fields": [
                                {
                                    "display": "First name",
                                    "value_name": "first_name",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "save_value_active_input_required"
                                },
                                {
                                    "display": "Middle name",
                                    "value_name": "middle_name",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "save_value_active_input"
                                },
                                {
                                    "display": "Last name",
                                    "value_name": "last_name",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "save_value_active_input_required"
                                },
                                {
                                    "display": "Phone number",
                                    "value_name": "phone_number",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "validate_and_save_phone_number"
                                },
                                {
                                    "display": "Email",
                                    "value_name": "email",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "validate_and_save_email"
                                }
                            ]
                        },
                        {
                            "background": "gui/diary/page_backgrounds/diary_page_1.webp",
                            "display": None,
                            "fields": [
                                {
                                    "display": "Residential Address",
                                    "value_name": "residential_address",
                                    "type": "address_input",
                                    "prefix": None,
                                    "value_type": "prop",
                                    "changed_function": None
                                }
                            ]
                        }
                    ]
                },
                {   
                    "id": DEPDENDENCY_PAGE_ID,
                    "sections": [
                        {
                            "background": "gui/diary/page_backgrounds/diary_page_2.webp",
                            "display": "DEPENDENCY",
                            "fields": [
                                {
                                    "display": "Can anyone else claim {} as a dependent?",
                                    "value_name": "someone_can_claim_as_dependent",
                                    "type": "checkbox",
                                    "prefix": None,
                                    "value_type": "bool"
                                }
                            ]
                        },
                        {
                            "background": "gui/diary/page_backgrounds/diary_page_3.webp",
                            "display": "PERSONAL DETAILS",
                            "fields": [
                                {
                                    "display": "{}'s birthday",
                                    "value_name": "birth_date",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "date",
                                    "changed_function": "validate_and_save_birth_date"
                                },
                                {
                                    "display": "Is {} blind?",
                                    "value_name": "is_blind",
                                    "type": "checkbox",
                                    "prefix": None,
                                    "value_type": "bool"
                                },
                                {
                                    "display": "{}'s occupation",
                                    "value_name": "occupation",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "save_value_active_input_required"
                                },
                                {
                                    "display": "{}'s social security number",
                                    "value_name": "social_security_number",
                                    "type": "input",
                                    "prefix": None,
                                    "value_type": "string",
                                    "changed_function": "validate_and_save_ssn"
                                },
                            ]
                        }
                    ]
                }
            ],
        },
        {
            "id": "income",
            "display": "INCOME",
            "pages": diary_pages_w2 + extra_w2_diary_pages + STATIC_INCOME_DIARY_PAGES_0 + diary_pages_1099_int + ssa_1099_pages + STATIC_INCOME_DIARY_PAGES_1 + diary_pages_1099_g
        },
        {
            "id": "credits_refund",
            "display": "CREDITS & REFUND",
            "pages": edu_eligibility_pages + aoc_screener_pages + aoc_refundable_pages + edu_school_pages + edu_final_pages + earned_income_credit_pages + excess_social_security_pages + educator_expenses_pages + IRA_CONRIBUTION_PAGES + refund_pages + banking_diary_pages
        }
    ]

    DEFAULT_DIARY_SECTIONS = diary_sections



    us_states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
        'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
        'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
        'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
        'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY' ]

    FILING_SINGLY_CHOICE = "single"
    MARRIED_FILING_JOINTLY_CHOICE = "married_filing_jointly"
    SURVIVING_SPOUSE_CHOICE = "surviving_spouse"
    HOH_CHOICE = "head_of_household"

    FILING_STATUS_CHOICES = [
        {
            "display": "I'm...filing singly, I guess",
            "value": FILING_SINGLY_CHOICE
        },
        {
            "display": "I'm married and filing jointly",
            "value": MARRIED_FILING_JOINTLY_CHOICE
        },
        {
            "display": "I'm filing as a qualified surviving spouse",
            "value": SURVIVING_SPOUSE_CHOICE
        },
        {
            "display": "I'm single but filing as head of household",
            "value": HOH_CHOICE
        }
    ]

    INT_1099_CHOICE = "1099-int"
    OTHER_FORMS_CHOICE = "other"
    WHAT_CHOICE = "what"

    INCOME_TYPE_CHOICES = [
        {
            "display": "Form W-2",
            "value": "w2"
        },
        {
            "display": "Form 1099-G",
            "value": "1099-g"
        },
        {
            "display": "Form SSA-1099",
            "value": "ssa-1099"
        },
        {
            "display": "Form 1099-INT",
            "value": INT_1099_CHOICE
        },
        {
            "display": "Any other form",
            "value": OTHER_FORMS_CHOICE
        },
        {
            "display": "What?",
            "value": WHAT_CHOICE
        }
    ]

    W2_FORM_CHOICES = [
        {
            "display": "I have one W-2 form",
            "value": False
        },
        {
            "display": "I have more than one W-2 form",
            "value": True
        },
        {
            "display": "Form what now?",
            "value": "what"
        }
    ]

    ELIGIBILITY_CHOICES = [
        {
            "display": "Okay! Let's find out if I'm eligible",
            "value": True
        },
        {
            "display": "No, I already know I'm not eligible",
            "value": False
        },
        {
            "display": "What are either of those?",
            "value": "what"
        }
    ]

    YES_OR_NO_CHOICES = [
        {
            "display": "Yes",
            "value": True
        },
        {
            "display": "No",
            "value": False
        }
    ]

    REFUND_CHOICES = [
        {
            "display": "All of it",
            "value": "all"
        },
        {
            "display": "Just some of it",
            "value": "some"
        }
    ]

    ALL_CHOICE = "all"
    SOME_CHOICE = "some"


    DEPENDENT_CLAIMER_VALUES = [
        {
            "value_name": "dependent_claimer_first_name",
            "display": "First name",
            "placeholder_text": "",
            "changed_function": "save_value_active_input_required",
            "type": "string"   
        },
        {
            "value_name": "dependent_claimer_middle_name",
            "display": "Middle name",
            "placeholder_text": "",
            "changed_function": "save_value_active_input",
            "type": "string"   
        },
        {
            "value_name": "dependent_claimer_last_name",
            "display": "Last name",
            "placeholder_text": "",
            "changed_function": "save_value_active_input_required",
            "type": "string"   
        }
    ]

    ADDRESS_VALUES = [
        {
            "value_name": "residential_address.line_1",
            "display": "Line 1",
            "placeholder_text": "Line 1",
            "changed_function": "validate_and_save_active_input_required_property",
            "type": "prop_string"   
        },
        {
            "value_name": "residential_address.line_2",
            "display": "Line 2",
            "placeholder_text": "Line 2",
            "changed_function": "validate_and_save_active_input_property",
            "type": "prop_string"   
        },
        {
            "value_name": "residential_address.city",
            "display": "City",
            "placeholder_text": "City",
            "changed_function": "validate_and_save_active_input_required_property",
            "type": "prop_string"   
        },
        {
            "value_name": "residential_address.state",
            "display": "State",
            "placeholder_text": "State (XX)",
            "changed_function": "validate_and_save_active_input_state_prop",
            "type": "prop_string"   
        },
        {
            "value_name": "residential_address.zip",
            "display": "Zip code",
            "placeholder_text": "Zip Code",
            "changed_function": "validate_and_save_active_input_zip_prop",
            "type": "prop_string"   
        }
    ]

    SCHOOL_0_ADDRESS_VALUES = [
        {
            "value_name": "aoc_schools[0].line_1",
            "display": "Line 1",
            "placeholder_text": "Line 1",
            "changed_function": "validate_and_save_active_input_required_array_property",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[0].line_2",
            "display": "Line 2",
            "placeholder_text": "Line 2",
            "changed_function": "validate_and_save_active_input_array_property",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[0].city",
            "display": "City",
            "placeholder_text": "City",
            "changed_function": "validate_and_save_active_input_required_array_property",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[0].state",
            "display": "State",
            "placeholder_text": "State (XX)",
            "changed_function": "validate_and_save_active_input_state_array_prop",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[0].zip",
            "display": "Zip code",
            "placeholder_text": "Zip Code",
            "changed_function": "validate_and_save_active_input_zip_array_prop",
            "type": "arr_prop_string"   
        }
    ]

    SCHOOL_1_ADDRESS_VALUES = [
        {
            "value_name": "aoc_schools[1].line_1",
            "display": "Line 1",
            "placeholder_text": "Line 1",
            "changed_function": "validate_and_save_active_input_required_array_property",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[1].line_2",
            "display": "Line 2",
            "placeholder_text": "Line 2",
            "changed_function": "validate_and_save_active_input_array_property",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[1].city",
            "display": "City",
            "placeholder_text": "City",
            "changed_function": "validate_and_save_active_input_required_array_property",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[1].state",
            "display": "State",
            "placeholder_text": "State (XX)",
            "changed_function": "validate_and_save_active_input_state_array_prop",
            "type": "arr_prop_string"   
        },
        {
            "value_name": "aoc_schools[1].zip",
            "display": "Zip code",
            "placeholder_text": "Zip Code",
            "changed_function": "validate_and_save_active_input_zip_array_prop",
            "type": "arr_prop_string"   
        }
    ]
    NAME_VALUES = [
        {
            "value_name": "first_name",
            "display": "First name",
            "placeholder_text": "First name",
            "changed_function": "save_value_active_input_required",
            "type": "string"   
        },
        {
            "value_name": "middle_name",
            "display": "Middle name",
            "placeholder_text": "Middle name",
            "changed_function": "save_value_active_input",
            "type": "string"   
        },
        {
            "value_name": "last_name",
            "display": "Last name",
            "placeholder_text": "Last name",
            "changed_function": "save_value_active_input_required",
            "type": "string"   
        }
    ]

    VALUE_DISPLAY_NAMES = {
        "dependent_claimer_first_name": "First name",
        "dependent_claimer_middle_name": "Middle name",
        "dependent_claimer_last_name": "Last name"
    }

    NUMBER_OF_PAGE_FLIP_SOUNDS = 8

    def custom_yes_or_no_choices(yes_text="Yes", no_text="No", has_what=False, what_text="What?!"):
        choices = [
            {
                "display": yes_text,
                "value": True
            },
            {
                "display": no_text,
                "value": False
            }
        ]
        
        if has_what:
            choices.append({
                "display": what_text,
                "value": "what"
            })
        
        return choices


    diary_field_section_page_mapping = {}

    def generate_diary_field_section_page_mapping():
        for section_idx, section in enumerate(diary_sections):
            for page_idx, page in enumerate(section["pages"]):
                for subsection in page["sections"]:
                    for field in subsection["fields"]:
                        if field["type"] == "address_input":
                            diary_field_section_page_mapping.update({
                                    f'{field["value_name"]}.line_1': {
                                        "section_number": section_idx,
                                        "page_number": page_idx
                                    },
                                    f'{field["value_name"]}.line_2': {
                                        "section_number": section_idx,
                                        "page_number": page_idx
                                    },
                                    f'{field["value_name"]}.city': {
                                        "section_number": section_idx,
                                        "page_number": page_idx
                                    },
                                    f'{field["value_name"]}.state': {
                                        "section_number": section_idx,
                                        "page_number": page_idx
                                    },
                                    f'{field["value_name"]}.zip': {
                                        "section_number": section_idx,
                                        "page_number": page_idx
                                    }
                            })
                        else:
                            diary_field_section_page_mapping.update({
                                    field["value_name"]: {
                                        "section_number": section_idx,
                                        "page_number": page_idx
                                    }
                            })

    generate_diary_field_section_page_mapping()

    COFFEE_CHOICES = [
        {
            "display": "Black Coffee",
            "value": "black coffee"
        },
        {
            "display": "Latte",
            "value": "latte"
        },
        {
            "display": "Tea! Pinky up!",
            "value": "tea"
        },
        {
            "display": "Matcha",
            "value": "matcha"
        }
    ]

    COFFEE_SCENE_CHOICES = [
        {
            "display": "Black Coffee",
            "value": "black coffee"
        },
        {
            "display": "Cortado",
            "value": "cortado"
        },
        {
            "display": "Latte",
            "value": "latte"
        },
        {
            "display": "Pumpkin Spice Latte",
            "value": "pumpkin spice latte"
        },
        {
            "display": "Tea",
            "value": "tea"
        },
        {
            "display": "Cappuccino",
            "value": "cappuccino"
        }
    ]

    IRIS_FAV_DRINK_CHOICE = "ventichagomachiucci"

    COFFEE_SCENE_MC_CHOICES = [
        {
            "display": "Black Coffee",
            "value": "black coffee"
        },
        {
            "display": "Latte",
            "value": "latte"
        },
        {
            "display": "Tea",
            "value": "tea"
        },
        {
            "display": "Water",
            "value": "water"
        },
    ]

    BOOKS_TO_CHOOSE_FROM = [
        "Looks like Iris is reading {i}Do Androids Dream Of Electric Sheep{/i}? I seem to recall this is the book that {i}Blade Runner{/i} is based on. Maybe Iris has a taste for sci-fi.",
        "Let’s see what Iris is reading today. Oh, wow. {i}Frankenstein{/i}. Really dipping into the classics. Doesn’t Iris work here? Should she really be spending so much time reading her own books?",
        "What’s this book? {i}The Cyborg Manifesto{/i}. Donna Haraway. This is intimidating reading. I’m impressed by Iris’ fortitude.",
        "Oh hey! This is Kazuo Ishiguro’s latest: {i}Klara And The Sun{/i}. I’ve heard this is really good. Hell of a writer, nothing but bangers. ",
        "Iris has a DVD on her desk today. I always forget that libraries have digital media too. {i}Her, with Scarlett Johansson and Joaquin Phoenix{/i}. This is that movie where the guy falls in love with an AI, right? Haven’t seen this in ages, I wonder if it holds up.",
        "It appears Iris is reading Isaac Asimov’s {i}I, Robot{/i}. No one can accuse Asimov of writing beautiful prose, but his basic concepts have shaped pretty much all subsequent fiction that deals with robots, sentience, and artificial intelligence.",
        "Looks like this time Iris is reading {i}All Systems Red{/i} by Martha Wells. I’ve heard a bunch of people talk about this series! Maybe I should give it a shot sometime.",
        "Iris has a DVD for the 1995 {i}Ghost In The Shell{/i} out on her desk, hell yeah. An absolute classic. Thank goodness no one ever tried to remake it."
    ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
