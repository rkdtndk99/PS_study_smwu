"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

문제 분석
한 명 빼고 모두 완주함
마라톤에 참여한 선수들 participant, 완주한 선수들 completion
완주하지 못한 선수 return

해결 전략
participant와 completion 비교해서 없는 사람 뽑아
근데 브루트포슨가 그거 하면 안되겠지? -> 중복때문에 안 되나 보다
"""

def solution(participant, completion):
    
    partdict = {x:0 for x in participant}
    compdict = {x:0 for x in completion}
    for i in participant:
        partdict[i]+=1
    for i in completion:
        compdict[i]+=1
    
    for i in participant:
        
        if i not in compdict.keys():
            return i
        if partdict[i] != compdict[i]:
            return i
        
"""
예전에 풀었던 코드
이 방식이 더 사람들이 많이 이용함

def solution(participant, completion):
    participant.sort()
    completion.sort()
    length = len(completion)
    for i in range(length):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]
"""