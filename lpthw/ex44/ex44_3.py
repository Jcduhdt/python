# -*- coding : utf-8 -*-
# 继承
# date : 2019-4-11
# author : Zhang xiong

# 运行前或运行后替换（覆盖的一种特例）

class Parent(object):

    def altered(self):
        print('PARENT altered()')

class Child(Parent):

    def altered(self):
        print('CHILD, before parent altered()')
        # super 获取Parent.altered
        super(Child, self).altered()
        print('CHILD, after parent altered()')

dad = Parent()
son = Child()

dad.altered()
son.altered()

# super() 与 __init__ 搭配使用
# class Child(Parent):

    # def __init__(self, stuff):
        # self.stuff = stuff
        # super(Child, self).__init__()

# consequence
# PARENT altered()
# CHILD, before parent altered()
# PARENT altered()
# CHILD, after parent altered()
