"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

"""
"""
문제 분석
다트 점수 계산 로직
- 3번 다트 던짐
- 각 기회마다 0~10점 얻을 수 있음
- single, double, triple 영역 존재, 각 영역 당첨 시 점수의 1제곱, 2제곱, 3제곱으로 계산
- 스타상 당첨 시, 해당 점수 및 직전에 얻은 점수 2배로 만듦.
    - 맨 처음에 스타상 당첨 시, 해당 점수만 2배
    - 스타상 효과 중첩 가능
- 아차상 당첨 시, 해당 점수만큼 마이너스
- 스타상 효과와 아차상 효과 중첩 가능
- s, d, t는 점수마다 하나씩 존재
- 스타상, 아차상은 점수마다 둘 중 하나만 존재 가능, 존재 안 할 수도 있음

해결 전략
숫자, s,d,t + 스타상, 아차상에 대한 리스트([(1,s,.),(2,d,*),(3,t,#)] 이런식) 만들기
시간은 걱정 없을 듯하니 편하게 구현이나 하자
"""

def solution(dartResult):
    answer = 0
    dartResult = list(dartResult)
    length = len(dartResult)
    s,e = 0,1
    arr = []
    # 초기 설정1
    for i in range(length):
        if dartResult[i] in ['S','D','T']: # s,d,t 기준으로 한 칸 뒤에 *이나 # 있는지 확인
            if i+1 < length and dartResult[i+1] in ['*','#']: # 있다면 그 칸까지 포함
                e = i+2
                if i+2 < length:
                    arr.append(dartResult[s:e])
                else:
                    arr.append(dartResult[s:])
            else: # 없다면 지금 칸까지 포함
                e = i+1
                arr.append(dartResult[s:e])
            s = e
            e = e+1
    # arr = [['1', 'D'], ['2', 'S', '#'], ['1', '0', 'S']]
    
    # 초기 설정2
    length = len(arr)
    for i in range(length):
        a,b,c='','','.'
        for j in arr[i]:
            if '0'<=j<='9':
                a+=j
            if j in ['S','D','T']:
                b=j
            if j in ['#','*']:
                c=j
        arr[i] = [int(a),b,c]
    # arr = [[1, 'D', '.'], [2, 'S', '#'], [10, 'S', '.']]
    
    # res 초기화로 조건 안 걸린 그냥 점수
    res = [i[0] for i in arr] # [1,2,10]    
    for i in range(length):
        # D나 T일 때 처리
        if arr[i][1] == 'D':
            res[i]= res[i]**2
        elif arr[i][1] == 'T':
            res[i] = res[i]**3
            
        # 아차상, 스타상 처리
        if arr[i][2] == '#':
            res[i] = res[i]*(-1)
        elif arr[i][2] == '*':
            if i-1 >= 0: # 두번째 이후 자리
                res[i-1]*=2
                res[i]*=2
            else: # 첫번째자리
                res[i]*=2
        

    return sum(res)