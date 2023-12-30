def solution(n, k):
    a=[]
    b=[]
    for i in range(1,n+1):
        if i % k ==0:
            a.append(k*i//k)
        elif i % k !=0:
            b.append(k*i//1)
    return a