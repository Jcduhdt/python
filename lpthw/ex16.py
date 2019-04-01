from sys import argv
#python ex16.py test16.txt

script, filename = argv

print(f"We're going to erase {filename}.")#erase 擦除
print("If you don't want that, hit CTRL-C (^C).")
#ctrl+c 中断  powershell中^C即ctrl+c
#这个命令在powershell中应该是中断 中止脚本运行
print("If you want do that, hit RETURN.")
#键入任意一数 或不键入 直接回车？

input("?")
# 这里应该就是在powershell界面中 给出一个选择 按enter就运行接下来的代码

print("Opening the file...")
target = open(filename, 'w')
#open对文件的写入态度是安全第一，只有特别指定，才会进入写入操作
#w 写入模式  r 只读模式(open的默认行为) a 追加模式

print("Truncating the file. Godbye!")
target.truncate()#truncate 清空文件

print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(f"{line1} \n{line2} \n{line3} \n")

print("And finally,we close it")
target.close()
