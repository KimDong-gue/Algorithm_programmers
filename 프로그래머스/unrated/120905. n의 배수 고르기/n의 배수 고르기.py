def solution(n, numlist):
    
    b=[]
    
    for i in numlist:
        
        if i % n ==0:
            
            b.append(i)
    return b
            