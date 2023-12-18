def solution(n):
    a = 0
    for n in range(1,n+1):
        if n % 2 ==0:
            a+=n
    return a
        