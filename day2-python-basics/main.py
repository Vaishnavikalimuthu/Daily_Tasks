from utils import reverse_string, prime_or_not, fibonaci

reverse_str = input("enter the string: ")
print(f"the reversed string : {reverse_string(reverse_str)}")

num = int(input("enter the no to check prime: "))
print(f"{prime_or_not(num)}")

fib_no = int(input("enter the no for fib: "))
print(f"fibonacci series : {fibonaci(fib_no)}")