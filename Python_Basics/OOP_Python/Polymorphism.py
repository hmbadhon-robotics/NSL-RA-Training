class Goru:
    def food(self):
        print("Goru Ghash Khae")
class Bagh:
    def food(self):
        print("Bagh Meat Khae")

# common function
def food_habit(animal):
    animal.food()

goru = Goru()
bagh = Bagh()

food_habit(goru)

food_habit(bagh)