def solution(num_list):
    a=[]
    b=[]
    for i in num_list:
        a=num_list[1::2]
        b=num_list[::2]
        a=sum(a)
        b=sum(b)
        if a > b:
            return a
        else:
            return b
        print(b)
