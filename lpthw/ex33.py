i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the buttom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

musics = []
k = 10
while k >= 1:
    musics.append(k)
    print(f"Now I have {k} musics.")
    print(musics)
    k -= 1
