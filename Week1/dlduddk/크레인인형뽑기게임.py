"""
문제 분석
인형뽑기 진행 함.
같은 종류의 인형이 연속으로 바구니에 쌓이면 사라짐
인형이 없는 곳에서 크레인 작동시키면 아무 일도 일어나지 않음.
터뜨려서 사라진 인형 개수 return.
해결 전략
list에 스택처럼 쌓자.
stack의 top에 있는 것과 새로 들어갈 것이 같다면 answer+=2 하고 pop 하자
"""
def solution(board, moves):
    answer = 0
    n = len(board)
    st = []
    for i in moves:
        for k in range(n):
            #print(board[k][i-1])
            if board[k][i-1] != 0:
                if st:
                    if st[-1] == board[k][i-1]:
                        print(st[-1])
                        st.pop()
                        answer+=2
                    else:
                        st.append(board[k][i-1])
                else:
                    st.append(board[k][i-1])
                board[k][i-1] = 0
                break
        #print(st)
    return answer