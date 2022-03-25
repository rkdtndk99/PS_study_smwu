class Solution {
    public int solution(String s) {
        int answer = 0;
        String numArray[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < numArray.length; i++) {
            s = s.replace(numArray[i], Integer.toString(i));
        }
        answer = Integer.parseInt(s);
        return answer;
    }
}

/* 해결 전략 
숫자에 대응되는 영단어 배열 생성 (인덱스 값과 대응되는 영단어 숫자가 같게 됨)
s 문자열에서 numArray[i] 값과 대응되는 문자열을 replace 사용하여 i로 대체함.
(이 때 i를 string으로 타입 일치시켜주기)
문자열 s를 int로 변환
*/

//다른사람의 풀이
import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        StringBuilder sb = new StringBuilder("");
        int len = s.length();
        String[] digits = {"0","1","2","3","4","5","6","7","8","9"};
        String[] alphabets = {"zero","one","two","three","four","five","six","seven","eight","nine"};

        for(int i=0; i<10; i++){
            s = s.replaceAll(alphabets[i],digits[i]);
        }

        return Integer.parseInt(s);
    }
}
