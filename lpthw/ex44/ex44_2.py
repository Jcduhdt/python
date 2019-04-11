# -*- coding : utf-8 -*-
# 继承
# date : 2019-4-11
# author : Zhang xiong

# 显示覆盖
class Parent(object):

    def override(self):
        print('PRAENT override()')

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# 显示覆盖即解决有时候需要让子类的函数有不同行为的情况 隐式继承是做不到的
# 只要在子类中定义一个同名的函数即可

# consequence
# PRAENT override()
# CHILD override()
