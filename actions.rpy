init python:
    class SubmitNameEntry(Action):
        def __call__(self):
            global first_name, last_name
            clear_errors()
            if first_name == "":
                add_error('first_name', "You must enter a first name!")
                renpy.restart_interaction()
            elif last_name == "":
                add_error('last_name', "You must enter a last name!")
                renpy.restart_interaction()
            else:
                clear_errors()
                renpy.jump_out_of_context("start")

    class SetVariableOption(Action):
        def __init__(self, variable_name, value, in_diary=False):
            self.value = value
            self.variable_name = variable_name
            self.in_diary = in_diary
        
        def __call__(self):
            setattr(globals(), "active_input_field_id", None)
            globals()[self.variable_name] = self.value
            clear_error_by_id(self.variable_name)
            if self.in_diary:
                evaluate_errors_and_add_diary_pages(changed=self.variable_name, evaluate_all=False)
            
            renpy.restart_interaction()

    class SetVariableMultipleOption(Action):
        def __init__(self, variable_name, value):
            self.value = value
            self.variable_name = variable_name
        
        def __call__(self):
            setattr(globals(), "active_input_field_id", None)
            if globals()[self.variable_name] == None:
                globals()[self.variable_name] = []
            
            
            if (self.value == WHAT_CHOICE and self.value not in globals()[self.variable_name]):
                globals()[self.variable_name] = []
            elif (self.value != WHAT_CHOICE and WHAT_CHOICE in globals()[self.variable_name]):
                globals()[self.variable_name].remove(WHAT_CHOICE)
            
            if self.value in globals()[self.variable_name]:
                globals()[self.variable_name].remove(self.value)
            else:
                globals()[self.variable_name].append(self.value)
            
            clear_errors()
            renpy.restart_interaction()

    class SetVariableArrayPropOption(Action):
        def __init__(self, variable_name_string, value, in_diary=False):
            self.value = value
            self.variable_name_string = variable_name_string
            (value_name, idx, attr) = get_value_name_idx_attr_from_str(variable_name_string)
            
            self.value_name = value_name
            self.idx = idx
            self.attr = attr
            
            self.in_diary = in_diary
        
        def __call__(self):
            setattr(globals(), "active_input_field_id", None)
            setattr(globals()[self.value_name][self.idx], self.attr, self.value)
            clear_error_by_id(self.variable_name_string)
            if self.in_diary:
                evaluate_errors_and_add_diary_pages(changed=self.variable_name_string, evaluate_all=False)
            renpy.restart_interaction()

    class ChangeDiaryPage(Action):
        def __init__(self, forwards=True):
            self.forwards = forwards
        
        def __call__(self):
            global _diary_page, _diary_section, diary_sections
            setattr(globals(), "active_input_field_id", None)
            if self.forwards:
                if _diary_page == len(diary_sections[_diary_section]["pages"]) - 1:
                    
                    if _diary_section != len(diary_sections) - 1:
                        _diary_page = 0
                        _diary_section += 1
                else:
                    
                    _diary_page = _diary_page + 1
            else:
                if _diary_page == 0:
                    
                    if _diary_section != 0:
                        _diary_section -= 1
                        _diary_page = len(diary_sections[_diary_section]["pages"]) - 1
                else:
                    _diary_page -= 1
            renpy.restart_interaction()

    class CustomAutoSave(Action):
        def __init__(self):
            return
        
        def __call__(self):
            purge_saves()
            renpy.notify("The game has been saved")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
