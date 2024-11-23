# Ask the user to input two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Check if the first number is greater than the second
if first_number > second_number:
    # Print a message and all numbers between the two
    print("The numbers between them are:", end=" ")
    for number in range(second_number + 1, first_number):
        print(number, end=" ")
else:
    print("The first number is not greater than the second.")
