"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

문제 분석
실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
해결 전략
stages를 먼저 정렬
cnt[특정 원소] = 특정 원소의 개수
isang[특정 원소] = 특정 원소 이상인 수의 개수
arr[특정 원소] = 특정 원소의 개수/stages에서 특정 원소 이상인 수의 개수
"""
def solution(N, stages):
    cnt = [0]*(N+2)
    isang = [0]*(N+2)
    arr = [0]*(N+2)
    stages.sort()
    for i in stages:
        cnt[i]+=1
    # cnt = [0,1,3,2,1,0,1]
    for i in range(1,N+2):
        isang[i] = sum(cnt[i:])
    for i in range(1,N+2):
        if isang[i]==0:
            arr[i] = (0,i)
        else:
            arr[i] = (cnt[i]/isang[i],i)
    del arr[0]
    del arr[-1]
    arr.sort(key=lambda x :(-x[0], x[1]))
    
    answer = []
    for i in arr:
        answer.append(i[1])
    return answer

