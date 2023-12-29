def solution(names):
    for idx,i in enumerate(names):
        return names[::5*(idx+1)]