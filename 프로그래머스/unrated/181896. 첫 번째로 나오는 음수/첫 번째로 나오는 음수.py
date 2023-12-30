def solution(num_list):
    cnt=0
    for a in num_list:
        if a < 0:
            break
        elif a >= 0:
            cnt+=1
            if len(num_list)==cnt:
                return -1
    return cnt