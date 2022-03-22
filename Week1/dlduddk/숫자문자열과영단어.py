"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

"""
"""
문제 분석
"one4seveneight" 이런식으로 입력되면 1478 이런식으로 반환해라
해결 전략
딕셔너리로 풀자

"""

def solution(s):
    nums = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    length = len(s)
    new_s = list(s)
    idxs = []
    
    for i in range(length):
        if 'a'<=(new_s[i])<='z':
            for j in range(i+1, length+1):
                if ''.join(new_s[i:j]) in nums.keys():
                    idxs.append((i,j))
                    break
    
    new_s2 = []
    if idxs:
        new_s2 = new_s[:idxs[0][0]]
        
        length = len(idxs)
        if length == 1:
            new_s2 += list(nums[''.join(new_s[idxs[0][0]:idxs[0][1]])])
            new_s2 += new_s[idxs[0][1]:]
        else:
            for i in range(length-1):
                new_s2 += list(nums[''.join(new_s[idxs[i][0]:idxs[i][1]])])
                new_s2 += new_s[idxs[i][1]:idxs[i+1][0]]
                #print(nums[''.join(new_s[idxs[i][0]:idxs[i][1]])])

            new_s2 += list(nums[''.join(new_s[idxs[i+1][0]:idxs[i+1][1]])])
            new_s2 += new_s[idxs[i+1][1]:]
    else:
        new_s2 = new_s
    
    new_s2 = int(''.join(new_s2))
    return new_s2

