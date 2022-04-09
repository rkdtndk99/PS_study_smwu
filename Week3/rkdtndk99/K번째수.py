# 내 풀이
def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        temp = []
        i = commands[index][0] - 1
        j = commands[index][1]
        k = commands[index][2] - 1
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer

# 다른 사람 풀이
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
