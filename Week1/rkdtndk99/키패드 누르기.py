# 내 풀이
def solution(numbers, hand):
    answer = ''
    lhand = 10
    rhand = 11

    # index == number로 좌표 만들기
    points = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            lhand = i
        elif i in [3, 6, 9]:
            answer += "R"
            rhand = i

        # 2580 나온 경우
        else:
            ldist = abs(points[lhand][0] - points[i][0]) + abs(points[lhand][1] - points[i][1])
            rdist = abs(points[rhand][0] - points[i][0]) + abs(points[rhand][1] - points[i][1])

            if ldist > rdist:
                answer += "R"
                rhand = i
            elif rdist > ldist:
                answer += "L"
                lhand = i
            else:
                if hand == "right":
                    answer += "R"
                    rhand = i
                else:
                    answer += "L"
                    lhand = i

    return answer

