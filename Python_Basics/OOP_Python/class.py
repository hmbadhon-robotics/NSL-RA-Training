

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

    
## creating some objects
table_1 = Table("Large",3)
table_2 = Table("Small",2)
table_3 = Table("Medium",4)

## accessing object
print(str(table_1.leg))
print(int(table_1.drawer))

print(str(table_2.leg))
print(int(table_2.drawer))

print(str(table_3.leg))
print(int(table_3.drawer))

##Access Functions
print(table_1.show_leg_size())

##Access Class Attribute
print(table_1.Table_maker)
print(Table.Table_maker)


    
