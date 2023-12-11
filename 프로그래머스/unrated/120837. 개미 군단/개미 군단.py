def solution(hp):
    #장군개미 5공격력
    #병정개미 3공격력
    #일개미 1공격력
    #5로 나눈 값을 3으로 나누고 그값을 1로 나눠서 그 정수를 return...
    a = hp // 5
    hp%=5
    b = hp // 3
    hp%=3
    c=hp//1
    hp%=1
    return a+b+c