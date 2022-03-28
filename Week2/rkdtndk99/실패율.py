# 내 풀이
def solution(N, stages):
    answer = {}
    stages.sort()
    for i in range(1, N + 1):
        c = stages.count(i)
        if c == 0:
            answer[i] = 0
        else:
            answer[i] = c / len(stages)
        for _ in range(c):
            stages.pop(0)
        st = dict(sorted(answer.items(), key=lambda item: item[1], reverse=True))

    return list(st.keys())

# 다른 사람 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)
