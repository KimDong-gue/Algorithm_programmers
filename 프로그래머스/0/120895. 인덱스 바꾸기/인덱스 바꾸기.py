def solution(my_string, num1, num2):
    
    my_string=list(my_string)
    agx = []
    agx1 = ''
    a = my_string[num1]
    b = my_string[num2]
    agx1 += my_string[num1]
    my_string[num2] = agx1
    my_string[num1] = b
    for i in my_string:
        agx.append(i)
    agx1=('').join(agx)
    return agx1
        
        
        