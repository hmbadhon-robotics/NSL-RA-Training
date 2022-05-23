
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
class Dining_Table(Table):
    def show(self):
        print("Dining Table.")


##creating inherited class object
comp_table = Computer_Table("large",3)
dine_table = Dining_Table("small",4)


#accessing inherited objects
comp_table.show()
dine_table.show()