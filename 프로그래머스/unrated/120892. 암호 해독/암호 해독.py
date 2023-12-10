def solution(cipher, code):
    #암호화된 문자열 cipher
    #code의 배수 번쨰 글자만 진짜 암호
    print(range(len(cipher)))
    c=''
    for i in range(code,len(cipher)+1,code):
        print('-----')
        c+=cipher[i-1]
    return c