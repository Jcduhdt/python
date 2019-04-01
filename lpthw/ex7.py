print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)   # what'd that do
#应该是把字符串连续重复10次
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma(逗号) at the end. try removing it to see what happens
print(end1+end2+end3+end4+end5+end6, end='')#在字符串末尾添加空字符串代替换行符
print(end7+end8+end9+end10+end11+end12)


print("zx"*5)
print("wy",end='')
print("math",end='  ')#  end=''即在字符串末用''中的内容替换换行符,似乎只能是空格
print("easy")
