import java.util.*;
class Solution {
    public static String solution(String p) {
        if(isCorrect(p)){
            return p;
        }

        return test2(p);
    }
    public static String test2(String w){
        if(isNull(w)){
            return "";
        }
        //2. 문자열 w를 균형잡힌 문자열 u,v로 분리
        //균형잡힌 문자열==(,)개수가 같기만 하면 됨
        String u="";
        String v="";
        int left=0;
        int right=0;
        for(int i=0;i<w.length();i++){
                if(w.charAt(i)=='('){
                    left++;
                }else if(w.charAt(i)==')'){
                    right++;
                }
            if(left==right&&(left!=0&&right!=0)){
                u=w.substring(0,i+1);
                if((i+1)!=w.length()){
                    v=w.substring(i+1,w.length());
                }
                break;
            }
        }
        if(isCorrect(u)){
            return u+test2(v);
        }else{
            //4-1 "(" 맨 처음에 붙이기+reculsion
            String tmp="("+test2(v);
            //4-2 맨 뒤에 ")"
            tmp+=")";
            //u의 첫 문자와 마지막 문자 제거
            u=u.substring(1,u.length()-1);
            //나머지 문자열의 괄호방향 뒤집기
            u=u.replace("(","~");
            u=u.replace(")","(");
            u=u.replace("~",")");
            tmp+=u;
            return tmp;
        }

    }
    //1. 빈 문자열 -> 빈 문자열 반환
    public static boolean isNull(String w){
        if(w.isEmpty()){
            return true;
        }
        return false;
    }
    //3. u가 올바른 문자열인지 확인
    public static boolean isCorrect(String u){
        Stack<Character> stack=new Stack<>();
        for(int i=0;i<u.length();i++){
            if(u.charAt(i)=='('){
                stack.add('(');
            }else{
                if(stack.isEmpty()){
                    //올바른 문자열 x case
                    return false;
                }
                stack.pop();
            }
        }
        if(!stack.isEmpty()){
            //올바른 문자열 x case
            return false;
        }
        return true;
    }
}
