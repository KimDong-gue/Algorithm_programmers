def solution(strArr):
    y='ad'
    print(y in strArr[1])
    print(y)
    a=[]
    for i in strArr:
        if y not in i:
            a.append(i)
    return a