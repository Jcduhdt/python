tabby_cat = "\tI'm tabbed in."#ASCII水平制表符
#从结果看是开头空8个字母的位置，两单词之间空4个
persian_cat = "I'm split\non a line."#换行
backslash_cat = "I'm \\ a \\ cat."#打出反斜杠\

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

zx = "study\thard"
print(zx)

#\\   输出反斜杠\
#\'   输出单引号'
#\"   输出双引号"
#\a   ASCII响铃符(BEL)
#\b   ASCII退格符(BS)
#\f   ASCII进纸符(FF)
#\n   ASCII换行符(LF)
#\N(name)    Unicode数据库中的字符名，其中name是它的名字，仅Unicode适用
#\r   ASCII回车符(CR)
#\t   ASCII水平制表符(TAB)
#\uxxx   值为16位十六进制xxxx的字符
#\Uxxxxxxxx   值为32位十六进制xxxxxxxx的字符
#\v   ASCII垂直制表符(VT)
#\ooo   值为八进制值ooo的字符
#\xhh   值为十六进制hh的字符
