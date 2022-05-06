import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = s.length();
        for(int i=1;i<=s.length()/2;i++){
            int current=1;//현재 압축 정도
            String zip=s.substring(0,i); //압축할 문자
            StringBuilder result=new StringBuilder(); //압축완료한 문자를 저장할 StringBuilder
            for(int j=i;j<=s.length();j+=i){
                //다음 문자 추출
                String next=s.substring(j,j+i > s.length()?s.length():i+j);
                //다음 문자와 현재 문자가 같으면 zip 증가
                if(zip.equals(next)) current++;
                //다음 문자와 현재 문자가 다를 경우
                else{
                    //압축이 안 됐을 경우는 공백, 압축이 됐을경우 zip을 붙여줌+압축할 문자를 넣어준다
                    result.append((current != 1? current:"")+zip);
                    zip=next;//다음 문자를 압축할 문자로 지정
                    current=1;//압축 정도 1로 초기화
                }
            }
            result.append(zip); //마지막에 추가 안 된 zip추가
            answer=Math.min(answer,result.length()); //가장 작은 문자열 길이 저장
        }
        return answer;
    }
}
