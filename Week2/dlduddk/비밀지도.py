"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)
"""
"""
문제 분석
한 변의 길이가 n인 정사각형 배열 형태,  "공백"(" ") 또는 "벽"("#") 두 종류로 이루어짐
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있음
지도 1 or 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽
지도 1 and 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백
정수 배열로 암호화,  벽 부분을 1, 공백 부분을 0

해결전략
일단 2진수로 만들기
if arr1[i][j] + arr2[i][j] > 0 -> 벽
else -> 공백
"""
def solution(n, arr1, arr2):
    answer = []

    # 이진수 만들기
    for i in range(n):
        temp1, temp2 = [], []
        num = 2**(n-1)
        for j in range(n):
            temp1.append(arr1[i]//num)
            arr1[i] %= num
            
            temp2.append(arr2[i]//num)
            arr2[i] %= num
            
            num //= 2
        arr1[i] = temp1
        arr2[i] = temp2

    # 벽인지 공백인지 구분하기
    for i in range(n):
        temp = ""
        for j in range(n):
            if arr1[i][j] + arr2[i][j] > 0:
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer