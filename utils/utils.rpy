init python:
    import random
    def clear_errors():
        global error, error_message, error_messages, should_close_diary_error_modal
        error = False
        error_message = ""
        error_messages = {}
        if in_diary:
            should_close_diary_error_modal = True

    def clear_error_by_id(id):
        global error_messages, error, should_close_diary_error_modal
        had_previous_error_message = error_messages.pop(id, None)
        if error_messages == {}:
            error = False
            if in_diary and had_previous_error_message != None and had_previous_error_message and id != "screener_choice":
                should_close_diary_error_modal = True
        elif len(error_messages) == 1:
            if error_messages.get("screener_choice", None) != None and in_diary and had_previous_error_message != None:
                should_close_diary_error_modal = True

    def clear_error_by_key_substring(sub):
        global error_messages
        error_messages = {k:v for k,v in error_messages.items() if not sub in k}

    def add_error(id, message):
        global error, error_messages
        error = True
        error_messages.update({id: message})

    def get_error_message_by_id(id):
        global error_messages
        return error_messages.get(id)

    def add_warning(id, message):
        global warning, warning_messages
        warning = True
        warning_messages.update({id: message})

    def get_warning_messagee_by_id(id):
        global warning_messages
        return warning_messages.get(id, None)

    def clear_warning_by_id(id):
        global warning_messages, warning
        warning_messages.pop(id, None)
        if warning_messages == {}:
            warning = False

    def clear_warnings():
        global warning_messages, warning
        warning = False
        warning_messages = {}

    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def update_completed_dates():
        global dates_completed, library_visited, cafe_visited, office_visited, iris_home_visited
        dates_completed_sum = 1
        
        if library_visited:
            dates_completed_sum += 1
        
        if cafe_visited:
            dates_completed_sum += 1
        
        if office_visited:
            dates_completed_sum += 1
        
        if iris_home_visited:
            dates_completed_sum += 1
        
        dates_completed = dates_completed_sum

    def play_random_paper_sound():
        sound_to_play = random.randint(1, NUMBER_OF_PAGE_FLIP_SOUNDS)
        renpy.play(f"audio/diary/page_flip_{sound_to_play}.mp3", channel="sound")

    def format_full_name(first_name, middle_name, last_name):
        final_name = format_first_name_middle_initial(first_name, middle_name)
        final_name = final_name + f' {format_last_name(last_name)}'
        
        return final_name

    def format_first_name_middle_initial(first_name, middle_name):
        final_name = first_name.capitalize()
        
        if middle_name.replace(' ', '') != '':
            final_name = final_name + f' {middle_name.strip()[0].upper()}.'
        
        return final_name

    def format_last_name(last_name):
        return last_name.capitalize()

    def format_address_into_one_line(address_line_1, address_line_2, address_city, address_state, address_zip):
        return f'{address_line_1}{" " + address_line_2 if address_line_2 is not "" else ""}, {address_city}, {address_state} {address_zip}'

    def format_ein(ein):
        ein_arr = ein.split('-')
        if len(ein_arr) == 2:
            return (ein_arr[0], ein_arr[1])
        else:
            return ('', '')

    def format_ssn(ssn):
        return ssn.replace('-', '')

    def get_value_name_idx_attr_from_str(val):
        arr = re.split('[\[\]\.]+', val)
        value_name = arr[0]
        idx = int(arr[1])
        attr = arr[2]
        
        return (value_name, idx, attr)

    def get_value_name_attr_from_str(val):
        arr = val.split('.')
        value_name = arr[0]
        attr = arr[1]
        
        return (value_name, attr)

    def get_value_array_property(value_name_string):
        try:
            (value_name, idx, attr) = get_value_name_idx_attr_from_str(value_name_string)
            return getattr(globals()[value_name][idx], attr)
        except Exception:
            return None

    def get_value_property(value_name_string):
        try:
            (value_name, attr) = get_value_name_attr_from_str(value_name_string)
            return getattr(globals()[value_name], attr)
        except Exception as e:
            renpy.log(e)
            return None

    def disable_ctc_if_last_name_changed():
        global last_name, DUMMY_LAST_NAME, ctc_disabled
        if last_name == DUMMY_LAST_NAME or get_error_message_by_id('last_name') is not None:
            ctc_disabled = True
        else:
            ctc_disabled = False
        renpy.restart_interaction()

    def convert_to_dollar_amount(val):
        return round(val, 2)

    class NumberInputValue(InputValue):
        def __init__(self, var, default=True):
            self.var = var
            self.default = default
        
        def get_text(self):
            return str(globals()[self.var])
        
        def set_text(self, text):
            if(text != ""):
                globals()[self.var] = int(text)
        
        def enter(self):
            return globals()[self.var]

    def reenable_ctc_after_time(seconds=2.0):
        global ctc_disabled
        seconds = time.sleep(seconds)
        ctc_disabled = False

    def purge_saves():
        saves = renpy.list_slots()
        for save in saves:
            renpy.unlink_save(save)
        renpy.take_screenshot()
        renpy.save("1-1", save_name)
        return

    def get_ellipsized_value(value, max_length):
        try:
            val_str = str(value) if value != None else ""
            if len(val_str) > max_length:
                return f'{val_str[0:max_length]}...'
            else:
                return val_str
        except Exception:
            return ""

    def add_book_to_iris_desk():
        global iris_desk_books, books_iris_is_reading, number_of_books_on_iris_desk
        if number_of_books_on_iris_desk < len(iris_desk_books):
            number_of_books_on_iris_desk += 1
            books_iris_is_reading = iris_desk_books[0:number_of_books_on_iris_desk]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
