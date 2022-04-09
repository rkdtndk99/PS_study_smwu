"""
문제 분석
n편 중 h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 미만 인용되었다면, h의 최댓값이 과학자의 H-index



해결 전략
citations.sort()
h개의 논문이 최소 h번 인용되었다.

"""
def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    maxval = citations[-1]
    for i in range(maxval+1):
        h = i
        # citations[0~n-1] 중 h 이상인 경우의 인덱스들 배열 -> h번 이상 인용된 논문들의 인덱스 배열
        large = [j for j in range(n) if citations[j] >= h]
        
        # 최소 h번 인용된 논문 수가 h개 이상
        if len(large) >= h:
            answer = h
        # else는 없어도 통과되는데 있으면 시간 훨씬 줄어듦
        else:
            break
    return answer
