while True:
    while True:
        try:
            input_num1 = int(input("Please input first num: "))
            break
        except:
            print("Enter a valid number")

    while True:
        try:
            input_num2 = int(input("Please input second num: "))
            break
        except:
            print("Enter a valid number")

    sum_num = input_num1 + input_num2
    print("The sum is", sum_num)