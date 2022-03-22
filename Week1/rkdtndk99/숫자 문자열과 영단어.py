# 내 풀이
def solution(s):
    dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9}
    answer = ""
    temp = ""
    arr = list(s)
    for i in range(len(arr)):
        if arr[i].isdigit():
            answer += arr[i]
            temp = ""
        else:
            temp += arr[i]
            if temp in dict:
                answer += str(dict[temp])
                temp = ""

    return int(answer)

# 다른 사람 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
  
 
