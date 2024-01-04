def solution(n_str):
    a=''.join(n_str)
    b=list(a)
    for idx,a in enumerate(b):
        if a!='0': # 다음에 0이 아닌 숫자가 나온다면 break
            c=''.join(b[idx:])
            return c
            
            
            
            
