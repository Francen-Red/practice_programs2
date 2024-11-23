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

    bigger_num = input_num1
    if input_num2 > bigger_num:
        bigger_num = input_num2
    print("The bigger number is", bigger_num)