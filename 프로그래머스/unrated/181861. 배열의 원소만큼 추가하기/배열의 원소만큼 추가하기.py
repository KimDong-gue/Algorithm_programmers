def solution(arr):
    x=[]
    y=[]
    for i in arr:
        x.append(i*str(i).split())
    a=sum(x,[])
    for j in a:
        y.append(int(j))
    return y