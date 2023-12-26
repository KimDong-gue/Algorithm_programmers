def solution(num_list):
    count = 0
    count1 = 0
    for num in num_list:
        if num % 2 == 0:
            count+=1
        elif num % 2 == 1:
            count1+=1
    return [count,count1]