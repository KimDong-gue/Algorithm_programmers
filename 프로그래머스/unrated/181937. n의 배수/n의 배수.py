def solution(num, n):
    #num , n 
    # num % n => 0 , 1 num % n != 0 , 0
    if num % n ==0:
        return 1
    elif num% n !=0:
        return 0