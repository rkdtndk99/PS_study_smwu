import java.util.*;
class Solution {
   public static int solution(int[] citations) {
        int answer = 0;
        Integer[] temp=new Integer[citations.length];
        for(int i=0;i<citations.length;i++){
            temp[i]=citations[i];
        }
        Arrays.sort(temp,Collections.reverseOrder());
        if(temp[citations.length-1]>citations.length){
            return citations.length;
        }
        int index=0;
        for(int i=0;i<citations.length;i++){
            if(temp[i]>i+1){
                continue;
            }
            index=i;
            break;
        }
        if(index>temp[index]){
            answer=index;
        }else{
            answer=temp[index];
        }
        return answer;
    }
}
