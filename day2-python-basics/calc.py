def calculator():
    print('Select your choice which you want to do')
    print('1. Add 2. Subtract 3. Multiply 4. Divide 5. Modulas 6. Exit')
    
    choice = int(input("Enter your choice (1-6): "))
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the first number:"))
    
    if choice == 1:
        add = num1 + num2
        result = print("the addition of two no :", add)
    
    elif choice == 2:
        result = print("the subtraction of two no :", num1 - num2)
    
    elif choice == 3:
        result = print("the multiplication of two no :", num1 * num2)
    
    elif choice == 4:
        result = print("the divition of two no :", num1 / num2)
    
    elif choice == 5:
        result = print("the modulo of two no :", num1 % num2)
    
    elif choice == 6:
        result = print("Exit")
        
    else:
        result = print("Enter the choice beteween 1-6 ")
    
    return result    

calculator()
