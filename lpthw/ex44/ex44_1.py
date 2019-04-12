# -*- coding : utf-8 -*-
# 继承
# date : 2019-4-11
# author : Zhang xiong

# describe : 继承指明一个类的大部分或全部功能都从一个父亲中获得
# class Foo(Bar) 这个就发生了继承效果，创建一个叫 Foo 的类，并让他继承自 Bar
# python会让Bar的实例所具有的所有动作都工作在 Foo 的实例上
# 有三种交互方式
# 1.子类上的动作完全等同于父类动作
# 2.子类上的动作完全覆盖了父类的动作
# 3.子类上的动作部分替换了父类的动作
# 即隐式继承
class Parent(object):

    def implicit(self):
        print('PARENT implicit()')

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# 我们所定义的 Child 这个类中并没有定义具体细节，但son.implicit这个函数依然可用
# 他就是调用了父类Parent中定义的这个函数
# 若果将函数放到基类(Parent)中，那么所有子类(Child)将会自动获得这些函数的功能

# consequence
# PARENT implicit()
# PARENT implicit()
