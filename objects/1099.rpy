init python:
    class Int1099:
        def __init__(self):
            self.payer_name = ""
            self.total_interest = None 
            self.tax_exempt_interest = None 
            self.federal_income_tax_witheld = None 
        
        def set_payer_name(self, val):
            self.payer_name = val
        
        def set_total_interest(self, val):
            self.total_interest = val
        
        def set_tax_exempt_interest(self, val):
            self.tax_exempt_interest = val
        
        def set_federal_income_tax_witheld(self, val):
            self.federal_income_tax_witheld = val
        
        def get_payer_name(self):
            return self.payer_name
        
        def get_taxable_interest(self):
            return self.total_interest or 0
        
        def get_total_interest(self):
            return self.total_interest or 0
        
        def get_tax_exempt_interest(self):
            return self.tax_exempt_interest or 0
        
        def get_federal_income_tax_witheld(self):
            return self.federal_income_tax_witheld or 0

    def get_total_1099_int_box_4():
        global int_1099_objects
        total = 0
        for obj in int_1099_objects:
            total += obj.get_federal_income_tax_witheld()
        return total

    def get_total_1099_int_box_1():
        global int_1099_objects
        total = 0
        for obj in int_1099_objects:
            total += obj.get_total_interest()
        return total

    def get_total_1099_int_taxable_interest():
        global int_1099_objects
        total = 0
        for obj in int_1099_objects:
            total += obj.get_taxable_interest()
        return total

    object_class_name_mappings.update({"Int1099": Int1099})
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
