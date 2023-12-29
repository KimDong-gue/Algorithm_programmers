def solution(arr):
    for idx1,i in enumerate(arr):
        for idx2,j in enumerate(arr):
            if arr[idx1][idx2]!=arr[idx2][idx1]:
                return 0
        return 1
                
            #arr[idx1][idx2]!=arr[idx2][idx1] 하나라도 존재하면 0을 출력
