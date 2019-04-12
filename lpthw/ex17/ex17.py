from sys import argv
from os.path import exists
#调取os.path 中的exists函数 判真假

script, from_file, to_file = argv

print(f"Coping from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file);indata = in_file.read()
#通过 ; 可以在同一行写多句命令
#indata = in_file.read()
# indata = in_file 的内容

print(f"The input file is {len(indata)} bytes long")
#len()字符串长度

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# abort 中止
input()
#这里是输入enter还是ctrl+c

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# 开始的时候准备了test17.txt是中文，运行时出错 采用了in17.txt的英文内容才行
#UnicodeDecodeError: 'gbk' codec can't
# decode byte 0xab in position 28: illegal multibyte sequence
#似乎是解码方式只能对应英文,怎样才能复制粘贴中文呢

#powershell 中运行 cat 文件名 可以显示文件中的内容
# echo 创建文件  eg. echo "This is a test file." > test.txt
