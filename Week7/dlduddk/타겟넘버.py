"""
문제 분석
    자연수들의 순서 바꾸지 않고 더하거나 빼서 타겟 넘버 만드는 방법의 수
해결 전략
    dfs를 이용하여 매번 더하고 빼고 해서 타겟 넘버 나오는지 확인
"""

def plus(n1, idx,length, numbers, target, cnt):
    if idx == length:
        if n1 == target:
            cnt = cnt + 1
        return cnt
    
    else:        
        n1 = n1 + numbers[idx]
        cnt = plus(n1, idx+1, length, numbers, target,cnt)
        cnt = minus(n1, idx+1,length, numbers, target,cnt)
        return cnt

def minus(n1, idx, length,numbers, target, cnt):    
    if idx == length:
        if n1 == target:
            cnt = cnt + 1
        return cnt
    
    else:
        n1 = n1 - numbers[idx]
        cnt = plus(n1, idx+1,length, numbers, target,cnt)
        cnt = minus(n1, idx+1,length, numbers, target,cnt)
        return cnt

def solution(numbers, target):
    length = len(numbers)
    cnt = 0
    cnt = plus(0, 0, length, numbers, target, cnt)
    cnt = minus(0, 0, length, numbers, target, cnt)
        
    cnt = cnt/2
    return cnt