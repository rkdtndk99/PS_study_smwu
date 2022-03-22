"""
커밋 : MM/DD(DAY)_(PRGM or BOJ)_Lv.(1 or 2 or 3)

"""
"""
문제 분석
규칙
    3<= 길이 <=15
    알파벳 소문자, 숫자, -, _, . 만 사용 가능
    .은 처음과 끝에 사용 불가! 연속 사용 불가!
새로운 아이디 추천 전략
    대문자 -> 소문자
    알파벳 소문자, 숫자, -, _, . 제외 모든 문자 제거
    . 이 2번 이상 연속된 부분은 .으로 치환
    . 이 처음이나 마지막에 위치하면 제거
    빈 문자열이라면 a 대임
    16자 이상이면, 첫 15자 이후 문자 제거
        만약 제거 후 .가 아이디 끝에 위치한다면 제거
    2자 이하라면 마지막 문자를 3자가 될 때까지 반복
해결 전략
그냥 시키는대로 하기
"""
def solution(new_id):
    answer = ''
    new_id_list = list(new_id)
    length = len(new_id_list)
    alpha_dict ={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
    small_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    nums = ['0','1','2','3','4','5','6','7','8','9']
    # 대문자 -> 소문자
    for i in range(length):
        if new_id_list[i] in alpha_dict.keys():
            new_id_list[i] = alpha_dict[new_id_list[i]]
    # 알파벳, 숫자, -, _, . 제외 삭제
    for i in range(length):
        if new_id_list[i] in small_alpha:
            continue
        elif new_id_list[i] in nums:
            continue
        elif new_id_list[i] in ['-','_','.']:
            continue
        else:
            new_id_list[i] = '+'
    while '+' in new_id_list:
        new_id_list.remove('+')
    
    # '.'이 두번 이상 연속되면 하나로 바꾸기
    length = len(new_id_list)
    for i in range(1,length):
        if new_id_list[i-1] in ['.','+'] and new_id_list[i]=='.':
            new_id_list[i]='+'
    while '+' in new_id_list:
        new_id_list.remove('+')
    
    # '.'이 처음이나 끝에 있으면 제거
    length = len(new_id_list)
    if new_id_list[length-1] == '.':
        del new_id_list[length-1]
    if new_id_list and new_id_list[0] == '.':
        del new_id_list[0]
    
    # 빈 문자열이라면 'a' 추가
    if not new_id_list:
        new_id_list.append('a')
    
    # 길이가 16자 이상이라면
    if len(new_id_list) >= 16:
        new_id_list = new_id_list[:15]
        if new_id_list[-1] == '.':
            del new_id_list[-1]
    # 길이가 2자 이하라면
    if len(new_id_list) <= 2:
        temp = new_id_list[-1]
        #print(temp)
        while len(new_id_list) != 3:
            new_id_list.append(temp)
    
    answer = ''.join(new_id_list)
            
    return answer