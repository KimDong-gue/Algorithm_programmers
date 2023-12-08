def solution(my_string):
    attend=''
    
    for i in my_string:
        if i.isupper():
            attend+=i.lower()
        else:
            attend+=i.upper()
    return attend
                
    