def solution(myString):
    myString=myString.split('x')
    myString.sort()
    for i in myString:    
        if '' in myString:
            myString.remove('')
    return myString

     