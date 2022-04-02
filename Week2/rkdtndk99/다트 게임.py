# 내 풀이
def solution(dartResult):
    dartResult = dartResult.replace('10', 'k')
    bonus = {'S': 1, 'D': 2, 'T': 3}
    temp = []

    for i in dartResult:
        if i.isdigit():
            temp.append(int(i))
        elif i == 'k':
            temp.append(10)
        elif i in bonus:
            temp[-1] = temp[-1] ** bonus[i]
        elif i == '#':
            temp[-1] *= -1
        elif i == '*':
            temp[-1] *= 2
            if len(temp) > 1:
                temp[-2] *= 2

    return sum(temp)
