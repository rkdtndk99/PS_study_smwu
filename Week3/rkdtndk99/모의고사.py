# 내 풀이
def solution(answers):
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    answer = [0, 0, 0]
    result = []

    for i in range(len(answers)):
        if answers[i] == students[0][i % 5]:
            answer[0] += 1
        if answers[i] == students[1][i % 8]:
            answer[1] += 1
        if answers[i] == students[2][i % 10]:
            answer[2] += 1

    m = max(answer)
    for i in range(len(answer)):
        if m <= answer[i]:
            result.append(i + 1)

    return result

