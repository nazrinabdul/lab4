numbers = [2, 5, 7, 3, 8, 10, 1, 6]

with open("massiv.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

greater_than_5 = []
with open("massiv.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number > 5:
            greater_than_5.append(number)

with open("boyuk_5.txt", "w") as file:
    for num in greater_than_5:
        file.write(str(num) + "\n")


total = sum(greater_than_5)
print("X > 5 olan ədədlərin cəmi:", total)
