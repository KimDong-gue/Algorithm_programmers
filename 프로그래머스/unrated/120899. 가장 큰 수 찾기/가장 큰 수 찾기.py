import numpy as np
def solution(array):
    
    a=np.max(array)
    print(a)
    print(array.count(a))
    for idx,ans in enumerate(array):
        if a == ans:
    
            return [ans,idx]
        
        