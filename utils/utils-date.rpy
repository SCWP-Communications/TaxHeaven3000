init python:
    import datetime

    def convert_string_to_date(date_string):
        try:
            return datetime.datetime.strptime(date_string, "%m/%d/%Y").date()
        except Exception as e:
            return None

    def get_age_at_end_of_tax_year_from_birth_date(_birth_date):
        renpy.dynamic("dec_31_tax_year")
        dec_31_tax_year = convert_string_to_date(f'12/31/{TAX_YEAR}')
        preliminary_age = dec_31_tax_year.year - _birth_date.year - ((dec_31_tax_year.month, dec_31_tax_year.day) < (_birth_date.month, _birth_date.day))
        
        if preliminary_age == 64 and _birth_date.month == 1 and _birth_date.day == 1:
            preliminary_age = 65
        
        return preliminary_age

    def get_age_today_from_birth_date(_birth_date):
        _todays_date = datetime.date.today()
        _age = _todays_date.year - _birth_date.year - ((_todays_date.month, _todays_date.day) < (_birth_date.month, _birth_date.day))
        
        return _age

    def convert_date_to_displayable_string(date_obj):
        return date_obj.strftime("%m/%d/%Y")

    def determine_was_born_before_jan_2_1958():
        if age >= 65:
            return True
        elif age == 64:
            if birth_date.month == 1 and birth_date.day == 1:
                return True
            else:
                return False
        else:
            return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
