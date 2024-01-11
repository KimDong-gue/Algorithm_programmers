def solution(binomial):
    a=0
    b=1
    c=binomial.split(' ')
    if '+' in c:
        a,op,b=tuple(c)
        (a,b)=int(a),int(b)
        return a+b
    elif '-' in c:
        a,op,b=tuple(c)
        (a,b)=int(a),int(b)
        return a-b
    elif '*' in c:
        a,op,b=tuple(c)
        (a,b)=int(a),int(b)
        return a*b
        