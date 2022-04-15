# 내 풀이
def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]] += 1
        else:
            dic[clothes[i][1]] = 1

    for v in dic.values():
        answer *= (v + 1)

    return answer - 1

# 다른 사람 풀이
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
