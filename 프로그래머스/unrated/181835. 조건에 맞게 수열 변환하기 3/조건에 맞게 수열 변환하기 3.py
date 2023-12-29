def solution(arr, k):
    b=[]
    c=[]
    if k % 2 ==0:
        for i in arr:
            b.append(i+k)
        return b
    else:
        for i in arr:
            c.append(i*k)
        return c
            