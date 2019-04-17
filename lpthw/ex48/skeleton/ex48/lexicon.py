# 我太菜了啊，这个代码还是看着别人的写下来的
# 看书我都不知道要写些什么。。
# 加油啊
# 写的时候还少写了elif stop模块 测试错误
def scan(stuff):
    result = []
    direction = ['north','south','east']
    verb = ['go','kill','eat']
    stop = ['the','in','of']
    noun = ['bear','princess']
    stuff = stuff.split()
    for i in range(len(stuff)):
        if stuff[i] in direction:
            d = ('direction',stuff[i])
            result.append(d)

        elif stuff[i] in verb:
            v = ('verb',stuff[i])
            result.append(v)

        elif stuff[i] in stop:
            s = ('stop',stuff[i])
            result.append(s)

        elif stuff[i] in noun:
            n = ('noun',stuff[i])
            result.append(n)

        elif convert_number(stuff[i]):
            num = ('number',int(stuff[i]))
            result.append(num)

        else:
            error = ('error',stuff[i])
            result.append(error)
    return result

def convert_number(s): # 如果输入能转化为数字则返回数字，不能则返回None
    try:
        return int(s)
    except ValueError:
        return None
