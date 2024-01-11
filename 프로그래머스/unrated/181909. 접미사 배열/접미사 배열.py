def solution(my_string):
    my_string=list(map(str,(my_string)))
    b=[]
    for i in range(len(my_string)):
        a=''.join(my_string[i:])
        b.append(a)
        b.sort()
    return b
        