def get10_numbers(number_input):
    while True:
        try:
            return int(input(number_input))
        except:
            print("ERROR")

num_1 = get10_numbers("Please input a number: ")
num_2 = get10_numbers("Please input a number: ")
num_3 = get10_numbers("Please input a number: ")
num_4 = get10_numbers("Please input a number: ")
num_5 = get10_numbers("Please input a number: ")
num_6 = get10_numbers("Please input a number: ")
num_7 = get10_numbers("Please input a number: ")
num_8 = get10_numbers("Please input a number: ")
num_9 = get10_numbers("Please input a number: ")
num_10 = get10_numbers("Please input a number: ")
total_sum = (num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10)
print("The sum is:", total_sum)