class School:
    def wear_uniform(self):
        return f'В школе все должны носить форму'
class University:
    def wear_uniform(self):
        return f'Можно носить любую одежду, если ты студент'

s = School()
print(s.wear_uniform())
u = University()
print(u.wear_uniform())

