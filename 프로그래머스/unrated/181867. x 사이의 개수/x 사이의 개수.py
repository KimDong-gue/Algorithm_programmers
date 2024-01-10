def solution(myString):
    #for idx,a in enumerate(myString):
    myString=list(myString.split('x'))
    a=[]
    for i in myString:
        a.append(len(i))
    return a
    
            