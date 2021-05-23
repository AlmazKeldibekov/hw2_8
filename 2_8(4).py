class Human:
    def eat_spaghetti(self):
        return f'I can eat spaghetti'
class Robot:
    def drink_oil(self):
        return f'I can drink oil'
class Cyborg(Human,Robot):
    pass

c = Cyborg()
print(c.eat_spaghetti(),c.drink_oil())

