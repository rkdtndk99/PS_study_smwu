# 내 풀이
def solution(id_list, report, k):
    # 받을 이메일 개수
    answer = {id: 0 for id in id_list}

    # 리스트 내 중복되는 값 무시하기 위해서
    report = list(set(report))
    r = {id: [] for id in id_list}

    for i in range(len(report)):
        user, warn = report[i].split()
        r[warn].append(user)

    for item, value in r.items():
        if len(value) >= k:
            for key in value:
                answer[key] += 1

    return list(answer.values())

# 다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
