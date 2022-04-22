"""
문제분석
    가격이 떨어지지 않은 기간 구하기
해결전략
    스택/큐 모르겠어서 그냥 노가다했는데 됐음
"""
# 1 10 13 5 15 2 3
def solution(prices):
    length = len(prices)
    answer = []
    for i in range(length):
        cnt = 0
        for j in range(i+1, length):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt+=1
                break
        answer.append(cnt)
    return answer