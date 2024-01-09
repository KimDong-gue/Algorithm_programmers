def solution(my_string, num1, num2):
    
    # 인덱스를 바꾼다...replace면, 문자를 다 바꿔주기 때문에...
    answer = ''
    my_string=list(my_string)
    print(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    print(my_string)
    return answer.join(my_string)