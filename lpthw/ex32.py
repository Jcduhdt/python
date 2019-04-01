the_count = [1, 2, 3, 4, 5]
# 创建列表 只能用 , 隔开 不能用空格替代
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, frist start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    # range(0, 6)循环6次， 从0到5，即第一个数到最后一个数，但不包含最后一个数
    #含首不含尾
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
    #在列表尾部追加元素

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

a = [[1, 2, 3], [4, 5, 6]]
# 创建二维列表 就是列表中包含列表但是怎么把每个元素都打印出来呢
for i in a:
    print(f"try: {i}")
#for j in i:
#    print(f"try: {j}")
