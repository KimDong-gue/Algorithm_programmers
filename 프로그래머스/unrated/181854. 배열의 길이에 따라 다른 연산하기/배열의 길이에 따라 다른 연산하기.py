def solution(arr, n):
    b=[]
    for i,a in enumerate(arr):
        if len(arr) % 2 !=0:
            if i % 2 ==0:
                b.append(arr[i]+n)
            else:
                b.append(arr[i])
        else:
            if i % 2 !=0:
                b.append(arr[i]+n)
            else:
                b.append(arr[i])
    return b
        