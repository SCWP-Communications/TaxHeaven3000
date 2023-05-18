init python:
    def clear_education_credit_values_and_errors():
        current_globals = globals()
        current_globals["edu_credit_eligible"] = False
        current_globals["claiming_aoc"] = False
        current_globals["aoc_refundable_eligible"] = False
        current_globals["claiming_lllc"] = False
        current_globals["aoc_claimed_last_four_years"] = None
        current_globals["aoc_first_four_years_completed_before_this_year"] = None
        current_globals["aoc_has_been_convicted"] = None
        current_globals["aoc_refundable_parents_alive"] = None
        current_globals["aoc_schools"] = [School()]
        current_globals["aoc_qualified_educational_expenses"] = None
        current_globals["student_status"] = None
        clear_error_by_id("aoc_claimed_last_four_years")
        clear_error_by_id("aoc_first_four_years_completed_before_this_year")
        clear_error_by_id("aoc_has_been_convicted")
        clear_error_by_id("aoc_refundable_parents_alive")
        clear_error_by_id("aoc_schools[0].name")
        clear_error_by_id("aoc_schools[0].line_1")
        clear_error_by_id("aoc_schools[0].city")
        clear_error_by_id("aoc_schools[0].state")
        clear_error_by_id("aoc_schools[0].zip")
        clear_error_by_id("aoc_schools[0].did_receive_1098t_this_year")
        clear_error_by_id("aoc_schools[0].did_receive_1098t_previous_year_box_7")
        clear_error_by_id("aoc_schools[1].name")
        clear_error_by_id("aoc_schools[1].line_1")
        clear_error_by_id("aoc_schools[1].city")
        clear_error_by_id("aoc_schools[1].state")
        clear_error_by_id("aoc_schools[1].zip")
        clear_error_by_id("aoc_schools[1].did_receive_1098t_this_year")
        clear_error_by_id("aoc_schools[1].did_receive_1098t_previous_year_box_7")
        clear_error_by_id("student_status")
        clear_error_by_id("aoc_qualified_educational_expenses")

    def clear_earned_income_credit_values_and_errors():
        current_globals = globals()
        current_globals["resided_in_us_for_more_than_half_the_year"] = None
        current_globals["had_nontaxable_combat_pay"] = None
        current_globals["nontaxable_combat_pay_election"] = None
        
        clear_error_by_id("resided_in_us_for_more_than_half_the_year")
        clear_error_by_id("had_nontaxable_combat_pay")
        clear_error_by_id("nontaxable_combat_pay_election")

    def evaluate_errors_and_add_diary_pages(changed=None, evaluate_all=True):
        evaluate_dependent_fields_and_add_errors(changed, evaluate_all)
        evaluate_fields_and_add_dependent_diary_pages(changed, evaluate_all)
        
        if in_diary_review or in_diary_review_bank_info:
            has_error_on_current_page()
            
            if not evaluate_all:
                jump_to_correct_dialogue_for_diary_review()
        elif not in_diary_tutorial and not evaluate_all:
            call_diary_with_correct_dialogue()
        
        renpy.restart_interaction()

    def file_upload_diary_review_evaluate_errors_and_add_diary_pages(changed):
        evaluate_dependent_fields_and_add_errors(changed, False)
        evaluate_fields_and_add_dependent_diary_pages(changed, False)
        jump_to_correct_dialogue_for_diary_review()
        
        renpy.restart_interaction()

    def evaluate_dependent_fields_and_add_errors(changed=None, evaluate_all=False):
        global REQUIRED_FIELDS
        calculate_return_needed = False    
        if evaluate_all:
            clear_errors()
        
        current_globals = globals()
        
        if evaluate_all:
            
            for field in REQUIRED_FIELDS:
                if current_globals[field] == None or current_globals[field] == "":
                    add_error(field, "This field is required")
        
        agi_changed = False
        if evaluate_all or ("w2_objects" in changed and "box_1" in changed) or ("int_1099_objects" in changed and ("total_interest" in changed or "tax_exempt_interest" in changed or "federal_income_tax_witheld" in changed)) or changed in ["household_empoloyee_wages_not_reported_on_w2", "nontaxable_combat_pay", "social_security_taxable_amount", "tax_deferred_ira_contributions", "unemployment_compensation", "unemployment_compensation_tax_witheld", "student_loan_interest", "educator_expenses"]:
            agi_changed = True
            calculate_return_up_to_agi()
            calculate_return_needed = True
        
        if changed != None and ("w2_objects" in changed and "box_2" in changed):
            calculate_return_needed = True
        
        if changed is not None and changed in ["aoc_refundable_earned_income_half_of_support", "interest_income_earned_income_half_of_support"]:
            if changed == "interest_income_earned_income_half_of_support":
                current_globals["aoc_refundable_earned_income_half_of_support"] = current_globals["interest_income_earned_income_half_of_support"]
            elif changed == "aoc_refundable_earned_income_half_of_support":
                current_globals["interest_income_earned_income_half_of_support"] = current_globals["aoc_refundable_earned_income_half_of_support"]
        
        if current_globals["cafe_visited"]:
            if evaluate_all:
                for field in CAFE_REQUIRED_FIELDS:
                    if current_globals[field] == None or current_globals[field] == "":
                        add_error(field, "This field is required")
                
                validate_and_save_ssn(value=current_globals["social_security_number"], evaluate_all=evaluate_all)
                validate_and_save_phone_number(value=current_globals["phone_number"], evaluate_all=evaluate_all)
                
                if current_globals["birth_date"] is not None:
                    validate_and_save_birth_date(value=convert_date_to_displayable_string(current_globals["birth_date"]), evaluate_all=evaluate_all)
                
                if current_globals["residential_address"].line_1 == "":
                    add_error("residential_address.line_1", "This field is required")
                
                if current_globals["residential_address"].city == "":
                    add_error("residential_address.city", "This field is required")
                
                current_globals["active_input_field_id"] = "residential_address.state"
                validate_and_save_active_input_state_prop(current_globals["residential_address"].state, evaluate_all=evaluate_all)
                current_globals["active_input_field_id"] = "residential_address.zip"
                validate_and_save_active_input_zip_prop(current_globals["residential_address"].zip, evaluate_all=evaluate_all)
                current_globals["active_input_field_id"] = None
        
        if current_globals["office_visited"]:
            
            if evaluate_all or changed == "has_unsupported_box_12_codes":
                if has_unsupported_box_12_codes:
                    add_error("has_unsupported_box_12_codes", "You must change this field")
            
            if evaluate_all or changed == "w2_objects" or "w2_objects" in changed:
                if evaluate_all or (changed != None and "box_2" not in changed and "box_1" not in changed and "box_4" not in changed):
                    clear_error_by_key_substring("w2_objects")
                calculate_return_needed = True
                if len(current_globals["w2_objects"]) == 0:
                    add_error("w2_objects", "At least one W2 is required")
                else:
                    clear_error_by_id("w2_objects")
                    if evaluate_all or (changed != None and "box_2" not in changed and "box_1" not in changed and "box_4" not in changed):
                        for idx, w2 in enumerate(current_globals["w2_objects"]):
                            if w2.get_box_1() == 0 or w2.box_1 == None:
                                add_error(f"w2_objects[{idx}].box_1", "This field is required")
                            
                            if w2.box_2 == None:
                                add_error(f"w2_objects[{idx}].box_2", "This field is required")
                            
                            if w2.box_4 == None:
                                add_error(f"w2_objects[{idx}].box_4", "This field is required")
            
            if evaluate_all or changed in ["household_empoloyee_wages_not_reported_on_w2", "has_household_wages_not_reported_on_w2"]:
                if evaluate_all:
                    if current_globals["household_empoloyee_wages_not_reported_on_w2"] == None:
                        add_error("household_empoloyee_wages_not_reported_on_w2", "This field is required")
            
            
            if changed in ["has_social_security_benefits", "social_security_taxable_amount"] or evaluate_all:
                calculate_return_needed = True
                if current_globals["has_social_security_benefits"]:
                    if evaluate_all or changed == "has_social_security_benefits":
                        if current_globals["social_security_taxable_amount"] == None:
                            add_error("social_security_taxable_amount", "This field is required")
                else:
                    clear_error_by_id("social_security_taxable_amount")
                    current_globals["social_security_taxable_amount"] = None
            
            
            if evaluate_all or changed == "has_income_interest" or changed == "int_1099_objects" or ("int_1099_objects" in changed and ("total_interest" in changed or "tax_exempt_interest" in changed)) or changed in ["birth_date", "aoc_refundable_earned_income_half_of_support", "interest_income_earned_income_half_of_support", "was_full_time_student_one_term"]:
                calculate_return_needed = True
                if current_globals["has_income_interest"]:
                    if evaluate_all or (changed != None and "tax_exempt_interest" not in changed and "total_interest" not in changed and "federal_income_tax_witheld" not in changed):
                        clear_error_by_key_substring("int_1099_objects")
                    for idx, obj in enumerate(current_globals["int_1099_objects"]):
                        if current_globals["int_1099_objects"][idx].payer_name == "" or current_globals["int_1099_objects"][idx].payer_name == None:
                            add_error(f"int_1099_objects[{idx}].payer_name", "This field is required")
                        else:
                            clear_error_by_id(current_globals["int_1099_objects"][idx].payer_name)
                        
                        if evaluate_all or (changed != None and "tax_exempt_interest" not in changed and "total_interest" not in changed and "federal_income_tax_witheld" not in changed):
                            if current_globals["int_1099_objects"][idx].total_interest == None:
                                add_error(f"int_1099_objects[{idx}].total_interest", "This field is required")
                            
                            if current_globals["int_1099_objects"][idx].tax_exempt_interest == None:
                                add_error(f"int_1099_objects[{idx}].tax_exempt_interest", "This field is required")
                            if current_globals["int_1099_objects"][idx].federal_income_tax_witheld == None:
                                add_error(f"int_1099_objects[{idx}].federal_income_tax_witheld", "This field is required")
                        
                        if get_total_1099_int_box_1() >= 2300:
                            if get_error_message_by_id("birth_date") is not None and get_error_message_by_id("birth_date") == "You must change this field":
                                clear_error_by_id("birth_date")
                            clear_error_by_id("interest_income_earned_income_half_of_support")
                            clear_error_by_id("was_full_time_student_one_term")
                            if current_globals["age"] < 18:
                                clear_warnings()
                                current_globals["was_full_time_student_one_term"] = None
                                if changed is not None:
                                    if changed == "birth_date":
                                        add_error("birth_date", "You must change your birth date")
                                    elif ("int_1099_objects" in changed and "total_interest" in changed):
                                        add_error(changed, "You must change this field")
                                else:
                                    for idx, obj in enumerate(current_globals["int_1099_objects"]):
                                        add_error(f"int_1099_objects[{idx}].total_interest", "Income interest can't be over $2300")
                            elif current_globals["age"] == 18:
                                clear_warnings()
                                current_globals["was_full_time_student_one_term"] = None
                                if current_globals["interest_income_earned_income_half_of_support"] is None:
                                    add_error("interest_income_earned_income_half_of_support", "This field is required")
                                elif current_globals["interest_income_earned_income_half_of_support"] == False:
                                    if changed is not None:
                                        if changed == "birth_date":
                                            add_error("birth_date", "You must change your birth date")
                                        elif ("int_1099_objects" in changed and "total_interest" in changed):
                                            add_error(changed, "You must change this field")
                                        elif changed == "interest_income_earned_income_half_of_support" or changed == "aoc_refundable_earned_income_half_of_support":
                                            add_error("interest_income_earned_income_half_of_support", "You must change this field")
                                else:
                                    clear_error_by_id("interest_income_earned_income_half_of_support")
                            elif current_globals["age"] > 18 and current_globals["age"] < 24:
                                if current_globals["was_full_time_student_one_term"] != None and current_globals["was_a_student"] != None and current_globals["student_status"] != None:
                                    if current_globals["was_full_time_student_one_term"]:
                                        if current_globals["was_a_student"] == False or current_globals["student_status"] != FULL_TIME_CHOICE:
                                            add_warning("was_full_time_student_one_term", "")
                                        else:
                                            clear_warnings()
                                    else:
                                        if current_globals["was_a_student"] and current_globals["student_status"] == FULL_TIME_CHOICE:
                                            add_warning("was_full_time_student_one_term", "")
                                        else:
                                            clear_warnings()
                                else:
                                    clear_warnings()
                                
                                if current_globals["was_full_time_student_one_term"] is None:
                                    add_error("was_full_time_student_one_term", "This field is required")
                                elif current_globals["was_full_time_student_one_term"] == True:
                                    if current_globals["interest_income_earned_income_half_of_support"] is None:
                                        add_error("interest_income_earned_income_half_of_support", "This field is required")
                                    elif current_globals["interest_income_earned_income_half_of_support"] == False:
                                        if changed is not None:
                                            if changed == "birth_date":
                                                add_error("birth_date", "You must change your birth date")
                                            elif ("int_1099_objects" in changed and "total_interest" in changed):
                                                add_error(changed, "You must change this field")
                                            elif changed == "interest_income_earned_income_half_of_support" or changed == "aoc_refundable_earned_income_half_of_support":
                                                add_error("interest_income_earned_income_half_of_support", "You must change this field")
                                            elif changed == "was_full_time_student_one_term":
                                                add_error("was_full_time_student_one_term", "You must change this field")
                                else:
                                    clear_warnings()
                                    clear_error_by_id("was_full_time_student_one_term")
                                    clear_error_by_id("interest_income_earned_income_half_of_support")
                            else:
                                current_globals["was_full_time_student_one_term"] = None
                        else:
                            clear_warnings()
                            if get_error_message_by_id("birth_date") != None and get_error_message_by_id("birth_date") == "You must change your birth date":
                                clear_error_by_id("birth_date")
                            clear_error_by_id("was_full_time_student_one_term")
                            clear_error_by_id("interest_income_earned_income_half_of_support")
                
                else:
                    for idx, obj in enumerate(current_globals["int_1099_objects"]):
                        clear_error_by_id(f"int_1099_objects[{idx}].payer_name")
                        clear_error_by_id(f"int_1099_objects[{idx}].total_interest")
                        clear_error_by_id(f"int_1099_objects[{idx}].tax_exempt_interest")
                        clear_error_by_id(f"int_1099_objects[{idx}].federal_income_tax_witheld")
                    
                    clear_warnings()
                    current_globals["int_1099_objects"] = [Int1099()]
                    current_globals["was_full_time_student_one_term"] = None
                    if get_error_message_by_id("birth_date") != None and get_error_message_by_id("birth_date") == "You must change your birth date":
                        clear_error_by_id("birth_date")
                    clear_error_by_id("interest_income_earned_income_half_of_support")
                    clear_error_by_id("was_full_time_student_one_term")
            
            
            if changed == "has_unemployment_compensation" or changed == "unemployment_1099g_file_location" or evaluate_all:
                calculate_return_needed = True
                if changed is not None and changed == "unemployment_1099g_file_location":
                    
                    current_globals["unemployment_compensation"] = None
                    current_globals["unemployment_compensation_tax_witheld"] = None
                
                if current_globals["has_unemployment_compensation"]:
                    if current_globals["unemployment_1099g_file_location"] is None:
                        add_error("unemployment_1099g_file_location", "You must upload a Form 1099-G")
                        clear_error_by_id("unemployment_compensation")
                        clear_error_by_id("unemployment_compensation_tax_witheld")
                    else:
                        clear_error_by_id("unemployment_1099g_file_location")
                        if current_globals["unemployment_compensation"] is None:
                            add_error("unemployment_compensation", "This field is required")
                        if current_globals["unemployment_compensation_tax_witheld"] is None:
                            add_error("unemployment_compensation_tax_witheld", "This field is required")
                
                else:
                    clear_error_by_id("unemployment_compensation")
                    clear_error_by_id("unemployment_compensation_tax_witheld")
                    clear_error_by_id("unemployment_1099g_file_location")
                    
                    current_globals["unemployment_compensation"] = None
                    current_globals["unemployment_compensation_tax_witheld"] = None
                    if current_globals["unemployment_1099g_file_location"] != None:
                        current_globals["unemployment_1099g_file_location"].delete_file_and_previews()
                        current_globals["unemployment_1099g_file_location"] = None
        
        if current_globals["library_visited"]:
            if evaluate_all:
                if current_globals["estimated_tax_payments"] == None:
                    add_error("estimated_tax_payments", "This field is required")
                else:
                    clear_error_by_id("estimated_tax_payments")
                
                if current_globals["amount_applied_from_previous_year"] == None:
                    add_error("amount_applied_from_previous_year", "This field is required")
                else:
                    clear_error_by_id("amount_applied_from_previous_year")
            
            
            if evaluate_all or agi_changed or "aoc_schools" in changed or changed in ["someone_can_claim_as_dependent", "was_a_student", "paid_tuition_or_qualified_expenses", "aoc_qualified_educational_expenses", "student_status","aoc_pursued_a_program_leading_to_degree", "birth_date", "aoc_claimed_last_four_years", "aoc_first_four_years_completed_before_this_year", "aoc_has_been_convicted", "aoc_refundable_parents_alive", "aoc_refundable_earned_income_half_of_support", "interest_income_earned_income_half_of_support"]:
                if evaluate_all or ("aoc_schools" not in changed) or ("aoc_schools" in changed and "ein" in changed):
                    calculate_return_needed = True
                age = current_globals["age"]
                current_student_status = current_globals["student_status"]
                determine_if_eligible_for_aoc_vs_lllc()
                if current_globals["form_1040_line_11"] >= 90000 or current_globals["someone_can_claim_as_dependent"]:
                    current_globals["was_a_student"] = None
                    current_globals["paid_tuition_or_qualified_expenses"] = None
                    current_globals["aoc_pursued_a_program_leading_to_degree"] = None
                    clear_warnings()
                    
                    clear_error_by_id("was_a_student")
                    clear_error_by_id("paid_tuition_or_qualified_expenses")
                    clear_error_by_id("aoc_pursued_a_program_leading_to_degree")
                    clear_education_credit_values_and_errors()
                    clear_earned_income_credit_values_and_errors()
                else:
                    if current_globals["was_a_student"] is None:
                        add_error("was_a_student", "This field is required")
                    else:
                        clear_error_by_id("was_a_student")
                        if current_globals["was_full_time_student_one_term"] != None:
                            if (current_globals["was_full_time_student_one_term"] and current_globals["was_a_student"] == False):
                                add_warning("was_a_student", "")
                            else:
                                clear_warnings()
                        else:
                            clear_warnings()
                    
                    if current_globals["paid_tuition_or_qualified_expenses"] is None:
                        add_error("paid_tuition_or_qualified_expenses", "This field is required")
                    else:
                        clear_error_by_id("paid_tuition_or_qualified_expenses")
                    
                    if current_globals["aoc_pursued_a_program_leading_to_degree"] is None:
                        add_error("aoc_pursued_a_program_leading_to_degree", "This field is required")
                    else:
                        clear_error_by_id("aoc_pursued_a_program_leading_to_degree")
                    
                    if current_globals["was_a_student"] and current_globals["paid_tuition_or_qualified_expenses"]:
                        if current_globals["student_status"] is None:
                            add_error("student_status", "This field is required")
                        else:
                            clear_error_by_id("student_status")
                            if current_globals["was_full_time_student_one_term"] != None:
                                if (current_globals["was_full_time_student_one_term"] and current_globals["student_status"] != FULL_TIME_CHOICE) or (not current_globals["was_full_time_student_one_term"] and current_globals["student_status"] == FULL_TIME_CHOICE):
                                    add_warning("student_status", "")
                                else:
                                    clear_warnings()
                            else:
                                clear_warnings()                    
                        
                        if evaluate_all or changed != "aoc_qualified_educational_expenses":
                            if current_globals["aoc_qualified_educational_expenses"] == None:
                                add_error("aoc_qualified_educational_expenses", "This field is required")
                            elif current_globals["aoc_qualified_educational_expenses"] != None:
                                if current_globals["claiming_aoc"]:
                                    value = str(current_globals["aoc_qualified_educational_expenses"])
                                    if float(value) > 4000:
                                        add_error("aoc_qualified_educational_expenses", "Value cannot exceed 4000")
                                    else:
                                        clear_error_by_id("aoc_qualified_educational_expenses")
                                elif current_globals["claiming_lllc"]:
                                    value = str(current_globals["aoc_qualified_educational_expenses"])
                                    if float(value) > 10000:
                                        add_error("aoc_qualified_educational_expenses", "Value cannot exceed 10000")
                                    else:
                                        clear_error_by_id("aoc_qualified_educational_expenses")
                                else:
                                    clear_error_by_id("aoc_qualified_educational_expenses")
                        
                        if current_student_status != LESS_THAN_HALF_CHOICE:
                            if current_globals["aoc_claimed_last_four_years"] is None:
                                add_error("aoc_claimed_last_four_years", "This field is required")
                            else:
                                clear_error_by_id("aoc_claimed_last_four_years")
                            
                            if current_globals["aoc_first_four_years_completed_before_this_year"] is None:
                                add_error("aoc_first_four_years_completed_before_this_year", "This field is required")
                            else:
                                clear_error_by_id("aoc_first_four_years_completed_before_this_year")
                            
                            if current_globals["aoc_has_been_convicted"] is None:
                                add_error("aoc_has_been_convicted", "This field is required")
                            else:
                                clear_error_by_id("aoc_has_been_convicted")
                        else:
                            current_globals["aoc_claimed_last_four_years"] = None
                            current_globals["aoc_first_four_years_completed_before_this_year"] = None
                            current_globals["aoc_has_been_convicted"] = None
                            clear_error_by_id("aoc_claimed_last_four_years")
                            clear_error_by_id("aoc_first_four_years_completed_before_this_year")
                            clear_error_by_id("aoc_has_been_convicted")
                        
                        
                        if current_globals["claiming_aoc"]:
                            
                            if (age < 18 or (age <= 24 and age >= 18 and student_status != HALF_TIME_CHOICE)) and current_globals["aoc_refundable_parents_alive"] is None:
                                add_error("aoc_refundable_parents_alive", "This field is required")
                            else:
                                clear_error_by_id("aoc_refundable_parents_alive")
                            
                            if (age <= 24 and age >= 18 and student_status != HALF_TIME_CHOICE) and current_globals["aoc_refundable_earned_income_half_of_support"] is None:
                                add_error("aoc_refundable_earned_income_half_of_support", "This field is required")
                            else:
                                clear_error_by_id("aoc_refundable_earned_income_half_of_support")
                            
                            if evaluate_all:
                                for idx, school in enumerate(current_globals["aoc_schools"]):
                                    current_globals["active_input_field_id"] = f"aoc_schools[{idx}].ein"
                                    validate_and_save_ein_active_field_array_prop(aoc_schools[idx].ein, evaluate_all=evaluate_all)
                                    current_globals["active_input_field_id"] = None
                        else:
                            current_globals["aoc_refundable_parents_alive"] = None
                            clear_error_by_id("aoc_refundable_parents_alive")
                            clear_error_by_id("aoc_refundable_earned_income_half_of_support")
                        
                        
                        if current_globals["aoc_schools"][0].name is "":
                            add_error("aoc_schools[0].name", "This field is required")
                        
                        if current_globals["aoc_schools"][0].line_1 is "":
                            add_error("aoc_schools[0].line_1", "This field is required")
                        
                        if current_globals["aoc_schools"][0].city is "":
                            add_error("aoc_schools[0].city", "This field is required")
                        
                        if current_globals["aoc_schools"][0].state is "":
                            add_error("aoc_schools[0].state", "This field is required")
                        
                        if current_globals["aoc_schools"][0].zip is "":
                            add_error("aoc_schools[0].zip", "This field is required")
                        
                        if current_globals["aoc_schools"][0].did_receive_1098t_this_year is None:
                            add_error("aoc_schools[0].did_receive_1098t_this_year", "This field is required")
                        else:
                            clear_error_by_id("aoc_schools[0].did_receive_1098t_this_year")
                        
                        if current_globals["aoc_schools"][0].did_receive_1098t_previous_year_box_7 is None:
                            add_error("aoc_schools[0].did_receive_1098t_previous_year_box_7", "This field is required")
                        else:
                            clear_error_by_id("aoc_schools[0].did_receive_1098t_previous_year_box_7")
                        if len(current_globals["aoc_schools"]) > 1:
                            
                            if current_globals["aoc_schools"][1].name is "":
                                add_error("aoc_schools[1].name", "This field is required")
                            
                            if current_globals["aoc_schools"][1].line_1 is "":
                                add_error("aoc_schools[1].line_1", "This field is required")
                            
                            if current_globals["aoc_schools"][1].city is "":
                                add_error("aoc_schools[1].city", "This field is required")
                            
                            if current_globals["aoc_schools"][1].state is "":
                                add_error("aoc_schools[1].state", "This field is required")
                            
                            if current_globals["aoc_schools"][1].zip is "":
                                add_error("aoc_schools[1].zip", "This field is required")
                            
                            if current_globals["aoc_schools"][1].did_receive_1098t_this_year is None:
                                add_error("aoc_schools[1].did_receive_1098t_this_year", "This field is required")
                            else:
                                clear_error_by_id("aoc_schools[1].did_receive_1098t_this_year")
                            
                            if current_globals["aoc_schools"][1].did_receive_1098t_previous_year_box_7 is None:
                                add_error("aoc_schools[1].did_receive_1098t_previous_year_box_7", "This field is required")
                            else:
                                clear_error_by_id("aoc_schools[1].did_receive_1098t_previous_year_box_7")
                        else:
                            clear_error_by_id("aoc_schools[1].name")
                            clear_error_by_id("aoc_schools[1].line_1")
                            clear_error_by_id("aoc_schools[1].city")
                            clear_error_by_id("aoc_schools[1].state")
                            clear_error_by_id("aoc_schools[1].zip")
                            clear_error_by_id("aoc_schools[1].did_receive_1098t_this_year")
                            clear_error_by_id("aoc_schools[1].did_receive_1098t_previous_year_box_7")
                    
                    else:
                        calculate_return_needed = True
                        clear_education_credit_values_and_errors()
            
            
            if evaluate_all or agi_changed or changed in ["birth_date", "someone_can_claim_as_dependent", "resided_in_us_for_more_than_half_the_year", "had_nontaxable_combat_pay"]:
                determine_if_eligible_for_eitc()
                calculate_return_needed = True
                if current_globals["form_1040_line_11"] >= 16480 or current_globals["someone_can_claim_as_dependent"] or (current_globals["age"] >= 65 or current_globals["age"] < 25):
                    clear_earned_income_credit_values_and_errors()
                else:
                    if current_globals["resided_in_us_for_more_than_half_the_year"] == None:
                        add_error("resided_in_us_for_more_than_half_the_year", "This field is required")
                    else:
                        clear_error_by_id("resided_in_us_for_more_than_half_the_year")
                    
                    if current_globals["had_nontaxable_combat_pay"] == None:
                        add_error("had_nontaxable_combat_pay", "This field is required")
                    else:
                        clear_error_by_id("had_nontaxable_combat_pay")
                        
                        
                        if not current_globals["had_nontaxable_combat_pay"]:
                            current_globals["nontaxable_combat_pay_election"] = None
                            clear_error_by_id("nontaxable_combat_pay_election")
                        else:
                            if current_globals["nontaxable_combat_pay_election"] == None:
                                add_error("nontaxable_combat_pay_election", "This field is required")
                            else:
                                clear_error_by_id("nontaxable_combat_pay_election")
            
            if evaluate_all or changed in ["educator_expenses", "has_educator_expenses"]:
                calculate_return_needed = True
                if evaluate_all or changed == "has_educator_expenses":
                    if current_globals["has_educator_expenses"] and current_globals["educator_expenses"] == None:
                        add_error("educator_expenses", "This field is required")
                
                if not current_globals["has_educator_expenses"]:
                    current_globals["educator_expenses"] = None
                    clear_error_by_id("educator_expenses")
            
            if evaluate_all or agi_changed or changed in ["someone_can_claim_as_dependent", "has_student_loan_interest", "student_loan_interest"]:
                calculate_return_needed = True
                if current_globals["form_1040_line_11"] >= 85000 or current_globals["someone_can_claim_as_dependent"]:
                    clear_error_by_id("student_loan_interest")
                    clear_error_by_id("has_student_loan_interest")
                    current_globals["has_student_loan_interest"] = None
                    current_globals["student_loan_interest"] = None
                else:
                    if current_globals["has_student_loan_interest"] == None:
                        add_error("has_student_loan_interest", "This field is required")
                    else:
                        clear_error_by_id("has_student_loan_interest")
                    
                    
                    
                    
                    
                    
                    if current_globals["has_student_loan_interest"] == False:
                        current_globals["student_loan_interest"] = None
                        clear_error_by_id("student_loan_interest")
                    elif current_globals["has_student_loan_interest"]:
                        if evaluate_all or changed == "has_student_loan_interest":
                            if current_globals["student_loan_interest"] == None:
                                add_error("student_loan_interest", "This field is required")
            
            if evaluate_all or agi_changed or changed in ["birth_date", "is_covered_by_employer_retirement_plan", "tax_deferred_ira_contributions"]:
                if changed is not None and changed in ["tax_deferred_ira_contributions", "is_covered_by_employer_retirement_plan"]:
                    calculate_return_needed = True
                
                if evaluate_all:
                    if current_globals["tax_deferred_ira_contributions"] == None:
                        add_error("tax_deferred_ira_contributions", "This field is required")
                
                if ((current_globals["form_1040_line_11"] > 68000 and current_globals["is_covered_by_employer_retirement_plan"] == False) or (current_globals["form_1040_line_11"] <= 68000)) and current_globals["tax_deferred_ira_contributions"] != None and current_globals["tax_deferred_ira_contributions"] != 0:
                    clear_error_by_id("is_covered_by_employer_retirement_plan")
                    clear_error_by_id("tax_deferred_ira_contributions")
                    if current_globals["tax_deferred_ira_contributions"] > MAX_IRA_CONTRIBUTION_UNDER_50 and current_globals["age"] < 50:
                        add_error("tax_deferred_ira_contributions", f"Value must be {MAX_IRA_CONTRIBUTION_UNDER_50} or less")
                    elif current_globals["tax_deferred_ira_contributions"] > MAX_IRA_CONTRIBUTION_50_OR_OVER and current_globals["age"] >= 50:
                        add_error("tax_deferred_ira_contributions", f"Value must be {MAX_IRA_CONTRIBUTION_50_OR_OVER} or less")
                elif current_globals["form_1040_line_11"] > 68000 and current_globals["tax_deferred_ira_contributions"] != None and current_globals["tax_deferred_ira_contributions"] != 0:
                    if current_globals["is_covered_by_employer_retirement_plan"] == None:
                        add_error("is_covered_by_employer_retirement_plan", "This field is required")
                    elif current_globals["is_covered_by_employer_retirement_plan"]:
                        if changed == "is_covered_by_employer_retirement_plan":
                            add_error("is_covered_by_employer_retirement_plan", "You must revise this answer")
                        else:
                            add_error("tax_deferred_ira_contributions", "Review IRA contribution amount")
                    else:
                        clear_error_by_id("is_covered_by_employer_retirement_plan")
                        clear_error_by_id("tax_deferred_ira_contributions")
                
                else:
                    clear_error_by_id("is_covered_by_employer_retirement_plan")
                    if current_globals["tax_deferred_ira_contributions"] != None:
                        clear_error_by_id("tax_deferred_ira_contributions")
            
            
            if evaluate_all or changed == "tax_deferred_ira_contributions":
                calculate_return_needed = True
                if current_globals["tax_deferred_ira_contributions"] == None or current_globals["tax_deferred_ira_contributions"] == 0:
                    current_globals["has_tax_deferred_ira_contributions"] = False
                else:
                    current_globals["has_tax_deferred_ira_contributions"] = True
        
        
        
        
        
        
        if changed is not None and (changed in ["estimated_tax_payments", "amount_applied_from_previous_year"] or ("w2_objects" in changed)):
            calculate_return_needed = True
        
        if calculate_return_needed:
            calculate_return()
        
        renpy.restart_interaction()

    def evaluate_fields_and_add_dependent_diary_pages(changed=None, evaluate_all=True):
        global diary_pages_w2, STATIC_INCOME_DIARY_PAGES_0, diary_pages_1099_int, extra_w2_diary_pages, STATIC_INCOME_DIARY_PAGES_1, diary_pages_1099_g, edu_eligibility_pages, aoc_screener_pages, aoc_refundable_pages, edu_school_pages, edu_final_pages, earned_income_credit_pages, excess_social_security_pages, educator_expenses_pages, refund_pages, diary_pages_w2, diary_sections
        current_globals = globals()
        agi_changed = False
        need_to_stay_on_current_page = False
        if evaluate_all or ("w2_objects" in changed and "box_1" in changed) or ("int_1099_objects" in changed and ("total_interest" in changed or "tax_exempt_interest" in changed or "federal_income_tax_witheld" in changed)) or changed in ["household_empoloyee_wages_not_reported_on_w2", "nontaxable_combat_pay", "social_security_taxable_amount", "tax_deferred_ira_contributions", "unemployment_compensation", "unemployment_compensation_tax_witheld", "student_loan_interest", "educator_expenses"]:
            agi_changed = True
        
        if current_globals["office_visited"]:
            if evaluate_all or changed == "w2_objects" or "w2_objects" in changed:
                add_diary_pages_for_w2s()
            
            if evaluate_all or agi_changed:
                extra_w2_diary_pages = [EXTRA_W2_DIARY_PAGE_WITHOUT_WARNING] if current_globals["form_1040_line_11"] > 34000 else [EXTRA_W2_DIARY_PAGE_WITH_WARNING]
            
            if changed == "has_unemployment_compensation" or changed == "unemployment_1099g_file_location" or evaluate_all:
                if current_globals["has_unemployment_compensation"]:
                    add_diary_pages_for_1099g()
                else:
                    current_globals["diary_pages_1099_g"] = []
            if evaluate_all or changed == "has_income_interest" or changed == "int_1099_objects" or ("int_1099_objects" in changed and "total_interest" in changed) or changed in ["birth_date", "aoc_refundable_earned_income_half_of_support", "interest_income_earned_income_half_of_support", "was_full_time_student_one_term"]:
                add_diary_pages_for_income_interest()
            
            if evaluate_all or changed == "has_social_security_benefits":
                add_diary_pages_for_ssa_1099()
            
            if changed != None and changed == "has_unsupported_box_12_codes":
                if has_unsupported_box_12_codes:
                    renpy.show_screen("game_over_modal", message="{i}Tax Heaven 3000{/i} does not currently support filers with certain W-2 box 12 codes")
            
            diary_sections[3]["pages"] = diary_pages_w2 + extra_w2_diary_pages + STATIC_INCOME_DIARY_PAGES_0 + diary_pages_1099_int + ssa_1099_pages + STATIC_INCOME_DIARY_PAGES_1 + diary_pages_1099_g
        
        if current_globals["library_visited"]:
            if changed is not None and ".ein" in changed:
                need_to_stay_on_current_page = True
            if evaluate_all or agi_changed or ("aoc_schools" in changed) or changed in ["someone_can_claim_as_dependent", "was_a_student", "paid_tuition_or_qualified_expenses","student_status","aoc_pursued_a_program_leading_to_degree", "birth_date", "aoc_claimed_last_four_years", "aoc_first_four_years_completed_before_this_year", "aoc_has_been_convicted", "aoc_refundable_parents_alive", "aoc_refundable_earned_income_half_of_support", "interest_income_earned_income_half_of_support"]:
                add_diary_pages_for_education_credits()
            if evaluate_all or agi_changed or changed in ["birth_date", "someone_can_claim_as_dependent", "resided_in_us_for_more_than_half_the_year", "had_nontaxable_combat_pay"]:
                add_diary_pages_for_earned_income_credit()
            if evaluate_all or agi_changed:
                add_diary_pages_for_excess_social_security()
            if evaluate_all or changed in ["educator_expenses", "has_educator_expenses"]:
                add_diary_pages_for_educator_expenses()
            if evaluate_all or agi_changed or changed in ["has_student_loan_interest", "student_loan_interest", "someone_can_claim_as_dependent"]:
                add_diary_pages_for_student_loan_interest()
            if evaluate_all or agi_changed or changed in ["is_covered_by_employer_retirement_plan", "tax_deferred_ira_contributions"]:
                if current_globals["form_1040_line_11"] > 68000 and is_covered_by_employer_retirement_plan and tax_deferred_ira_contributions != None and tax_deferred_ira_contributions != 0:
                    renpy.show_screen("game_over_modal", message="{i}Tax Heaven 3000{/i} does not currently support certain filers who made traditional IRA contributions whilst covered by an employer-sponsored retirement plan")
            if form_1040_line_37 > 0:
                overview_page = copy.deepcopy(REFUND_OVERVIEW_PAGE)
                overview_page["sections"].append(
                    {
                        "background": "gui/diary/page_backgrounds/diary_page_39.webp",
                        "display": None,
                        "fields": [
                            {
                                "display": "{}'s 2022 federal income tax owed",
                                "value_name": "form_1040_line_37",
                                "type": "static",
                                "prefix": "$",
                                "value_type": "number",
                                "changed_function": None
                            }
                        ]
                    }
                )
                if len(refund_pages) > 1:
                    extra_pages = refund_pages[1:]
                else:
                    extra_pages = []
                refund_pages = [overview_page] + extra_pages
            else:
                overview_page = copy.deepcopy(REFUND_OVERVIEW_PAGE)
                overview_page["sections"].append(
                    {
                        "background": "gui/diary/page_backgrounds/diary_page_39.webp",
                        "display": None,
                        "fields": [
                            {
                                "display": "{}'s 2022 federal income tax refund",
                                "value_name": "form_1040_line_34",
                                "type": "static",
                                "prefix": "$",
                                "value_type": "number",
                                "changed_function": None
                            }
                        ]
                    }
                )
                if len(refund_pages) > 1:
                    extra_pages = refund_pages[1:]
                else:
                    extra_pages = []
                refund_pages = [overview_page] + extra_pages
            
            diary_sections[4]["pages"] = IRA_CONRIBUTION_PAGES + edu_eligibility_pages + aoc_screener_pages + aoc_refundable_pages + edu_school_pages + edu_final_pages + earned_income_credit_pages + excess_social_security_pages + educator_expenses_pages + student_loan_pages + refund_pages + banking_diary_pages
        
        generate_diary_field_section_page_mapping()
        if need_to_stay_on_current_page:
            try:
                current_field_map = diary_field_section_page_mapping[active_input_field_id]
                global _diary_page, _diary_section
                _diary_section = current_field_map["section_number"]
                _diary_page = current_field_map["page_number"]
            except:
                pass
        
        
        
        
        renpy.restart_interaction()

    def add_diary_pages_for_ssa_1099():
        global has_social_security_benefits, ssa_1099_pages
        
        if has_social_security_benefits:
            ssa_1099_pages_copy = copy.deepcopy(SSA_1099_DIARY_PAGES)
            ssa_1099_pages_copy[0]["sections"].append(HAS_SSA_1099_SECTION)
            ssa_1099_pages = ssa_1099_pages_copy
        else:
            ssa_1099_pages_copy = copy.deepcopy(SSA_1099_DIARY_PAGES)
            ssa_1099_pages_copy[0]["sections"].append({
                "background": "gui/diary/page_backgrounds/diary_page_12.webp",
                "display": None,
                "fields": []
            })
            ssa_1099_pages = ssa_1099_pages_copy

    def add_diary_pages_for_income_interest():
        global diary_pages_1099_int
        
        if not has_income_interest:
            diary_pages_1099_int = []
        else:
            diary_pages_1099_int = []
            for idx, obj in enumerate(int_1099_objects):
                diary_pages_1099_int.append(create_1099_int_page(idx))
            
            diary_pages_1099_int = diary_pages_1099_int + SUMMARY_PAGES_1099_INT
            
            if get_total_1099_int_box_1() >= 2300:
                if age < 18:
                    renpy.show_screen("game_over_modal", message="{i}Tax Heaven 3000{/i} does not currently support certain filers under age 24 with interest income over $2300")
                elif age == 18:
                    diary_pages_1099_int.append(EARNED_INCOME_HALF_OF_SUPPORT_PAGE_1099_INT)
                    if interest_income_earned_income_half_of_support == False:
                        renpy.show_screen("game_over_modal", message="{i}Tax Heaven 3000{/i} does not currently support certain filers under age 24 with interest income over $2300")
                elif age > 18 and age < 24:
                    diary_pages_1099_int.append(EARNED_INCOME_HALF_OF_SUPPORT_AND_FULL_TIME_STUDENT_1099_INT_PAGE)
                    if was_full_time_student_one_term and interest_income_earned_income_half_of_support == False:
                        renpy.show_screen("game_over_modal", message="{i}Tax Heaven 3000{/i} does not currently support certain filers under age 24 with interest income over $2300")

    def add_diary_pages_for_education_credits():
        global edu_eligibility_pages, aoc_screener_pages, aoc_refundable_pages, edu_school_pages, edu_final_pages
        
        if form_1040_line_11 >= 90000 or someone_can_claim_as_dependent:
            edu_eligibility_pages = []
            aoc_screener_pages = []
            aoc_refundable_pages = []
            edu_school_pages = []
            edu_final_pages = []
        else:
            edu_eligibility_pages = STATIC_CREDITS_PAGES_0
            
            if was_a_student and paid_tuition_or_qualified_expenses:
                if student_status == LESS_THAN_HALF_CHOICE:
                    aoc_refundable_pages = []
                    aoc_screener_pages = []
                    aoc_refundable_pages = []
                else:
                    aoc_screener_pages = AOC_SCREENER_PAGES
                
                if claiming_aoc:
                    if age > 24:
                        aoc_refundable_pages = AOC_REFUNDABLE_ELIGIBLE_OVER_24_PAGES
                    elif age < 18:
                        aoc_refundable_pages = [
                            {
                                "sections": [
                                    AOC_REFUNDABLE_ELIGIBLE_UNDER_18_SECTION
                                ]
                            }
                        ]
                        
                        if aoc_refundable_eligible:
                            aoc_refundable_pages[0]["sections"].append(AOC_REFUNDABLE_ELIGIBLE_SECTION)
                        else:
                            aoc_refundable_pages[0]["sections"].append(AOC_REFUNDABLE_INELIGIBLE_SECTION)
                    
                    else:
                        if student_status == HALF_TIME_CHOICE and age != 18:
                            aoc_refundable_pages = AOC_REFUNDABLE_ELIGIBLE_OVER_24_PAGES
                        else:
                            aoc_refundable_pages = [
                                {
                                    "sections": [
                                        AOC_REFUNDABLE_BETWEEN_18_AND_24_SECTION
                                    ]
                                }
                            ]   
                            
                            if aoc_refundable_eligible:
                                aoc_refundable_pages[0]["sections"].append(AOC_REFUNDABLE_ELIGIBLE_SECTION)
                            else:
                                aoc_refundable_pages[0]["sections"].append(AOC_REFUNDABLE_INELIGIBLE_SECTION)
                else:
                    aoc_refundable_pages = []
                
                if len(aoc_schools) > 1:
                    school_page_1 = copy.deepcopy(EDU_SCHOOL_PAGE_1)
                    school_page_1["sections"][1].update({
                        "stickies": {
                            "add": {
                                "value_name": "aoc_schools",
                                "value_type": "School",
                                "display": "School",
                                "index": 0
                            },
                            "remove": {
                                "value_name": "aoc_schools",
                                "value_type": "School",
                                "index": 0,
                                "display": "School"
                            }
                        }
                    })
                    
                    school_page_2 = copy.deepcopy(EDU_SCHOOL_PAGE_2)
                    school_page_2["sections"][1].update({
                        "stickies": {
                            "remove": {
                                "value_name": "aoc_schools",
                                "value_type": "School",
                                "display": "School",
                                "index": 1
                            }
                        }
                    })
                    edu_school_pages = [school_page_1, school_page_2]
                else:
                    school_page_1 = copy.deepcopy(EDU_SCHOOL_PAGE_1)
                    school_page_1["sections"][1].update({
                        "stickies": {
                            "add": {
                                "value_name": "aoc_schools",
                                "display": "School",
                                "value_type": "School",
                                "index": 0
                            }
                        }
                    })
                    edu_school_pages = [school_page_1]
                
                if claiming_aoc:
                    edu_final_pages = STATIC_CREDITS_PAGES_1_AOC + [AOC_SUMMARY_PAGE]
                else:
                    edu_final_pages = STATIC_CREDITS_PAGES_1_LLLC + [LLLC_SUMMARY_PAGE]
            
            else:
                aoc_screener_pages = []
                aoc_refundable_pages = []
                edu_school_pages = []
                edu_final_pages = []

    def add_diary_pages_for_earned_income_credit():
        global form_1040_line_11, someone_can_claim_as_dependent, age, earned_income_credit_pages, had_nontaxable_combat_pay
        if form_1040_line_11 >= 16480 or someone_can_claim_as_dependent or (age >= 65 or age < 25):
            earned_income_credit_pages = []
        else:
            if had_nontaxable_combat_pay:
                earned_income_credit_pages = EARNED_INCOME_CREDIT_PAGES_WITH_NONTAXABLE_COMBAT_PAY_INPUT
            else:
                earned_income_credit_pages = EARNED_INCOME_CREDIT_PAGES

    def add_diary_pages_for_excess_social_security():
        global excess_social_security_pages
        
        if has_excess_social_security_to_claim:
            excess_social_security_pages = EXCESS_SOCIAL_SECURITY_PAGES
        else:
            excess_social_security_pages = []

    def add_diary_pages_for_educator_expenses():
        global educator_expenses_pages
        
        if has_educator_expenses:
            educator_expenses_pages = [EDUCATOR_EXPENSE_VALUES_PAGE]
        else:
            educator_expenses_pages = [EDUCATOR_EXPENSE_SCREENER_PAGE]

    def add_diary_pages_for_student_loan_interest():
        global student_loan_pages
        
        if form_1040_line_11 >= 85000 or someone_can_claim_as_dependent:
            student_loan_pages = []
        elif not has_student_loan_interest:
            student_loan_pages = [STUDENT_LOAN_SCREENER_PAGE]
        else:
            student_loan_pages = [STUDENT_LOAN_VALUES_PAGE]

    def add_diary_pages_for_1099g(refresh=True):
        global diary_pages_1099_g, unemployment_1099g_file_location, DEFAULT_1099_G_DIARY_PAGE, SUMMARY_PAGES_1099_G, diary_sections
        if refresh:
            diary_pages_1099_g = []
        if unemployment_1099g_file_location == None:
            diary_pages_1099_g = [DEFAULT_1099_G_DIARY_PAGE]
        else:
            diary_pages_1099_g.append({
                "id": G_1099_PAGE_ID,
                "sections": [
                    {
                        "background": "gui/diary/page_backgrounds/diary_page_15.webp",
                        "display": f"1099-G INCOME",
                        "fields": [
                            {
                                "display": "Total unemployment compensation (1099-G box 1)",
                                "value_name": "unemployment_compensation",
                                "type": "input",
                                "prefix": "$",
                                "value_type": "number",
                                "changed_function": "validate_and_save_dollar_active_field"
                            },
                            {
                                "display": "Federal income tax witheld (1099-G box 4)",
                                "value_name": "unemployment_compensation_tax_witheld",
                                "type": "input",
                                "prefix": "$",
                                "value_type": "number",
                                "changed_function": "validate_and_save_dollar_active_field"
                            }
                        ]
                    },
                    {
                        "display": None,
                        "fields": [
                            {
                                "display": "1099-G",
                                "value_name": "unemployment_1099g_file_location",
                                "type": "file",
                                "index": None,
                                "prefix": None,
                                "value_type": None,
                                "changed_function": None,
                                "pdf_type": "PDF"
                            }
                        ]
                    }
                ]
            })

    def add_diary_pages_for_w2s(refresh=True):
        global w2_objects, diary_pages_w2, DEFAULT_W2_DIARY_PAGE, diary_sections, STATIC_INCOME_DIARY_PAGES_0, diary_pages_1099_int, STATIC_INCOME_DIARY_PAGES_1, diary_pages_1099_g
        if refresh:
            diary_pages_w2 = []
        if len(w2_objects) == 0:
            diary_pages_w2.append(DEFAULT_W2_DIARY_PAGE)
        else:
            new_page = {}
            for idx, w2 in enumerate(w2_objects):
                if idx % 4 == 0:
                    page_id = FIRST_W2_PAGE_ID
                elif idx % 4 == 1:
                    page_id = SECOND_W2_PAGE_ID
                else:
                    page_id = THIRD_W2_PAGE_ID
                
                new_page = {
                    "id": page_id,
                    "sections": []
                }
                
                new_page["sections"].append(
                    {
                        "display": f"W-2 #{idx + 1} INCOME",
                        "fields": [
                            {
                                "display": "Taxable income (W-2 box 1) in 2022",
                                "value_name": f"w2_objects[{idx}].box_1",
                                "type": "input",
                                "prefix": "$",
                                "value_type": "arr_prop_number",
                                "changed_function": "validate_and_save_dollar_active_field_array_property"
                            },
                            {
                                "display": "Federal tax witheld (W2 box 2) in 2022",
                                "value_name": f"w2_objects[{idx}].box_2",
                                "type": "input",
                                "prefix": "$",
                                "value_type": "arr_prop_number",
                                "changed_function": "validate_and_save_dollar_active_field_array_property"
                            },
                            {
                                "display": "Social security tax witheld (W2 box 4)",
                                "value_name": f"w2_objects[{idx}].box_4",
                                "type": "input",
                                "prefix": "$",
                                "value_type": "arr_prop_number",
                                "changed_function": "validate_and_save_dollar_active_field_array_property"
                            }
                        ]
                    }
                )
                
                
                
                
                
                
                
                
                
                
                
                
                
                new_page["sections"][0].update({
                    "background": "gui/diary/page_backgrounds/diary_page_4.webp"
                })
                
                new_page["sections"].append(
                    {
                        "display": None,
                        "fields": [
                            {
                                "display": "W-2",
                                "value_name": "w2_objects",
                                "index": idx,
                                "type": "file",
                                "prefix": None,
                                "value_type": None,
                                "changed_function": None,
                                "pdf_type": "W2"
                            }
                        ]
                    }
                )
                diary_pages_w2.append(new_page)

    def remove_index_from_array(value_name, index):
        globals()[value_name].pop(index)
        evaluate_errors_and_add_diary_pages(changed=value_name, evaluate_all=False)

    def add_value_to_array(value_name, value_type):
        global object_class_name_mappings
        value_type_callable = object_class_name_mappings[value_type]
        globals()[value_name].append(value_type_callable())
        evaluate_errors_and_add_diary_pages(changed=value_name, evaluate_all=False)

    def has_error_on_current_page():
        global diary_field_section_page_mapping, error_messages, _diary_section, _diary_page, has_error_on_current_diary_page
        for value_name in error_messages.keys():
            try:
                mapping = diary_field_section_page_mapping[value_name]
                if mapping["section_number"] == _diary_section and mapping["page_number"] == _diary_page:
                    has_error_on_current_diary_page = True
                    return
            except Exception as e:
                has_error_on_current_diary_page = False
                return
        has_error_on_current_diary_page = False

    def has_warning_on_current_page():
        global diary_field_section_page_mapping, warning_messages, _diary_section, _diary_page, has_warning_on_current_diary_page
        for value_name in warning_messages.keys():
            try:
                mapping = diary_field_section_page_mapping[value_name]
                if mapping["section_number"] == _diary_section and mapping["page_number"] == _diary_page:
                    has_warning_on_current_diary_page = True
                    return
            except Exception as e:
                has_warning_on_current_diary_page = False
                return
        has_warning_on_current_diary_page = False

    def add_personal_diary_page(page):
        global personal_diary_pages, diary_sections
        personal_diary_pages.append(page)
        
        diary_sections[1]["pages"] = personal_diary_pages

    def jump_to_correct_dialogue_for_diary_review():
        has_error_on_current_page()
        has_warning_on_current_page()
        if has_error_on_current_diary_page:
            renpy.jump("diary_review_errors")
        elif in_diary_review and _diary_section == len(diary_sections) - 1 and _diary_page == len(diary_sections[_diary_section]['pages']) - 2 and error:
            renpy.jump("diary_review_end_of_review_errors_existing")
        elif has_warning_on_current_diary_page:
            page_id = diary_sections[_diary_section]["pages"][_diary_page].get("id", None)
            if page_id is not None:
                renpy.jump(f"diary_review_warning_{page_id}")
            else:
                renpy.jump("diary_review_ok")
        else:
            page_id = diary_sections[_diary_section]["pages"][_diary_page].get("id", None)
            if page_id is not None:
                renpy.jump(f"diary_review_{page_id}")
            else:
                renpy.jump("diary_review_ok")

    def jump_to_bookmarked_page():
        global _diary_page, _diary_section, diary_bookmark_index
        
        _diary_page = 0
        _diary_section = 1
        _diary_page = diary_bookmark_index

    def call_diary_with_correct_dialogue():
        if len(warning_messages) > 0:
            renpy.call("scene_5_diary_say_dialogue", "Hmmm, the student status I’ve selected here doesn’t match up with what I previously told Iris. I should fix that.")
        else:
            renpy.call("scene_5_diary_say_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
