from sys import argv
#sys是一个软件包，这句话的意思是从该软件包中取出argv这个特性

script, filename = argv

txt = open(filename)
#open 类似 input 接受参数并返回参数  返回文件对象，而不是文件内容

print(f"Here's your file {filename}:")
print(txt.read())
#接受命令方式，使用句点. 嘿，txt，执行你的read命令，无需任何参数

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
#txt_again.close()
