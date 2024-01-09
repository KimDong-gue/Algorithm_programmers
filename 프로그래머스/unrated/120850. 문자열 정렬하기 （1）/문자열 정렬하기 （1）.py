def solution(my_string):
    my_string=list(my_string)
    a=[]
    for i in my_string:
        if i.isdigit():
            i=int(i)
            a.append(i)
            a.sort()
    return a
    