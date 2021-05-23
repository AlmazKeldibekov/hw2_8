class Human:
    name = 'Kairat'
    age = 21
    favorite_lesson = 'math'
class Teacher(Human):
    speciality = 'teacher'
    salary = 24000

class Student(Human):
    grade = 2

teacher = Teacher()
student = Student()
human = Human()
#перенёс свойство favorite_lesson в родительский класс потому что он был в обоих классах
