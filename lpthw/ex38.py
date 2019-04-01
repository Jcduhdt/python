ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
# .split(' ') : ''中的内容即分隔符   比如空格，意思是制定分隔符为空格
more_stuff = ["Days", "Night", "Song", "Frisbee",
               "Cron", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    # .pop : 用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        # .pop(0) 为第一个元素 .pop(-1)为最后一个元素
    print("Adding: ", next_one)
    stuff.append(next_one)
    # .split(' ') : ''中的内容即分隔符   比如空格，意思是制定分隔符为空格
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
# .join() 用于将序列中的元素以指定的字符连接生成一个新的字符串
# join 插入
print('#'.join(stuff[3:5])) # super stellar!
# 同 range(0, 10)
