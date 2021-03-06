class Animal(object):
    def run(self):
        print('Animal is running...')


alan = Animal()
alan.run()


class Dog(Animal):
    pass


# *对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。
# *子类获得了父类的全部功能,自动拥有了run()方法


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Catching mouse...')


Bob = Dog()
Bob.run()

Jack = Cat()
Jack.run()
# *子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这就是：多态。
'''
要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。
我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种
所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
'''


def run_twice(animal):
    # ?这里理解为函数还是方法？
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(alan)
run_twice(Jack)


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())
# *新增一个Animal的子类，不必对run_twice()做任何修改
# *实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''
