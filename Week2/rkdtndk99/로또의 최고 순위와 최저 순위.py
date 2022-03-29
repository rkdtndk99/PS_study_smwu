def solution(lottos, win_nums):
    answer = []
    match = 0 
    nomatch = 0 
    for item in lottos: 
        if item in win_nums: 
            match += 1 # number of matching numbers
        elif item == 0 : 
            nomatch += 1
    answer.append(7 - (match + nomatch if match+nomatch > 1 else 1))
    answer.append(7 - (match if match >= 2 else 1))
    return answer
