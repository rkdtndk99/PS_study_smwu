"""
문제 분석
    문자 1개, 2개, 3개, ... 단위로 잘라서 압축해서 제일 짧게 압축하는 경우의 길이 리턴
해결 전략
    직접 1개부터 length//2개 단위까지 시도해보기
"""

def solution(s):
    if len(s)==1:
        return 1
    
    min_len = 1001
    length = len(s)
    length2 = length//2 # 단위 길이의 최대는 len(s)/2
    
    for i in range(1, length2+1): # 단위 길이
        candidate = []
        
        tmp = s[:i]
        cnt = 1
        for j in range(i,length+i, i): # s[:i] 와 s[i:i+i]부터 비교해야하므로, i로 시작.
            # range(i, length,i)로 두면 후처리 필요한데 귀찮음
            if s[j:j+i] == tmp:
                cnt+=1
            else:
                if cnt != 1:
                    candidate.append(str(cnt))
                    cnt = 1
                candidate.append(tmp)
                tmp = s[j:j+i]
            """
            a = "aabbaccc"
            for i in range(13):
            print(a[:i])
            
            a
            aa
            aab
            aabb
            aabba
            aabbac
            aabbacc
            aabbaccc
            aabbaccc
            aabbaccc
            aabbaccc
            aabbaccc
            """

        string = ''.join(candidate)

        if len(string) < min_len:
            min_len = len(string)
        
    return min_len