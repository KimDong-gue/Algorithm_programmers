def solution(num, k):
    num=str(num)
    cnt=0
    k=str(k)
    for i in num:
        cnt+=1
        if i == k:
            return cnt
    return -1
            