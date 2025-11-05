def reverse_string(s):
    # rev_s = s[::-1]
    rev_s = ''
    for i in s:
        rev_s = i+rev_s
    return rev_s
    
def prime_or_not(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                return f"{n} is not a prime no"
        return f"{n} is a prime no"
    else:
        return f"{n} is a prime no"
        
        
def fibonaci(n):
    a,b= 0,1 
    fib_series = []
    for i in range(n):
        fib_series.append(a)
        a,b = b, a+b
    return fib_series