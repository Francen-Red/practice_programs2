def get10_numbers(number_input):
    while True:
        try:
            return int(input(number_input))
        except:
            print("ERROR")

numbers = [get10_numbers("Please input a number: ") for _ in range(10)]
sum_num = sum(numbers)
print("The total sum is", sum_num)