print("How old are you?", end='')#这里可以不用写end=''作者只是为了把问题与输入放一排
age = input()#变量equal输入 接受一个标准输入数据，返回为string(字符串)类型
print("How tall are you?", end='')
height = input()
print("How much do you weight?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
