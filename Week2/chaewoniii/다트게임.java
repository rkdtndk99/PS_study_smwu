class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int[] score=new int[3];
        int k=0;
        for(int i=0;i<dartResult.length();i++){
            char c=dartResult.charAt(i);
            if(c>='0'&&c<='9'){
                if(c=='1'&&dartResult.charAt(i+1)=='0'){
                    score[k]=10;
                    i++;
                }else{
                    score[k]=c-'0';
                }
                k++;
                continue;
            }
            switch(c){
                case 'S':
                    break;
                case 'T':
                    score[k-1]=(int)Math.pow(score[k-1],3);
                    break;
                case 'D':
                    score[k-1]=(int)Math.pow(score[k-1],2);
                    break;
                case '*':
                    if((k-1)==0){
                        score[k-1]=score[k-1]*2;
                        break;
                    }
                    score[k-1]=score[k-1]*2;
                    score[k-2]=score[k-2]*2;
                    break;
                case '#':
                    score[k-1]=-score[k-1];
                    break;
            }
             
        }
        for(int i:score){
            answer+=i;
        }
        return answer;
    }
}
