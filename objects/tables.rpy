init python:
    import csv
    global EIC_TABLE, TAX_TABLE
    TABLE_FOLDER = f'{renpy.config.gamedir}/tables'

    class Table:
        def __init__(self):
            self.table = {}
            self.load_table()
        
        def load_table(self):
            with open(self.TABLE_PATH, mode='r') as infile:
                reader = csv.reader(infile)
                self.table = {int(rows[0]):int(rows[2]) for rows in list(reader)}
        
        def get_value_for_number(self, number):
            pass

    class TaxTable(Table):
        TABLE_PATH = f'{TABLE_FOLDER}/Tax2022Table.csv'
        
        def __init__(self):
            super().__init__()
        
        def get_value_for_number(self, number):
            nearest_1000 = int(number // 1000 * 1000)
            closest_number = 0
            increment = 0
            if nearest_1000 == 0:
                choices = list(self.table.keys())[0:42]
                for option in choices:
                    
                    if option > number:
                        break
                    closest_number = option
                return self.table.get(closest_number, 0)
            
            if nearest_1000 in [1000, 2000]:
                increment = 25
            elif nearest_1000 >= 3000:
                increment = 50
            
            closest_number = int(number // increment * increment)
            
            return self.table.get(closest_number, 0)


    class EICTable(Table):
        TABLE_PATH = f'{TABLE_FOLDER}/EIC2022Table.csv'
        
        def __init__(self):
            super().__init__()
        
        def get_value_for_number(self, number):
            
            nearest_50 = int(number // 50 * 50)
            if nearest_50 == 0:
                nearest_50 = 1
            
            return self.table.get(nearest_50, 0)

    EIC_TABLE = EICTable()
    TAX_TABLE = TaxTable()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
