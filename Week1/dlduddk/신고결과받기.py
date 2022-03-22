"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

"""
"""
문제 분석
각 유저는 한 번에 한 명의 유저 신고 가능.
    신고 횟수 제한 없음. 서로 다른 유저 계속 신고 가능
    한 유저 여러 번 신고 가능. but 동일한 유저에 대해 신고 횟수 1회로 처리됨.
k번 이상 신고된 유저는 게시판 이용 정지. 해당 유저를 신고했던 모든 유저에게 정지 사실 알림.
    유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지 메일 발송

해결 전략
k번 이상 신고당한 유저 발생 시, 해당 유저를 신고한 유저들에게 메일 발송 해야 함.
-> 신고 당하는 유저에 대해서 리스트든 딕셔너리든 만들자

한 유저가 특정 유저 반복 신고 시, 중복은 카운트하면 안 됨.
-> 신고 당하는 유저 : [그 유저를 신고한 유저] 형식으로 딕셔너리를 만들고, 신고 당하는 유저의 value에 해당하는 리스트에 신고한 유저가 있다면 continue 하자

유저가 신고한 내용 취합해서 메일 발송
-> 위에서 만든 딕셔너리의 value 길이가 k 이상인 경우, value 안의 유저들의 값 +1
"""
def solution(id_list, report, k):
    length = len(id_list)
    answer = [0]*length
    user = {}
    user2 = {}
    idx = 0
    for i in id_list:# 딕셔너리 초기화
        user[i] = [] # value : i를 신고한 유저들
        user2[i] = idx  # value : i의 인덱스
        idx += 1

    for i in report:
        a, b = i.split()[0], i.split()[1] # a: 신고함, b: 신고당함
        if a not in user[b]: # b를 신고한 사람 중에 a가 없다면 추가
            user[b].append(a)

    for i in range(length):
        if len(user[id_list[i]]) >= k:# user[id_list[i]]가 k번 이상 신고당하면
            for j in user[id_list[i]]: # user[id_list[i]](즉 id_list[i]를 신고한 유저들)의 인덱스에 대해서 answer +=1 함
                answer[user2[j]]+=1 # user2는 id_list에 있는 id와 인덱스 매치해주는 딕셔너리
    return answer