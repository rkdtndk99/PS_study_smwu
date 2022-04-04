# 내 풀이
def solution(n, lost, reserve):
    s_res = set(reserve) - set(lost)
    s_lost = set(lost) - set(reserve)
    for i in s_res:
        if i - 1 in s_lost:
            s_lost.remove(i - 1)
        elif i + 1 in s_lost:
            s_lost.remove(i + 1)
    return n - len(s_lost)

# 다른 사람 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
