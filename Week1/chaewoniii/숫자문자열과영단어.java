package com.company;

public class Main {
    class Solution {
        public int solution(String s) {
            int answer = 0;
            String ans="";
            for(int i=0;i<s.length();i++){
                char c=s.charAt(i);
                if(c>='0'&&c<='9'){
                    ans+=c;
                }
                switch(c){
                    case 'z':
                        i=i+3;
                        ans+='0';
                        break;
                    case 'o':
                        i=i+2;
                        ans+='1';
                        break;
                    case 't':
                        if(s.charAt(i+1)=='w'){
                            i=i+2;
                            ans+='2';
                        }
                        if(s.charAt(i+1)=='h'){
                            i=i+4;
                            ans+='3';
                        }
                        break;
                    case 'f':
                        if(s.charAt(i+1)=='o'){
                            i=i+3;
                            ans+='4';
                        }
                        if(s.charAt(i+1)=='i'){
                            i=i+3;
                            ans+='5';
                        }
                        break;
                    case 's':
                        if(s.charAt(i+1)=='i'){
                            i=i+2;
                            ans+='6';
                        }
                        if(s.charAt(i+1)=='e'){
                            i=i+4;
                            ans+='7';
                        }
                        break;
                    case 'e':
                        i=i+4;
                        ans+='8';
                        break;
                    case 'n':
                        i=i+3;
                        ans+='9';
                        break;
                }
            }
            answer=Integer.parseInt(ans);
            return answer;
        }
    }
    public static void main(String[] args) {
	// write your code here
    }
}
