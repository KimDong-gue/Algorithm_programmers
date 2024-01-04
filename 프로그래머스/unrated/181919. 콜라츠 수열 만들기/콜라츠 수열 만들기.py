def solution(x):
    def cola(x):
        if x % 2 == 0:
            return x//2
        elif x % 2 !=0:
            return 3*x+1
    n=cola(x)
    b=[x,n]
    while n!=1:
        n=cola(n)
        b.append(n)
    return b
            
        