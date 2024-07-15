def solution(todo_list, finished):
    # todo_list는 영,소문자 / 서로 다르다
    # finished[i]는 true or false / true는 todo_list[i]를 마쳤음을, false는아직 못마침
    # false가 적어도 하나가있음
    answer = []
    for i in range(0,len(todo_list)):
        if finished[i] == True:
            pass
        else:
            answer.append(todo_list[i])
    
    return answer