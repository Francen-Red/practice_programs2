while True:
    while True:
        try:
            input_num1 = int(input("Pls input a number: "))
            break
        except:
            print("Pls input a valid number")

    while True:
        try: 
            input_num2 = int(input("Pls input another number: "))
            break
        except:
            print("Pls input a valid number")

    smaller_num = input_num1
    if smaller_num == input_num2:
        print("The two numbers are equal")
    
    else:
        if input_num2 < smaller_num:
            smaller_num = input_num2
        print("The smaller number is", smaller_num)
    
 