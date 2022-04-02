"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)
"""
"""
문제 분석
알아 볼 수 없는 번호 -> 0
당첨 가능 최고 순위 및 최저 순위 리턴
해결 전략
시간 초과 걱정은 없음
0~1개 일치 : 6
2개 일치 : 5
3개 일치 : 4
4개 일치 : 3
5개 일치 : 2
6개 일치 : 1
(7-일치하는 개수(cnt+zero or cnt), 일치하는 개수 0이면 6위)
0이 모두 일치할 때 : 최고 순위
0이 모두 안 일치할 때 : 최저 순위
"""
def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            cnt+=1
        if i == 0:
            zero +=1
                
    if zero+cnt == 0: # zero, cnt 모두 0인 경우. : 다 채워져 있고 틀림
        answer.append(6)
        answer.append(6)
    else: # zero가 있거나, 일치하는 숫자 있음.
        answer.append(7-(zero+cnt)) # zero가 다 맞는 경우 -> 최고 순위
        answer.append(6 if cnt==0 else 7-cnt) # zero가 다 틀린 경우. -> 최저 순위(일치하는 개수 0이면 6위)
    return answer
