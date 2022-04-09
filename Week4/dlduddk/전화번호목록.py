"""
문제 분석
다른 번호의 접두어인 경우가 있다면 false 아니면 true

해결 전략
우선 0~9를 키로하고, 각 숫자로 시작하는 전화번호를 value에 넣고, 각 value sort() 하자

시간초과를 피하기 위한 노력들
length, k_len, j_len 미리 구해놓고 이용하기
k_len, j_len 모두 2 이상인 경우에만 검사, 아닌 경우 return False (한 자리수인 경우이므로)
    2 이상인 경우니까 두번째 글자 검사 먼저 해보고 startswith 쓰기
        이때, 두번째 숫자 다르면 정렬해놓은 상태이므로 나머지 전화번호에서도 두번째 숫자 다르므로 for문 break함
    startswith 이거 하기 전에 k_len > j_len 검사해놓기(>=도 안 됨! 어차피 중복 전화번호 없다니까)
"""
def solution(phone_book):
    dictionary = {i:[] for i in range(10)}
    
    for i in phone_book:
        dictionary[int(i[0])].append(i)
        
    for i in range(10):
        dictionary[i].sort()
    
    for i in range(10):
        length = len(dictionary[i])
        for j in range(length):
            for k in range(j+1, length):
                k_len = len(dictionary[i][k])
                j_len = len(dictionary[i][j])
                if k_len >= 2 and j_len >= 2 :
                    if dictionary[i][k][1]==dictionary[i][j][1] and k_len > j_len: 
                    
                        if dictionary[i][k].startswith(dictionary[i][j]):
                            return False
                    else: # 두번째 자리 수가 다름 -> 정렬을 이미 했기 때문에 두번째 자리 수가 다르면 나머지 비교할 필요 없음
                        break
                else: # 둘 중 하나가 한 자리 수 -> 한 자리 수이면 무조건 접두어임
                    return False
                        
    return True # 이전에 False가 안되었으면 True야
    