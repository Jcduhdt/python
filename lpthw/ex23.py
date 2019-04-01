import sys
script, encoding, error = sys.argv
#  python ex23.py utf-8 strict
# 编码方式为utf-8

def main(language_file, encoding, errors):
    line = language_file.readline()
    # 从文件中读取一行
    if line:
# if 做决策 这里检验这一行内容是否包含某种东西  运行到结尾时 readline会返回空字符串
# 检查到空字符串 即判断假，会跳过后面两行代码
        print_line(line, encoding, errors)
        #打印这一行
        return main(language_file,encoding, errors)
# 调用mian函数 构成循环 if语句防止函数永远循环


def print_line(line, encoding, errors):
    #对文件每一行进行编码
    next_lang = line.strip()
    #把每行结尾的 \n 删掉      next_lang是一个字符串
    raw_bytes = next_lang.encode(encoding, errors = errors)
    #对原始字符串进行编码 成为字节序列 括号内是编码方式以及处理错误方式
    cooked_string = raw_bytes.decode(encoding, errors = errors)
# 解码 得到python字符串 应同next_lang
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)

#运行ex23.py时，将b''(字节串)中的字节转换成了指定的utf-8编码
# <===> 左边是python用数字表示的字节，或者说是用于存储字符串的原始字节
# 右边是处理后的显示
# encode 将字符串编写成字节序列
# decode 将字节序列解码成字符串
# utf-8  utf-16  utf-32  big5 编码
