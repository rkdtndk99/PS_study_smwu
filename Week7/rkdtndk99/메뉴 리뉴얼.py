# combination : 조합 구하는 모듈
from itertools import combinations
# Counter : 배열 안에 있는 원소의 중복 갯수 세는 모듈 
from collections import Counter


def solution(orders, course):
    answer = []
    # 코스의 개수만큼 반복 
    for c in course:
        temp = []
        for order in orders:
            # 주문에 대해 c만큼 뽑아 조합
            # ex) order : [A, B, C] / course : 2 -> combi = [AB, BC, AC]
            combi = combinations(sorted(order), c)
            # 임시 배열에 모든 조합 다 넣어주기 
            temp += combi
        # temp 배열 내에 조합된 개수 세기 Counter는 dictionary 형식으로 출력됨 
        # ex) [AB : 1, BC: 2, ... ]
        counter = Counter(temp)
        # counter 1개 이상이고 최댓값이 1이 아닐 때 
        if len(counter) != 0 and max(counter.values()) != 1:
            # 정답 배열에 해당 조합 추가. 
            # 정답이 counter에 포함되어 있고, 최댓값이랑 동일한 경우에만 추가
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)
