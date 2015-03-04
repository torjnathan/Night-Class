__author__ = 'Nathan'

class MyClass(object):
    school = "pdx code guild"

night_class = MyClass()
day_class = MyClass()

night_class.teacher = "Grant"
day_class.teacher = "Jamil"

night_class.__dict__
day_class.__dict__

print(day_class.school)
print(night_class.school)

day_class.school = "Portland State"

print(day_class.school)
