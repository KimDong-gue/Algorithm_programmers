def solution(str_list, ex):
    a=[]
    str=''
    for i in str_list:
        if ex not in i:
            a.append(i)    
            str=''.join(a)
    
    return str
  
