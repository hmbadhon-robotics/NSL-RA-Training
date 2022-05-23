
##Public Class
print("Public Class Results")
class Cup:
    def __init__(self) -> None:
        self.color = None
        self.content = None
    def fill(self, beverage):
        self.content = beverage
    def empty(self):
        self.content = None
    def show(self):
        print(self.color)
        print(self.content)

redCup = Cup()
redCup.color = "red"
redCup.content = "tea"
redCup.show()
redCup.empty()
redCup.fill("coffee")
redCup.show()

print("Protected Class Results")
##Protected Class or Weakly Private
class Cup:
    def __init__(self) -> None:
        self.color = None
        #by convention _content is protected variable but it can be accessed
        self._content = None # protected variable
    def fill(self, beverage):
        self._content = beverage
    def empty(self):
        self._content = None
    def show(self):
        print(self.color)
        print(self._content)

redCup = Cup()
redCup.color = "red"
redCup._content = "tea"
redCup.show()
redCup.empty()
redCup.fill("coffee")
redCup.show()


print("Private Class Results")

class Cup:
    def __init__(self) -> None:
        self.color = None
        self.__content = None #private variable
    def fill(self,beverage):
        self.__content = beverage
    def empty(self):
        self.__content = None

    def show(self):
        print(self.color)
        print(self.__content)

redCup = Cup()
redCup.color = "red"
redCup.__content = "tea" # this doesn't let tea to be added
#redCup._Cup__content="tea" #this will let tea to be added
redCup.show()
redCup.empty()
redCup.fill("coffee")
redCup.show()




