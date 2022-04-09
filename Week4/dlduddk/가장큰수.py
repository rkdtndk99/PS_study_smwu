"""
문제 분석
주어진 0 또는 양의 정수를 이어붙여 만들 수 있는 가장 큰 수 알아내기

해결 전략
문자열로 해서 정렬하기 
이때 numbers의 원소는 1000 이하이므로, 모든 숫자 최소 4자리로 만들어서 비교하기
"""

def solution(numbers):
    temp = []
    for i in numbers:
        temp.append(str(i))
    temp.sort(key = lambda x : x*4,reverse=True)
    # temp = ['3', '30', '34', '5', '9'] -> '3333', '30303030','34343434','5555','9999'로 비교
    #print(temp)
    #print('3333'>'30303030') # True로 출력됨(두번째 숫자가 왼쪽이 더 큼) -> '30','3' 순서인데 reverse하니까 '3','30'이 됨
    answer = ''.join(temp) # 이 상태로 끝내면 실패 뜸
    
    # 이 부분은 구글링 함.
    # 모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.
    return str(int(answer)) 
    
    
