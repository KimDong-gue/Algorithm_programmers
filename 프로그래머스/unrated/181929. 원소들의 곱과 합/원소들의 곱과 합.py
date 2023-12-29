def solution(num_list):
    #모든 원소들의 곱이
    #모든 원소들의 합의 제곱보다 작으면 1
    #크면 0
    a=1
    b=0
    for i in num_list:
        a*=i
    for i in num_list:    
        b+=i
        
    b=b**2
    
    
    if a > b:
        return 0
    else:
        return 1
