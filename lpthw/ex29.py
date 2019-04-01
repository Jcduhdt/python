people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
#if 语句为代码创建了分支，如果布尔表达式为真 就运行接下来的代码，否则就跳过这一段
#if语句行尾冒号告诉Python接下来要创建一个新的代码块
#四个缩进是告诉Python这些代码处于该代码块中
