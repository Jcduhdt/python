# this one is like your scripts with argv
def print_two      (*args):# 函数名之后不用紧跟()
    # 函数名命名规则同C
    #*arg告诉python把函数所有参数接收进来，放到名叫arg的列表中
    #同argv，不过这是用在函数上
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    # def 即 define 定义函数 后面的即函数名，必须要以 : 结尾
    #def之后，即冒号以下使用四个空格进行缩进的行均属于该函数，不能多也不能少

# ok, that *args is actually pointless, we can just do this
def print_two_again    (arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):# 最初少打了_one,导致错误
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():#最初 写成了print_one 错误
    print("I got nothing.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()# 最初把这四行都空了4格，导致运行时没出结果 错误都没报

# 括号内以都好隔开想要的值
# 前面定义函数 最后使用函数
# 为什么函数输入要用 "" 来引起呢  不引会报错 颜色也不一样
