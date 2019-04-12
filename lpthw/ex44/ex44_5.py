# -*- coding : utf-8 -*-
# 组合
# date : 2019-4-11
# author : Zhang xiong

# 可实现与继承相同的功能，直接使用别的类和模块
# 并不是父类子类关系

class Other(object):

    def override(self):
        print('Other override()')

    def implicit(self):
        print('Other implicit()')

    def altered(self):
        print('Other altered()')

class Child(object):

    # 初始化时调用其他类
    def __init__(self):
        self.other = Other()

    # 必须定义一个Chlld.implicit函数来完成这个功能
    def implicit(self):
        self.other.implicit()

    def override(self):
        print('Child override()')

    def altered(self):
        print('Child, before Other altered()')
        self.other.altered()
        print('Child, after Other altered()')

son = Child()

son.implicit()
son.override()
son.altered()

# consequence
# Other implicit()
# Child override()
# Child, before Other altered()
# Other altered()
# Child, after Other altered()
