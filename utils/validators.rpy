init python:
    global CHANGED_FUNCTIONS
    import re
    phone_expression = re.compile('[0-9]\d\d-\d\d\d-\d\d\d\d$')
    email_expression = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")
    ssn_expression = re.compile("^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$")
    ein_expression = re.compile("^\\d{2}-{1}\\d{7}$")

    def validate_and_save_routing_number(value=""):
        global routing_number
        if not value.isnumeric():
            add_error("routing_number", "Invalid routing number")
        elif len(value) != 9:
            add_error("routing_number", "Routing number must be 9 characters")
        else:
            clear_error_by_id("routing_number")
        routing_number = value
        
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed="routing_number", evaluate_all=False)
        
        renpy.restart_interaction()
    def validate_and_save_account_number(value=""):
        global bank_account_number
        if not value.isnumeric():
            add_error("bank_account_number", "Invalid account number")
        elif len(value) > 17:
            add_error("bank_account_number", "Account number is too long")
        elif len(value) == 0:
            add_error("bank_account_number", "Account number is required")
        else:
            clear_error_by_id("bank_account_number")
        bank_account_number = value
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed="bank_account_number", evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_active_input_number_of_days(value=""):
        global active_input_field_id
        
        if not value.isnumeric():
            add_error(active_input_field_id, 'Invalid number')
            globals()[active_input_field_id] = None
        elif int(value) < 0 or int(value) > 365:
            add_error(active_input_field_id, 'Invalid number of days')
            globals()[active_input_field_id] = int(value)
        else:
            clear_error_by_id(active_input_field_id)
            globals()[active_input_field_id] = int(value)
        
        renpy.restart_interaction()

    def validate_and_save_active_input_array_property(value=""):
        clear_error_by_id(active_input_field_id)
        
        set_value_array_property(active_input_field_id, value)
        
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        
        renpy.restart_interaction()

    def validate_and_save_active_input_property(value=""):
        clear_error_by_id(active_input_field_id)
        
        set_value_property(active_input_field_id, value)
        
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        
        renpy.restart_interaction()

    def validate_and_save_active_input_required_array_property(value=""):
        
        if value is not "":
            clear_error_by_id(active_input_field_id)
            set_value_array_property(active_input_field_id, value.strip())
        else:
            add_error(active_input_field_id, "This field is required")
            set_value_array_property(active_input_field_id, "")
        
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        
        renpy.restart_interaction()

    def validate_and_save_active_input_required_property(value=""):
        if value is not "":
            clear_error_by_id(active_input_field_id)
            set_value_property(active_input_field_id, value.strip())
        else:
            add_error(active_input_field_id, "This field is required")
            set_value_property(active_input_field_id, "")
        
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        
        renpy.restart_interaction()

    def validate_and_save_phone_number(value="", evaluate_all=False):
        global phone_number
        
        if re.fullmatch(phone_expression, value) is None:
            add_error('phone_number', "Must be in format XXX-XXX-XXXX")
        else:
            clear_error_by_id('phone_number')
        
        phone_number = value
        
        if in_diary and not evaluate_all:
            evaluate_errors_and_add_diary_pages(changed="phone_number", evaluate_all=False)
        
        renpy.restart_interaction()

    def validate_and_save_email(value=""):
        global email
        
        if re.fullmatch(email_expression, value) is None:
            add_error('email', "Invalid email")
        else:
            clear_error_by_id('email')
        
        email = value
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed="email", evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_active_input_state_array_prop(value=""):
        if value.upper() not in us_states:
            add_error(active_input_field_id, "Invalid state code")
        else:
            clear_error_by_id(active_input_field_id)
        
        set_value_array_property(active_input_field_id, value.upper())
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_active_input_state_prop(value="", evaluate_all=False):
        if value.upper() not in us_states:
            add_error(active_input_field_id, "Invalid state code")
        else:
            clear_error_by_id(active_input_field_id)
        
        set_value_property(active_input_field_id, value.upper())
        
        if in_diary and not evaluate_all:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_active_input_zip_array_prop(value=""):
        if len(value) is not 5 or not value.isnumeric():
            add_error(active_input_field_id, "Invalid zip code")
        else:
            clear_error_by_id(active_input_field_id)
        set_value_array_property(active_input_field_id, value)
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_active_input_zip_prop(value="", evaluate_all=False):
        if len(value) is not 5 or not value.isnumeric():
            add_error(active_input_field_id, "Invalid zip code")
        else:
            clear_error_by_id(active_input_field_id)
        set_value_property(active_input_field_id, value)
        if in_diary and not evaluate_all:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_active_input_state(value=""):
        if value not in us_states:
            add_error(active_input_field_id, "Invalid state code")
        else:
            clear_error_by_id(active_input_field_id)
        
        globals()[active_input_field_id] = value
        renpy.restart_interaction()

    def validate_and_save_active_input_zip(value=""):
        if len(value) is not 5 or not value.isnumeric():
            add_error(active_input_field_id, "Invalid zip code")
        else:
            clear_error_by_id(active_input_field_id)
        
        globals()[active_input_field_id] = value
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_ssn(value="", evaluate_all=False):
        global social_security_number
        
        if re.fullmatch(ssn_expression, value) is None:
            add_error('social_security_number', "Should be in format XXX-XX-XXXX")
        else:
            clear_error_by_id('social_security_number')
        
        social_security_number = value
        if in_diary and not evaluate_all:
            evaluate_errors_and_add_diary_pages(changed="social_security_number", evaluate_all=False)
        renpy.restart_interaction() 

    def validate_and_save_dollar_active_field(value=""):
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
            if in_diary:
                evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        else:
            if round(float(value), 2) != globals()[active_input_field_id]:
                clear_error_by_id(active_input_field_id)
                globals()[active_input_field_id] = round(float(value), 2)
                if in_diary:
                    evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_dollar_active_field_array_property(value=""):        
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            set_value_array_property(active_input_field_id, None)
            if in_diary:
                evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        else:
            if round(float(value), 2) != get_value_array_property(active_input_field_id):
                clear_error_by_id(active_input_field_id)
                set_value_array_property(active_input_field_id, round(float(value), 2))
                
                if in_diary:
                    evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def set_value_array_property(value_name_string, value):
        try:
            (value_name, idx, attr) = get_value_name_idx_attr_from_str(value_name_string)
            setattr(globals()[value_name][idx], attr, value)
        except Exception:
            return

    def set_value_property(value_name_string, value):
        try:
            (value_name, attr) = get_value_name_attr_from_str(value_name_string)
            setattr(globals()[value_name], attr, value)
            renpy.log(getattr(globals()[value_name], attr))
        except Exception:
            return

    def validate_and_save_dollar_active_field_less_than_4000(value=""):
        value_changed = False
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
            value_changed = True
        elif float(value) > 4000:
            if float(value) != globals()[active_input_field_id]:
                add_error(active_input_field_id, "Value cannot exceed 4000")
                globals()[active_input_field_id] = round(float(value), 2)
                value_changed = True
        else:
            if float(value) != globals()[active_input_field_id]:
                clear_error_by_id(active_input_field_id)
                globals()[active_input_field_id] = round(float(value), 2)
                value_changed = True
        
        if in_diary and value_changed:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_dollar_active_field_less_than_10000(value=""):
        value_changed = False
        if not value.replace('.','',1).isdigit():
            value_changed = True
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
        elif float(value) > 10000:
            if float(value) != globals()[active_input_field_id]:
                value_changed = True
                add_error(active_input_field_id, "Value cannot exceed 10000")
                globals()[active_input_field_id] = round(float(value), 2)
        else:
            if float(value) != globals()[active_input_field_id]:
                value_changed = True
                clear_error_by_id(active_input_field_id)
                globals()[active_input_field_id] = round(float(value), 2)
        
        if in_diary and value_changed:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_dollar_active_field_less_than_limit(value="", evaluate_all=False):
        value_changed = False
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
            value_changed = True
        else:
            if float(value) != globals()[active_input_field_id]:
                clear_error_by_id(active_input_field_id)
                value_changed = True
                globals()[active_input_field_id] = round(float(value), 2)
                
                limit = dollar_active_field_limits.get(active_input_field_id, None)
                if limit is not None:
                    if float(value) >= limit:
                        add_error(active_input_field_id, f"Must be less than {limit}")
        
        if in_diary and not evaluate_all and value_changed:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_dollar_active_field_less_than_equal_to_limit(value="", evaluate_all=False):
        value_changed = False
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
            value_changed = True
        else:
            if float(value) != globals()[active_input_field_id]:
                value_changed = True
                clear_error_by_id(active_input_field_id)
                globals()[active_input_field_id] = round(float(value), 2)
                
                limit = dollar_active_field_limits.get(active_input_field_id, None)
                if limit is not None:
                    if float(value) > limit:
                        add_error(active_input_field_id, f"Value cannot exceed {limit}")
        if in_diary and not evaluate_all and value_changed:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()  

    def validate_and_save_dollar_active_field_less_than_refund_amount(value=""):
        value_changed = False
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
            value_changed = True
        elif float(value) > refund:
            if float(value) != globals()[active_input_field_id]:
                add_error(active_input_field_id, "Must be less than {0:.2f}".format(refund))
                globals()[active_input_field_id] = round(float(value), 2)
                value_changed = True
        else:
            if float(value) != globals()[active_input_field_id]:
                clear_error_by_id(active_input_field_id)
                globals()[active_input_field_id] = round(float(value), 2)
                value_changed = True
        if in_diary and value_changed:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def save_value_active_input(value=""):
        clear_error_by_id(active_input_field_id)
        globals()[active_input_field_id] = value
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def save_value_active_input_required(value=""):
        global variable_change_callbacks
        if value == "":
            try:
                add_error(active_input_field_id, f"{VALUE_DISPLAY_NAMES[active_input_field_id]} is required")
            except Exception:
                add_error(active_input_field_id, "This field is required")
        else:
            clear_error_by_id(active_input_field_id)
        globals()[active_input_field_id] = value.strip()
        callback = variable_change_callbacks.get(active_input_field_id, None)
        if callback is not None:
            callback()
        
        if in_diary:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_birth_date(value="", evaluate_all=False):
        global birth_date, age
        renpy.dynamic("value_date", "today")
        
        value_date = convert_string_to_date(value)
        if value_date == None:
            add_error("birth_date", "Invalid date in format MM/DD/YYYY")
        else:
            clear_error_by_id("birth_date")
            today = datetime.date.today()
            
            if value_date > today:
                add_error("birth_date", "Invalid birth date")
            
            birth_date = value_date
            age = get_age_at_end_of_tax_year_from_birth_date(birth_date)
            
            if in_diary and not evaluate_all:
                evaluate_errors_and_add_diary_pages(changed="birth_date", evaluate_all=False)
        
        renpy.restart_interaction()

    def validate_and_save_ein_active_field_array_prop(value="", evaluate_all=False):
        if value != "":
            if re.fullmatch(ein_expression, value) is None:
                add_error(active_input_field_id, "Should be in format XX-XXXXXXX")
            else:
                clear_error_by_id(active_input_field_id)
        else:
            clear_error_by_id(active_input_field_id)
        
        set_value_array_property(active_input_field_id, value)
        if in_diary and not evaluate_all:
            evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()

    def validate_and_save_ira_contribution_active_field(value=""):
        global age, MAX_IRA_CONTRIBUTION_UNDER_50, MAX_IRA_CONTRIBUTION_50_OR_OVER, form_1040_line_11
        
        if not value.replace('.','',1).isdigit():
            add_error(active_input_field_id, "Invalid dollar amount")
            globals()[active_input_field_id] = None
            renpy.restart_interaction()
            return
        
        total_amount_w2_box_1 = get_total_w2_box_1()
        value_float = round(float(value), 2)
        if form_1040_line_11 >= 78000 and is_covered_by_employer_retirement_plan:
            
            if value_float != globals()[active_input_field_id]:
                clear_error_by_id(active_input_field_id)
            pass
        elif value_float > MAX_IRA_CONTRIBUTION_UNDER_50 and age < 50:
            add_error(active_input_field_id, f"Value must be {MAX_IRA_CONTRIBUTION_UNDER_50} or less")
        elif value_float > MAX_IRA_CONTRIBUTION_50_OR_OVER and age >= 50:
            add_error(active_input_field_id, f"Value must be {MAX_IRA_CONTRIBUTION_50_OR_OVER} or less")
        else:
            if value_float != globals()[active_input_field_id]:
                clear_error_by_id(active_input_field_id)
        
        if value_float != globals()[active_input_field_id]:
            globals()[active_input_field_id] = value_float
            if in_diary:
                evaluate_errors_and_add_diary_pages(changed=active_input_field_id, evaluate_all=False)
        renpy.restart_interaction()


    CHANGED_FUNCTIONS = {"save_value_active_input_required": save_value_active_input_required, "save_value_active_input": save_value_active_input, "validate_and_save_ssn": validate_and_save_ssn, "validate_and_save_active_input_state": validate_and_save_active_input_state, "validate_and_save_active_input_zip": validate_and_save_active_input_zip, "validate_and_save_dollar_active_field": validate_and_save_dollar_active_field, "validate_and_save_ira_contribution_active_field": validate_and_save_ira_contribution_active_field, "validate_and_save_email": validate_and_save_email, "validate_and_save_birth_date": validate_and_save_birth_date, "validate_and_save_ssn": validate_and_save_ssn, "validate_and_save_ein_active_field_array_prop": validate_and_save_ein_active_field_array_prop, "validate_and_save_phone_number": validate_and_save_phone_number, "validate_and_save_dollar_active_field_array_property": validate_and_save_dollar_active_field_array_property, "validate_and_save_active_input_array_property": validate_and_save_active_input_array_property, "validate_and_save_active_input_state_array_prop": validate_and_save_active_input_state_array_prop, "validate_and_save_active_input_zip_array_prop":validate_and_save_active_input_zip_array_prop, "validate_and_save_active_input_required_array_property": validate_and_save_active_input_required_array_property, "validate_and_save_dollar_active_field_less_than_refund_amount": validate_and_save_dollar_active_field_less_than_refund_amount, "validate_and_save_active_input_zip_prop": validate_and_save_active_input_zip_prop, "validate_and_save_active_input_state_prop": validate_and_save_active_input_state_prop, "validate_and_save_active_input_required_property": validate_and_save_active_input_required_property, "validate_and_save_active_input_property": validate_and_save_active_input_property, "validate_and_save_account_number": validate_and_save_account_number, "validate_and_save_routing_number": validate_and_save_routing_number, "validate_and_save_dollar_active_field_less_than_10000": validate_and_save_dollar_active_field_less_than_10000, "validate_and_save_dollar_active_field_less_than_4000": validate_and_save_dollar_active_field_less_than_4000, "validate_and_save_dollar_active_field_less_than_limit": validate_and_save_dollar_active_field_less_than_limit, "validate_and_save_dollar_active_field_less_than_equal_to_limit": validate_and_save_dollar_active_field_less_than_equal_to_limit}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
