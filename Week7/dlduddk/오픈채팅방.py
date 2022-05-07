"""
문제 접근
    나갔다가 다시 들어올 때, 또는 이름 변경 -> 들어오고 나갈 때 해당 유저가 사용했던 닉네임 모두 바뀜
해결 전략
    딕셔너리에 key : 유저 아이디 value : 최종 닉네임 저장
"""
def solution(record):
    answer = []
    user = {}

    for i in record: 
        a = i.split(' ')
        if a[0] == 'Enter' or a[0] == 'Change':
            user[a[1]] = a[2]

    
    for i in record:
        a = i.split(' ')
        if a[0] == 'Enter': 
            answer.append(user[a[1]]+"님이 들어왔습니다.")
        elif a[0] == 'Leave': 
            answer.append(user[a[1]]+"님이 나갔습니다.")
        
    return answer