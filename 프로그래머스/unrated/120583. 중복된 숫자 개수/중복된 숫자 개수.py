def solution(array, n):
    count =0 
    
    for i in array:
        
        if n == i:
            count+=1
    
    return count
#array를 n에 넣고,
#n이 array에 포함될때 마다, count 1씩 증가
