from sys import argv#sys模块
#sys.argv 变量是一个包含了命令行参数的字符串列表, 利用命令行想程序传递参数.
#其中,脚本的名称总是 sys.argv 列表的第一个参数。
#import 导入   将python的特性引入脚本的方法  模块
#argv 是参数变量(argument variable),它保存着运行python时传递给python脚本的参数
# read the WYSS section for how to run this
script, first, second, third = argv
#script 脚本
#将argv解包(unpack) 将argv中的变量一次赋值给等号前面四个变量
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
#powershell中键入python ex13.py first 2nd 3rd
#看到argv时要键入上一排的内容，argv赋值给多少个变量就键入多少个变量
#多输少输都会报错，自己可以试一下
#其中first 2nd 3rd可替换成自己想要的三种东西
#argv和input的不同之处在于使用时机，argv是执行命令时输入，input是脚本运行过程中输入
print("What's your name? ")
a = input()
print("What's your GF's name? ")
b = input()
print(f"OK, I know your name is {a} and your girlfirend's name is {b}.")
