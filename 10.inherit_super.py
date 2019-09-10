class Person(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age, school, score):
        super(Student, self).__init__(name, gender, age)
        # *这是对继承自父类的属性进行初始化。而且是用父类的初始化方法来初始化继承的属性。
        # *也就是说，子类继承了父类的所有属性和方法，父类属性自然会用父类方法来进行初始化。
        # *当然，如果初始化的逻辑与父类的不同，不使用父类的方法，自己重新初始化也是可以的。
        # !super()仍未搞明白
        # self.name = name
        # self.gender = gender
        # self.age = age
        self.school = school
        self.score = score


s = Student('Alice', 'female', 18, 'Middle school', 87)
print(s.school)
print(s.name)
