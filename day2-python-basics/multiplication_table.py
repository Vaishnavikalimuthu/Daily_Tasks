def multiplication_table():
    num = int(input("enter the no for table: "))
    for i in range(1,11):
        print(f"{i} x {num} = {i*num}")
        
multiplication_table()