formatter = "{} {} {} {}"#formatter 也是个变量名称

print(formatter.format(1, 2, 3, 4))#.format()是替换掉前面的{}
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#True 和 False是python中的关键字，表真假概念，不需要加""
#加了就成为字符串，没有原本功能了
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
     "Try your",
     "Own text here",
     "Maybe a poem",
     "Or a song about fear"
))
