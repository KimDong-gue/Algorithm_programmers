def solution(my_string):
    if ' ' in my_string: 
        return my_string.split(' ')
        
    else: 
        return list(my_string.split(' '))
    