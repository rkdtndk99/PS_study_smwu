"""
문제분석
    중요도 높은 문서 먼저 인쇄하는 프린터
        대기 목록 중 가장 앞의 문서J를 대기목록에서 꺼냄
            나머지 대기목록 중 J보다 중요도 높은 문서 존재하면 J를 대기목록 가장 뒤에 넣음
            아니면 J인쇄
    숫자가 클수록 중요
    현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities
    내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location
    내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
해결전략
    그냥 시키는대로 하기
"""
def solution(priorities, location):
    cnt = 1
    while priorities:
        j = priorities[0] # 맨 앞에 있는 문서 J
        priorities = priorities[1:] # 나머지 대기목록
        if priorities:
            if j < max(priorities): # 나머지 대기목록 중 J보다 중요도 높은 거 존재하면
                priorities.append(j) # J를 뒤에 넣음
                
                location -= 1 # location 위치 업데이트
                if location < 0:
                    location = len(priorities)-1
                    
                
            elif location == 0: # J가 가장 중요도 높았고, 내가 요청한 문서인 경우
                return cnt
            else: # J가 가장 중요도 높았으나 내가 요청한 문서 아님
                cnt += 1 
                location -= 1
        else:
            return cnt