def solution(numbers, n):
    a=[]
    for i in numbers:
        a.append(i)
        b=sum(a)
        if b>n:
            return b
            break
                
                
