def solution(age):
    a=[]
    for i in str(age):
        print(i)
        print('kds')
        i=str(i).replace('0','a')
        i=str(i).replace('1','b')
        i=str(i).replace('2','c')
        i=str(i).replace('3','d')
        i=str(i).replace('4','e')
        i=str(i).replace('5','f')
        i=str(i).replace('6','g')
        i=str(i).replace('7','h')
        i=str(i).replace('8','i')
        i=str(i).replace('9','j')
        a.append(i)
    return ''.join(a)
    