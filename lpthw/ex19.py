def cheese_and_crackers(cheese_count,boxes_of_crackers) :
    #cheese 奶酪 crackers 薄脆饼干
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    #blanket 毯子
    #该函数是输入cheese的个数以及饼干盒数，输出语句

print("We can just give the function number directly:")
cheese_and_crackers(20,30)
#直接输入数字，引用函数

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#输入变量 引用函数

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#输入数学公式 引用函数

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#输入变量 plus 数字 引用函数
#本节讲述给函数传递值的不同方式
print("Please input the number of cheese and crackers")
a = input("cheese: ")
b = int(input("crackers: "))# int()必须输入整数
cheese_and_crackers(a, b)
