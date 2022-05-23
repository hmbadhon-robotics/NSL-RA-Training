# Class Declaration
class Table:
    ##class attributes
    Table_maker="Nuhash_Furniture"

    ##fields
    def __init__(self,leg,drawer):
        self.leg=leg
        self.drawer=drawer
    ## Functions
    def show_leg_size(self):
        return str(self.drawer)


## Inheriting Table Classs

class Computer_Table(Table):
    def show(self):
        print("Computer Table.")
    ##overriden function
    def show_leg_size(self):
        return "Computer Table"+"leg size "+str(self.drawer)


##applying Overriden Function
comp_table = Computer_Table("Small",4)
print(comp_table.show_leg_size())