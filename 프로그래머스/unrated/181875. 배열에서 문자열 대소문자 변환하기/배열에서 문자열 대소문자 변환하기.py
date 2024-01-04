def solution(strArr):
    c=[]
    for i,a in enumerate(strArr):
        print(i)
        if i % 2 ==0:
            print(1)
            b=a.lower()
            c.append(b)      
        elif i % 2 !=0:
            print(2)
            b=a.upper()
            c.append(b)
    return c
         