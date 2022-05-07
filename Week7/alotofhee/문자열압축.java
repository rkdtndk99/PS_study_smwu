class Solution {
  public int solution(String s) {
    int answer = s.length();
    for(int i = 1; i <= s.length() / 2; i++) {
      int cnt = 1;
      String str = s.substring(0, i); 
      StringBuilder result = new StringBuilder();
      for(int j = i; j <= s.length(); j += i) {
        String next = "";
        if (j + i > s.length()) {
          next = s.substring(j, s.length());
        }
        else {
          next = s.substring(j, i + j);
        }
        if (str.equals(next)) {
          cnt++;
        }
        else {
          if (cnt != 1) {
            result.append(cnt + str);
          }
          else {
            result.append(str);
          }
          str = next;
          cnt = 1;
        } 
      } 
      result.append(str);
      answer = Math.min(answer, result.length());
    } 
    return answer; 
  } 
}
