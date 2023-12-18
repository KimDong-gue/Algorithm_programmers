def solution(my_string):
    b=''
    a=list(map(str,my_string))
    a.reverse()
    b=''.join(a)
    return b
    