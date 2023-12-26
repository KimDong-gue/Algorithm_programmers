def solution(s1, s2):
    l=[]
    for i in s1:
        if i in s2:
            l.append(i)
    return len(l)
    
    