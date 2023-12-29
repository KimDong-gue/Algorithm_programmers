def solution(num_list):
    b=''
    c=''
    for i in num_list:
        if i % 2 ==0:
            b+=str(i)
        else:
            c+=str(i)
    return int(b)+int(c)
