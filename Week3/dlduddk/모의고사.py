"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

문제 분석
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
가장 많은 문제를 맞힌 사람

해결 전략
학생 답안이랑 정답 비교 후 가장 많이 맞춘 학생 리턴하기
"""
def solution(answers):
    # 학생들 답안
    s1 = [1,2,3,4,5]*2000
    s2 = [2,1,2,3,2,4,2,5]*1250
    s3 = [3,3,1,1,2,2,4,4,5,5]*1000
    
    cnt = [[1,0],[2,0],[3,0]] # [학생 번호, 맞춘 개수]
    res = [] # 결과
    length = len(answers)
    
    # 맞춘 개수
    for i in range(length):
        if answers[i] == s1[i]:
            cnt[0][1]+=1
        if answers[i] == s2[i]:
            cnt[1][1]+=1
        if answers[i] == s3[i]:
            cnt[2][1]+=1
    
    cnt.sort(key=lambda x: -x[1]) # 맞춘 개수 내림차순
    maxval = cnt[0][1] # 가장 많이 맞춘 문제 수
    res.append(cnt[0][0]) # 가장 많이 맞춘 학생

    # 가장 많이 맞춘 학생이 여러명인지
    for i in range(1,3):
        if cnt[i][1] == maxval: 
            res.append(cnt[i][0])
    return res
"""
예전에 푼 코드
def solution(answers):
    s1 = [1,2,3,4,5]*2000
    s2 = [2,1,2,3,2,4,2,5]*1250
    s3 = [3,3,1,1,2,2,4,4,5,5]*1000
    
    cnt1 =0
    cnt2 =0
    cnt3 =0
    length = len(answers)
    for i in range(length):
        if s1[i] == answers[i]:
            cnt1 = cnt1+1
        if s2[i] == answers[i]:
            cnt2 = cnt2+1
        if s3[i] == answers[i]:
            cnt3 = cnt3+1
    answer = []
    if cnt1 > cnt2 and cnt1 > cnt3:
        answer.append(1)
    if cnt2 > cnt1 and cnt2 > cnt3:
        answer.append(2)
    if cnt3 > cnt1 and cnt3 > cnt2:
        answer.append(3)
    
    if cnt1 == cnt2 and cnt1 > cnt3:
        answer.append(1)
        answer.append(2)
    
    if cnt1 == cnt3 and cnt1 > cnt2:
        answer.append(1)
        answer.append(3)
    
    if cnt2 == cnt3 and cnt2 > cnt1:
        answer.append(2)
        answer.append(3)
    
    if cnt2 == cnt3 and cnt2 == cnt1:
        answer.append(1)
        answer.append(2)
        answer.append(3)
        
    return answer
"""