init python:
    def calculate_return():
        global was_born_before_jan_2_1958, form_1040_line_29, form_1040_line_20, form_1040_line_21, form_1040_line_22, form_1040_line_24, form_1040_line_25b, form_1040_line_25d, federal_income_tax_witheld_from_w2, form_1040_line_27, form_1040_line_29, form_1040_line_31, form_1040_line_32, form_1040_line_33, form_1040_line_34, form_1040_line_37, refund, estimated_tax_payments_and_amount_applied_from_prev_year
        was_born_before_jan_2_1958 = '/On' if age >= 65 else '/Off'
        calculate_return_up_to_8863()
        form_1040_line_20 = calculate_form_1040_line_20()
        form_1040_line_21 = calculate_form_1040_line_21()
        form_1040_line_22 = calculate_form_1040_line_22()
        form_1040_line_24 = calculate_form_1040_line_24()
        form_1040_line_25b = calculate_form_1040_line_25b()
        form_1040_line_25d = calculate_form_1040_line_25d()
        federal_income_tax_witheld_from_w2 = get_total_w2_box_2()
        estimated_tax_payments_and_amount_applied_from_prev_year = calculate_1040_line_26()
        form_1040_line_27 = calculate_form_1040_line_27()
        form_1040_line_29 = calculate_form_1040_line_29()
        form_1040_line_31 = calculate_form_1040_line_31()
        form_1040_line_32 = calculate_form_1040_line_32()
        form_1040_line_33 = calculate_form_1040_line_33()
        form_1040_line_34 = calculate_form_1040_line_34()
        refund = form_1040_line_34
        form_1040_line_37 = calculate_form_1040_line_37()

    def calculate_return_up_to_agi():
        global form_scheduleb_line_2, form_1040_line_1a, form_1040_line_1z, form_1040_line_2a, form_1040_line_2b, form_1040_line_6b, form_1040_line_8, form_1040_line_9, form_1040_line_10, form_1040_line_11, form_1040_line_15, form_1040_line_16, form_1040_line_18, form_schedule1_line_26, form_schedule1_line_10, form_1040_line_12, form_1040_line_14
        form_1040_line_1a = get_total_w2_box_1()
        form_1040_line_1z = calculate_form_1040_line_1z()
        form_1040_line_2a = calculate_form_1040_line_2a()
        form_1040_line_2b = calculate_form_1040_line_2b()
        
        if has_income_interest:
            form_scheduleb_line_2 = calculate_form_scheduleb_line_2()
        
        form_1040_line_6b = calculate_form_1040_line_6b()
        
        
        calculate_form_schedule1()
        form_1040_line_8 = form_schedule1_line_10
        form_1040_line_9 = calculate_form_1040_line_9()
        form_1040_line_10 = form_schedule1_line_26
        form_1040_line_11 = calculate_form_1040_line_11()
        form_1040_line_12 = calculate_form_1040_line_12()
        
        form_1040_line_14 = form_1040_line_12
        
        form_1040_line_15 = calculate_form_1040_line_15()
        form_1040_line_16 = calculate_form_1040_line_16()
        form_1040_line_18 = form_1040_line_16

    def calculate_return_up_to_8863():
        global edu_credit_eligible, has_excess_social_security_to_claim
        calculate_return_up_to_agi()
        determine_if_eligible_for_aoc_vs_lllc()
        if edu_credit_eligible:
            calculate_form_8863()
        
        determine_if_has_excess_social_security()
        if edu_credit_eligible or has_excess_social_security_to_claim:
            calculate_form_schedule3()

    def calculate_form_8863():
        global education_tax_credit, claiming_aoc, claiming_lllc, form_8863_line_27, aoc_qualified_educational_expenses, form_8863_line_28, form_8863_line_29, form_8863_line_30, form_8863_line_31, form_8863_line_3, form_1040_line_11, form_8863_line_4, form_8863_line_2, ineligible_for_edu_credits, form_8863_line_5, form_8863_line_6, form_8863_line_7, form_8863_line_7_box, aoc_refundable_eligible, form_8863_line_8, form_8863_line_9, form_8863_line_10, form_8863_line_11, form_8863_line_12, form_8863_line_13, form_8863_line_14, form_8863_line_15, form_8863_line_16, form_8863_line_17, form_8863_line_18, form_8863_line_19
        if claiming_aoc:
            form_8863_line_27 = convert_to_dollar_amount(max(0, (aoc_qualified_educational_expenses or 0)))
            form_8863_line_28 = convert_to_dollar_amount(max(0, form_8863_line_27 - 2000))
            form_8863_line_29 = convert_to_dollar_amount(form_8863_line_28 * 0.25)
            form_8863_line_30 = convert_to_dollar_amount((aoc_qualified_educational_expenses or 0) if form_8863_line_28 == 0 else form_8863_line_29 + 2000)
            form_8863_line_31 = 0
            form_8863_line_11 = 0
            form_8863_line_12 = 0
            form_8863_line_14 = 0
            form_8863_line_15 = 0
            form_8863_line_17 = 0
            form_8863_line_18 = 0
        elif claiming_lllc:
            form_8863_line_27 = 0
            form_8863_line_28 = 0
            form_8863_line_29 = 0
            form_8863_line_30 = 0
            form_8863_line_31 = convert_to_dollar_amount(min(10000, (aoc_qualified_educational_expenses or 0)))
        
        form_8863_line_3 = convert_to_dollar_amount(form_1040_line_11)
        form_8863_line_4 = convert_to_dollar_amount(form_8863_line_2 - form_8863_line_3)
        
        if form_8863_line_4 <= 0:
            ineligible_for_edu_credits = True
            education_tax_credit = 0
            form_8863_line_19 = 0
            form_8863_line_6 = 0
            form_8863_line_7 = 0
            form_8863_line_7_box = False
            form_8863_line_8 = 0
            form_8863_line_9 = 0
            form_8863_line_10 = 0
            form_8863_line_11 = 0
            form_8863_line_12 = 0
            form_8863_line_14 = 0
            form_8863_line_15 = 0
            form_8863_line_17 = 0
            form_8863_line_18 = 0
            form_8863_line_19 = 0
            return
        
        
        if form_8863_line_4 >= form_8863_line_5:
            form_8863_line_6 = round(1.0, 3)
        else:
            form_8863_line_6 = round(form_8863_line_4/form_8863_line_5, 3)
        
        
        form_8863_line_7 = convert_to_dollar_amount(form_8863_line_30 * form_8863_line_6)
        
        form_8863_line_7_box = False
        
        
        if not (claiming_aoc and not aoc_refundable_eligible):
            form_8863_line_8 = convert_to_dollar_amount(form_8863_line_7 * 0.4)
        else:
            form_8863_line_7_box = True
            form_8863_line_8 = 0
        
        form_8863_line_9 = convert_to_dollar_amount(form_8863_line_7 - form_8863_line_8)
        form_8863_line_10 = convert_to_dollar_amount(form_8863_line_31)
        
        if form_8863_line_31 > 0:
            form_8863_line_11 = convert_to_dollar_amount(min(form_8863_line_10, 10000))
            form_8863_line_12 = convert_to_dollar_amount(form_8863_line_11 * 0.2)
            
            form_8863_line_14 = form_1040_line_11
            form_8863_line_15 = form_8863_line_13 - form_8863_line_14
            
            if form_8863_line_15 > 0:
                form_8863_line_17 = 1.000 if form_8863_line_15 >= form_8863_line_16 else round(form_8863_line_15/form_8863_line_16, 3)
                form_8863_line_18 = convert_to_dollar_amount(form_8863_line_12 * form_8863_line_17)
        
        
        cl_val_1 = form_8863_line_18 + form_8863_line_9
        
        
        cl_val_2 = form_1040_line_18
        
        form_8863_line_19 = convert_to_dollar_amount(min(cl_val_1, cl_val_2))
        education_tax_credit = convert_to_dollar_amount(form_8863_line_8 + form_8863_line_19)

    def calculate_form_schedule3():
        global form_schedule3_line_11, form_schedule3_line_15, w2_objects, max_social_security_tax_this_year, w2_box_4_totals
        
        if has_excess_social_security_to_claim:
            w2_box_4_totals = convert_to_dollar_amount(get_total_w2_box_4())
            form_schedule3_line_11 = convert_to_dollar_amount(max_social_security_tax_this_year - w2_box_4_totals)
        
        form_schedule3_line_15 = convert_to_dollar_amount(form_schedule3_line_11)

    def calculate_form_schedule1():
        global form_1040_line_8, form_1040_line_9, form_schedule1_line_10, form_schedule1_line_11, form_schedule1_line_26, unemployment_compensation, form_schedule1_line_7, form_schedule1_line_20, form_schedule1_line_21
        form_schedule1_line_7 = convert_to_dollar_amount(unemployment_compensation or 0)
        form_schedule1_line_10 = convert_to_dollar_amount(form_schedule1_line_7)
        form_1040_line_8 = form_schedule1_line_10
        form_1040_line_9 = calculate_form_1040_line_9()
        form_schedule1_line_11 = calculate_form_schedule1_line_11()
        form_schedule1_line_20 = calculate_form_schedule1_line_20()
        form_schedule1_line_21 = calculate_form_schedule1_line_21()
        
        form_schedule1_line_26 = convert_to_dollar_amount(form_schedule1_line_11 + form_schedule1_line_20 + form_schedule1_line_21)

    def calculate_form_schedule1_magi(omit_21=False, omit_20=False):
        global form_1040_line_9, nontaxable_combat_pay_election, form_schedule1_line_11, form_schedule1_line_20, form_schedule1_line_21
        s1_line_26 = form_schedule1_line_11
        if not omit_20:
            s1_line_26 = s1_line_26 + form_schedule1_line_20
        if not omit_21:
            s1_line_26 = s1_line_26 + form_schedule1_line_21
        
        magi = form_1040_line_9 + (nontaxable_combat_pay_election or 0) - s1_line_26
        return magi

    def calculate_form_schedule1_line_11():
        global educator_expenses
        return min(educator_expenses or 0, 300)

    def calculate_form_schedule1_line_20():
        global form_1040_line_1a, tax_deferred_ira_contributions, nontaxable_combat_pay_election, age, is_covered_by_employer_retirement_plan
        
        if form_1040_line_1a <= 0:
            return 0
        magi = calculate_form_schedule1_magi(omit_20=True, omit_21=True)
        if (not is_covered_by_employer_retirement_plan and age < 50) or (is_covered_by_employer_retirement_plan and age < 50 and magi < 68000):
            return convert_to_dollar_amount(min(6000, tax_deferred_ira_contributions or 0))
        elif (not is_covered_by_employer_retirement_plan and age >= 50) or (is_covered_by_employer_retirement_plan and age >= 50 and magi < 68000):
            return convert_to_dollar_amount(min(7000, tax_deferred_ira_contributions or 0))
        elif is_covered_by_employer_retirement_plan:
            if magi >= 78000:
                return 0
            elif magi >= 68000 and magi < 78000:
                val_6a = 6000 if age < 50 else 7000
                val_7 = val_6a * (0.6 if age < 50 else 0.7)
                
                val_8 = form_1040_line_1a + (nontaxable_combat_pay_election or 0)
                return convert_to_dollar_amount(min([tax_deferred_ira_contributions or 0,val_7,val_8]))

    def calculate_form_schedule1_line_21():
        global student_loan_interest
        sl_val_1 = min((student_loan_interest or 0), 2500)
        magi = calculate_form_schedule1_magi(omit_21=True)
        if magi >= 85000:
            return 0
        elif magi <= 70000:
            return sl_val_1
        else:
            
            val_11a = magi - 70000
            val_11ai = round(val_11a/15000, 3)
            val_11aii = sl_val_1 * val_11ai
            return convert_to_dollar_amount(sl_val_1 - val_11aii)

    def calculate_form_scheduleb_line_2():
        global form_1040_line_2b
        return form_1040_line_2b

    def calculate_form_1040_line_1z():
        
        global form_1040_line_1a, household_empoloyee_wages_not_reported_on_w2
        return convert_to_dollar_amount((form_1040_line_1a or 0) + (household_empoloyee_wages_not_reported_on_w2 or 0))

    def calculate_form_1040_line_2a():
        global int_1099_objects
        total_amount = 0
        for obj in int_1099_objects:
            total_amount += obj.get_tax_exempt_interest()
        
        return convert_to_dollar_amount(total_amount)

    def calculate_form_1040_line_2b():
        global int_1099_objects
        total_amount = 0
        for obj in int_1099_objects:
            total_amount += obj.get_taxable_interest()
        
        return convert_to_dollar_amount(total_amount)

    def calculate_form_1040_line_6b():
        global social_security_taxable_amount, form_1040_line_1z, form_1040_line_2a, form_1040_line_2b, educator_expenses, tax_deferred_ira_contributions
        
        
        ss_value_1 = ((social_security_taxable_amount or 0) * 0.5) + form_1040_line_1z + (form_1040_line_2a or 0) + (form_1040_line_2b or 0)
        
        
        ss_value_2 = (educator_expenses or 0) + (tax_deferred_ira_contributions or 0)
        
        single_filers_ss_base_amount = 25000
        ss_value_3 = ss_value_1 - ss_value_2
        if ss_value_2 > ss_value_1 or single_filers_ss_base_amount > ss_value_3:
            return 0
        else:
            ss_value_4 = ss_value_3 - single_filers_ss_base_amount
            ss_value_5 = max(ss_value_4 - 9000, 0)
            
            ss_value_6 = min(ss_value_4, 9000) * 0.5
            ss_value_7 = ss_value_5 * 0.85
            
            
            ss_value_8 = min((social_security_taxable_amount or 0) * 0.5, ss_value_6) + ss_value_7
            
            
            return round(min(ss_value_8, (social_security_taxable_amount or 0) * 0.85), 2)

    def calculate_form_1040_line_9():
        global form_1040_line_1z, form_1040_line_2b, form_1040_line_6b, form_1040_line_8
        
        return round(form_1040_line_1z + (form_1040_line_2b or 0) + form_1040_line_6b + form_1040_line_8, 2)

    def calculate_form_1040_line_11():
        global form_1040_line_9, form_1040_line_10
        
        return convert_to_dollar_amount(form_1040_line_9 - form_1040_line_10)

    def calculate_form_1040_line_12():
        global someone_can_claim_as_dependent, is_blind, age, form_1040_line_1z
        base_standard_deduction = 12950
        if not someone_can_claim_as_dependent and not is_blind:
            if age < 65:
                return base_standard_deduction
            else:
                return base_standard_deduction + 1750
        elif someone_can_claim_as_dependent and not is_blind:
            if age < 65:
                return max(min(base_standard_deduction, form_1040_line_1z + 400), 1150)
            else:
                return max(min(base_standard_deduction, form_1040_line_1z + 400), 1150) + 1750
        elif not someone_can_claim_as_dependent and is_blind:
            if age < 65:
                return base_standard_deduction + 1750 
            else:
                return base_standard_deduction + 1750 + 1750
        else:
            
            if age < 65:
                return max(min(base_standard_deduction, form_1040_line_1z + 400), 1150) + 1750
            else:
                return max(min(base_standard_deduction, form_1040_line_1z + 400), 1150) + 1750 + 1750

    def calculate_form_1040_line_15():
        global form_1040_line_11, form_1040_line_14
        
        return convert_to_dollar_amount(max(0, form_1040_line_11 - form_1040_line_14))

    def calculate_form_1040_line_16():
        global form_1040_line_15, TAX_TABLE
        
        if form_1040_line_15 < 100000:
            return convert_to_dollar_amount(TAX_TABLE.get_value_for_number(form_1040_line_15))
        elif form_1040_line_15 >= 100000 and form_1040_line_15 <= 170050:
            return round((form_1040_line_15 * 0.24) - 6164.5, 2)
        elif form_1040_line_15 > 170050 and form_1040_line_15 <= 215950:
            return round((form_1040_line_15 * 0.32) - 19768.5, 2)
        elif form_1040_line_15 > 215950 and form_1040_line_15 <= 539900:
            return round((form_1040_line_15 * 0.35) - 26247, 2)
        else:
            return round((form_1040_line_15 * 0.37) - 37045, 2)

    def calculate_form_1040_line_20():
        global form_8863_line_19
        
        return convert_to_dollar_amount(form_8863_line_19)

    def calculate_form_1040_line_21():
        global form_1040_line_20, form_1040_line_19
        return convert_to_dollar_amount(form_1040_line_20 + form_1040_line_19)

    def calculate_form_1040_line_22():
        global form_1040_line_18, form_1040_line_21
        return convert_to_dollar_amount(max(form_1040_line_18 - form_1040_line_21, 0))

    def calculate_form_1040_line_24():
        global form_1040_line_22, form_1040_line_23
        return convert_to_dollar_amount(form_1040_line_22 + form_1040_line_23)

    def calculate_form_1040_line_25b():
        global unemployment_compensation_tax_witheld
        return convert_to_dollar_amount(get_total_1099_int_box_4() + (unemployment_compensation_tax_witheld or 0))

    def calculate_form_1040_line_25d():
        global federal_income_tax_witheld_from_w2, form_1040_line_25b
        
        return convert_to_dollar_amount(federal_income_tax_witheld_from_w2 + form_1040_line_25b)

    def calculate_1040_line_26():
        global estimated_tax_payments, amount_applied_from_previous_year
        return convert_to_dollar_amount((estimated_tax_payments or 0) + (amount_applied_from_previous_year or 0))

    def calculate_form_1040_line_27():
        global qualifies_for_eitc, form_1040_line_1z, form_1040_line_11, EIC_TABLE, nontaxable_combat_pay_election
        determine_if_eligible_for_eitc()
        if qualifies_for_eitc:
            value_1 = form_1040_line_1z + (nontaxable_combat_pay_election or 0)
            value_2 = EIC_TABLE.get_value_for_number(value_1)
            
            if value_2 == 0:
                return 0
            
            value_3 = form_1040_line_11
            if value_3 == value_1 or value_3 < 9200:
                return convert_to_dollar_amount(min(560, value_2))
            
            value_4 = EIC_TABLE.get_value_for_number(value_3)
            return convert_to_dollar_amount(min(560, value_4, value_2))
        else:
            return 0

    def calculate_form_1040_line_29():
        global form_8863_line_8
        return convert_to_dollar_amount(form_8863_line_8)

    def calculate_form_1040_line_31():
        
        return convert_to_dollar_amount(0)

    def calculate_form_1040_line_32():
        
        global form_1040_line_27, form_1040_line_29, form_1040_line_31
        return convert_to_dollar_amount(form_1040_line_27 + form_1040_line_29 + form_1040_line_31)

    def calculate_form_1040_line_33():
        global form_1040_line_25d, estimated_tax_payments_and_amount_applied_from_prev_year, form_1040_line_32
        
        return convert_to_dollar_amount(form_1040_line_25d + (estimated_tax_payments_and_amount_applied_from_prev_year or 0) + form_1040_line_32)

    def calculate_form_1040_line_34():
        global form_1040_line_33, form_1040_line_24
        return convert_to_dollar_amount(max(form_1040_line_33 - form_1040_line_24, 0))

    def calculate_form_1040_line_37():
        global form_1040_line_33, form_1040_line_24
        return convert_to_dollar_amount(max(form_1040_line_24 - form_1040_line_33, 0))

    def determine_if_eligible_for_eitc():
        global form_1040_line_1z, resided_in_us_for_more_than_half_the_year, someone_can_claim_as_dependent, qualifies_for_eitc, form_1040_line_11, age
        form_1040_line_1z = calculate_form_1040_line_1z()
        
        if form_1040_line_1z <= 0.01 or (not resided_in_us_for_more_than_half_the_year) or someone_can_claim_as_dependent or (age >= 65 or age < 25) or (form_1040_line_11 >= 16480):
            qualifies_for_eitc = False 
        else:
            qualifies_for_eitc = True 

    def determine_if_eligible_for_aoc_vs_lllc():
        global aoc_schools, form_1040_line_11, edu_credit_eligible, someone_can_claim_as_dependent, was_a_student, aoc_pursued_a_program_leading_to_degree, student_status, HALF_TIME_CHOICE, FULL_TIME_CHOICE, aoc_claimed_last_four_years, aoc_first_four_years_completed_before_this_year, aoc_has_been_convicted, aoc_eligible, claiming_aoc, claiming_lllc, aoc_refundable_eligible, aoc_refundable_parents_alive, aoc_refundable_earned_income_half_of_support, age
        
        if not was_a_student or not paid_tuition_or_qualified_expenses or form_1040_line_11 >= 90000 or someone_can_claim_as_dependent:
            edu_credit_eligible = False
            claiming_aoc = False
            claiming_lllc = False
            aoc_refundable_eligible = False
        else:
            edu_credit_eligible = True
            
            any_school_has_no_ein = False
            for school in aoc_schools:
                if school.ein == "" or school.ein == None:
                    any_school_has_no_ein = True
            
            if student_status in [HALF_TIME_CHOICE, FULL_TIME_CHOICE]  and aoc_pursued_a_program_leading_to_degree and not aoc_claimed_last_four_years and not aoc_first_four_years_completed_before_this_year and not aoc_has_been_convicted and (aoc_claimed_last_four_years is not None) and (aoc_first_four_years_completed_before_this_year is not None) and (aoc_has_been_convicted is not None) and not any_school_has_no_ein:
                aoc_eligible = True
                claiming_aoc = True
                claiming_lllc = False
                if age < 18 and not aoc_refundable_parents_alive:
                    aoc_refundable_eligible = True
                elif age >= 24 or (age >= 18 and age < 24 and student_status != FULL_TIME_CHOICE):
                    aoc_refundable_eligible = True
                elif age < 24 and age >= 18 and (aoc_refundable_parents_alive == False or aoc_refundable_earned_income_half_of_support):
                    aoc_refundable_eligible = True
                else:
                    aoc_refundable_eligible = False
            else:
                aoc_eligible = False
                claiming_aoc = False
                aoc_refundable_eligible = False
                claiming_lllc = True

    def determine_if_has_excess_social_security():
        global has_excess_social_security_to_claim, max_social_security_tax_this_year, form_schedule3_line_11
        has_excess_social_security_to_claim = False
        w2_box_4_totals = 0
        
        
        for w2 in w2_objects:
            box_4 = w2.get_box_4()
            if box_4 > max_social_security_tax_this_year:
                has_excess_social_security_to_claim = False
                form_schedule3_line_11 = 0
                return
            else:
                w2_box_4_totals += box_4
        
        if w2_box_4_totals > max_social_security_tax_this_year:
            has_excess_social_security_to_claim = True
        
        if not has_excess_social_security_to_claim:
            form_schedule3_line_11 = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
