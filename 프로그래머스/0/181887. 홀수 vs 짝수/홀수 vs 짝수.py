def solution(num_list):
    # 첫번째 원소를 1번 원소
    # 홀수번째 원소들의 합과 짝수번째 원소들의 합중 큰값을 return
    sum2=0
    sum1=0
    for i in range(len(num_list)):
        if i % 2 == 0:
            sum1+=num_list[i]
        else:
            sum2+=num_list[i]
    if sum1 > sum2:
        return sum1
    else:
        return sum2
        