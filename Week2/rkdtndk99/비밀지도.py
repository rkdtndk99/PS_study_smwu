# 내 풀이
def solution(n, arr1, arr2):
    answer = []
    temp = ''
    for i in range(n):
        temp1 = format(arr1[i], "b").zfill(n)
        temp2 = format(arr2[i], "b").zfill(n)
        arr1[i] = temp1
        arr2[i] = temp2

    for j in range(n):
        for k in range(n):
            if arr1[j][k] == '1' or arr2[j][k] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
        temp = ''

    return answer

# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = str(bin(i | j)[2:])
        temp = temp.rjust(n, '0')
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)

    return answer
