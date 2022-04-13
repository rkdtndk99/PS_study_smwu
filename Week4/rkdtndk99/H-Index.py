def solution(citations):
    count = 0
    citations.sort()
    for i in range(citations[-1] + 1):
        new_c = [item for item in range(len(citations)) if citations[item] >= i]
        
        if len(new_c) >= i : 
            count = i 
        else : 
            break 
            
    return count
