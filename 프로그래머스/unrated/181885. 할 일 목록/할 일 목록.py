def solution(todo_list, finished):
    a=[]
    for i in range(len(todo_list)):
        # todo_list와 finished 매칭..
        if not finished[i]:
            a.append(todo_list[i])
    return a
        
 