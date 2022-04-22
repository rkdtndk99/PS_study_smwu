"""
문제 분석
    하루에 한 번 배포 가능
    기능마다 개발 속도 다름
해결 전략
    각 기능마다 며칠 후에 완성되는지 리스트에 담아
"""
def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    finish = []
    for i in range(length):
        tmp = (100-progresses[i])//speeds[i]
        if speeds[i]*tmp+progresses[i] < 100:
            tmp+=1
        finish.append(tmp)
    
    maxval = finish[0]
    cnt=1
    # 7 3 9
    # 5 10 1 1 20 1
    for i in finish[1:]:
        if i > maxval: # maxval보다 크면 앞에 누적된 cnt 리스트에 넣고, maxval 업데이트
            maxval = i
            answer.append(cnt)
            cnt=1
        else: # maxval보다 작으면 앞에 밀린 작업때문에 배포 못하는 작업임. cnt+=1 
            cnt+=1
    answer.append(cnt)
    
    return answer
