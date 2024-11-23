odd_count = 0
odd_nums = []

for i in range(10):
    while True:
        try:
            number = int(input("Pls input a number: "))
            break
        except ValueError:
            print("Error! Pls input a valid number")

    if number % 2 != 0:
        odd_count += 1
        odd_nums.append(number)

print("The odd numbers are", odd_nums)
print("The odd numbers count is", odd_count)