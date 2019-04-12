from sys import argv
# python ex20.py test20.txt
script, input_file = argv
# 应该是必须先 open 再进行其他诸如read write readline 之类的吧
def print_all(f):
    print(f.read())
#磁头，通过磁头操作文件
def rewind(f):#rewind 倒回 倒带
    f.seek(0)
    #seek()使磁头到达括号内的字节处，seek(0)即磁头到达文件0字节处
    #seek(20)即磁头到达文件的第20个字节处
    #seek()函数处理的对象是字节

def print_a_line(line_count, f):
    print(line_count, f.readline())
# readline()即读取文件的一行，并把磁头移动到 \n 处
# readline()函数返回的内容中包含文件中本身就有的 \n
# readline()扫描文件的每一个字节 直到 \n 为止
current_file = open(input_file)

print("Frist let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a type.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
#print函数也会以 \n 结尾 所以运行该函数会有两个 \n 可以在print函数中用end = ""结尾
current_line = current_line + 1
# a+=b 即 a=a+b
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
