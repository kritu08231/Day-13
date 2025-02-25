#WAF to find the factorial of number.

def cal_fact(a=1):
    fact=1
    for i in range(1,a+1):
        fact*=i
    print("factorial",fact)
    
cal_fact(5)
