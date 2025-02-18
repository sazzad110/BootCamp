class Person():
    def introduce(self):
        print("I am a person.")
    
class Student(Person):
    def introduce(self):
        print("I am a student.")

p = Person()
p.introduce()

s = Student()
s.introduce()