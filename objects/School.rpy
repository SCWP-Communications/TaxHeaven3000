init python:
    global object_class_name_mappings
    class School:
        def __init__(self):
            self.name = ""
            self.line_1 = ""
            self.line_2 = ""
            self.city = ""
            self.state = ""
            self.zip = ""
            self.ein = ""
            self.did_receive_1098t_this_year = None
            self.did_receive_1098t_previous_year_box_7 = None

    object_class_name_mappings.update({"School": School})
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
