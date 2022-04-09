"""
문제 분석
서로 다른 옷의 조합 수 리턴
해결 전략
딕셔너리로 입력 저장 
옷 종류 : 의상 종류 개수

"""

def solution(clothes):
    li = []
    for i in clothes:
        li.append(i[1])
    li = set(li)
    # 각 clothes 종류마다 의상 수 0으로 초기화
    dictionary = {i : 0 for i in li}
    
    # 각 clothes 종류마다 의상 수 세아리기
    for i in clothes:
        dictionary[i[1]]+=1

    
    cnt = []
    for i in dictionary.keys():
        cnt.append(dictionary[i]+1) # 각 의상수 종류마다 (의상 수 +1)을 cnt에 추가
        """
        a,b,c + 선택x -> 4
        d,e + 선택x -> 3
        f,g + 선택x -> 3
        4*3*3 - 1(모두 선택x인 경우)
        """
    answer = 1    
    for i in cnt:
        answer *= i
    return answer-1
    