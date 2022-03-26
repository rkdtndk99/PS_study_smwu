# 내 풀이
def solution(board, moves):
    answer = 0
    stack = []

    for i in range(len(moves)):
        col = moves[i] - 1
        for j in range(len(board)):
            if board[j][col] != 0:
                out = board[j][col]
                board[j][col] = 0
                stack.append(out)
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break
    return answer

# 다른 사람 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
