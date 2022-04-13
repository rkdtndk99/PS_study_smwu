# 내 풀이
def solution(numbers):
    numbers = map(str, numbers)
    new = sorted(numbers, key = lambda x : x*4, reverse = True)
    answer = ''.join(new)
    return str(int(answer))
