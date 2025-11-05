def largest_number():
    no_list = []
    for i in range(3):
        no = int(input("enter the no: "))
        no_list.append(no)
        
    largest = print(f"the largest no is {max(no_list)}")
  
    return largest
    
largest_number()  
    
    