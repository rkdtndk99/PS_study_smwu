"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

"""
"""
문제 분석
4행 1열, 3열이 첫 시작
상하좌우 1칸씩만 이동 가능
1열은 왼손, 2열은 둘 다 가능(현재 키패드에서 더 가까운 쪽 이용, 같다면 왼손잡이, 오른손잡이 고려), 3열은 오른손
해결 전략
147 이면 무조건 왼쪽
369 이면 무조건 오른쪽
2580 이면 abs(인덱스 차)로 계산, 같으면 hand로 결정
"""
def get_len(which, temp):
    return abs(which[0]-temp[0])+abs(which[1]-temp[1])

def solution(numbers, hand):
    answer = ''
    left = [4,1] # 4행 1열
    right = [4,3] # 4행 3열
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left = [i//3+1, 1]
        elif i in [3,6,9]:
            answer+='R'
            right = [i//3, 3]
        else:
            if i == 0:
                temp = [4,2]
            elif i == 2:
                temp = [1,2]
            elif i == 5:
                temp = [2,2]
            else:
                temp = [3,2]
            if get_len(left,temp) < get_len(right, temp):
                left = temp[:]
                answer += 'L'
            elif get_len(left,temp) > get_len(right, temp):
                right = temp[:]
                answer += 'R'
            else:
                if hand == 'right':
                    right = temp[:]
                    answer += 'R'
                else:
                    left = temp[:]
                    answer += 'L'
    return answer
