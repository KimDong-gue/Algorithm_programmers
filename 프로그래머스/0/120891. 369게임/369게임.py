def solution(order):
    clap=['3','6','9']
    order=list(str(order))
    cnt=0
    for i in order:
        if i in clap:
            cnt+=1
    return cnt