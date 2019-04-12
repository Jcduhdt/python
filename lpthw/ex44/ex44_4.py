# -*- coding : utf-8 -*-
# 继承
# date : 2019-4-11
# author : Zhang xiong

# 三种方式的组合使用

class Parent(object):

    def override(self): # 覆盖
        print('Parent override()')

    def implicit(self): # 隐式继承
        print('Parent implicit()')

    def altered(self): # 运行前后替换
        print('Parent altered()')

class Child(Parent):

    def override(self):
        print('Child override()')

    def altered(self):
        print('Child, before parent altered()')
        # 用 Child, self 这两个参数调用 super 然后在此返回的基础上调用 altered
        super(Child, self).altered()
        print('Child, after parent altered()')

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# consequence
# Parent implicit()
# Parent implicit()
# Parent override()
# Child override()
# Parent altered()
# Child, before parent altered()
# Parent altered()
# Child, after parent altered()
