def solution(arr, idx):
    
    # arr의 원소는 1또는 0 이다.
    # 정수보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환!!
    # 예제1) 1보다 크면서 배열의 값이 1인 가장 작은 인덱스는 3
    # 예제2) 4보다 크면서 배열의 값이 1인 가장 작은 인덱스는 없다 따라서 -1
    # 예제3) 3보다 크면서 배열의 값이 1인 가장 작은 인덱스는 3
    for i in range(idx,len(arr)):
        if arr[i]==1:
            return i
    return -1
            #정수보다 인덱스가 크면서, 배열의 값이 1일때 , + 가장 작은 인덱스(return)
                #+ 1이 나올때 까지 진행
