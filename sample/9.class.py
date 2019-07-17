class Student(object):
    # *类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
    # *通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
    def __init__(self, name, score):
        # *由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
        # *通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
        # *第一个参数永远是self，表示创建的实例本身
        # self.name = name
        # self.score = score
        self.__name = name
        self.__score = score
        # *加两个下划线变为私有变量，只有内部可以访问，外部不能访问

    def print_score(self):
        # *print('%s:%s' % (self.name, self.score))
        print('%s:%s' % (self.__name, self.__score))
        # *python格式化与C相同

    def get_grade(self):
        # if self.score >= 90:
        if self.__score >= 90:
            return 'A'
        # elif self.score >= 60:
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def set_name(self, name):
        self.__name = name

    # *允许外部代码获取、修改


bart = Student('Bart Simpson', 59)

# print(bart.name)
print(bart.get_name())
# print(bart.score)
print(bart.get_score())
bart.print_score()
print(bart.get_name(), bart.get_grade())
bart.set_name('alan')
print(bart.get_name())
