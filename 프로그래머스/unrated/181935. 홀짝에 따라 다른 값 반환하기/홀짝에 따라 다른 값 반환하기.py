def solution(n):
    a=0
    b=0
    for i in range(1,n+1):        
        if i % 2 == 0 and n % 2 == 0:
            a+=i**2
        elif i % 2 == 1 and n % 2 == 1:
            b+=i
    return a if n % 2 == 0 else b 
            