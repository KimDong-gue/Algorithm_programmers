def solution(my_string, letter):
    a=''
    for i in my_string:
        if i != letter:
            a+=i
    return a