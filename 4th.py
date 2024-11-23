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

    if input_num1 != input_num2:
        print("Not Equal")
    elif input_num1 == input_num2:
        print("Equal")