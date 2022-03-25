class Solution {
    public String solution(String new_id) {
        String answer = "";
        //step1
        answer = new_id.toLowerCase();
        //step2
        String temp2 = "";
        for (int i = 0; i < answer.length(); i++) {
        	char c = answer.charAt(i);
        	if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || c == '-' || c == '_' || c == '.') {
        		temp2 += c;
        	}
        }
        answer = temp2;
        //step3
        String temp3 = answer.toString().replace("..", ".");
        while (temp3.contains("..")) {
        	temp3 = temp3.replace("..", ".");
        }
        answer = temp3;
        //step4
        if (answer.length() > 0) {
            if (answer.charAt(0) == '.') {
                answer = answer.substring(1, answer.length());
            }
        }
        if (answer.length() > 0) {
            if (answer.charAt(answer.length() - 1) == '.') {
                answer = answer.substring(0, answer.length() - 1);
            }
        }
        //step5
        if (answer.length() == 0) {
        	answer = "a";
        }
        //step6
        if (answer.length() >= 16) {
        	answer = answer.substring(0, 15);
        	if (answer.charAt(answer.length() - 1) == '.') {
        		answer = answer.substring(0, answer.length() - 1);
        	}
        }
        //step7
        if (answer.length() <= 2) {
        	char c = answer.charAt(answer.length() - 1);
        	while (answer.length() < 3) {
        		answer += c;
        	}
        }
        return answer;
    }
}

/* 해결 전략
단계별로 해결
step4 실행시 문자열 크기 0보다 커아햠.
charAt 사용시 인덱스 범위 주의하기 (StringIndexOutOfBoundsException)
*/

//다른사람의 풀이
class Solution {
    public String solution(String new_id) {
        String answer = "";
        String temp = new_id.toLowerCase();

        temp = temp.replaceAll("[^-_.a-z0-9]","");
        System.out.println(temp);
        temp = temp.replaceAll("[.]{2,}",".");
        temp = temp.replaceAll("^[.]|[.]$","");
        System.out.println(temp.length());
        if(temp.equals(""))
            temp+="a";
        if(temp.length() >=16){
            temp = temp.substring(0,15);
            temp=temp.replaceAll("^[.]|[.]$","");
        }
        if(temp.length()<=2)
            while(temp.length()<3)
                temp+=temp.charAt(temp.length()-1);

        answer=temp;
        return answer;
    }
}


