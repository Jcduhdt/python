types_of_people = 10 #人有十种 定义变量
x = f"There are {types_of_people} types of people." #x等于要打印的内容提前把括号内的内容写出来

binary = "binary" #二进制的意思，这句是定义变量为字符串
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # 同x

print(x)
print(y)  #即打印事先写好的内容

print(f"I said: {x}") #这里说明x也是变量，插入字符串内输出
print(f"I also said: '{y}'")

hilarious = "Flase" #定义变量
joke_ecaluation = "Isn't that joke so funny?! {}"

print(joke_ecaluation.format(hilarious))
#.format()是在已创建的字符串上对应的{}应用格式化

w = "This is the left side of..."
e = "a string with a right side." #变量

print(w + e) #+号生成更长的字符串
z = ['zhangxiong','wangyuan'] #好像''里不能是变量，输出结果会变成变量名相连
print(''.join(z)) #括号内是格式，''不能删，同.format()吧
