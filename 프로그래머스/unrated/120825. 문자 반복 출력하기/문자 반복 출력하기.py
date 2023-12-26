def solution(my_string, n):
    my=''.join(my_string)
    me=list(my)
    m2=''
    for i in me:
        m2+=i*n
    return m2