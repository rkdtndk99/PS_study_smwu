import java.util.*;
class Solution {
    public static int[] solution(int N, int[] stages) {
            int[] answer = new int[N];
            int[] current=new int[N];
            double[] failure=new double[N];
            double[] temp=new double[N];
            int num=stages.length;
            for(int i:stages){
                if(i>N){
                    continue;
                }
                current[i-1]++;
                //{1,3,2,1,0}
            }
            for(int i=0;i<N;i++){
                if(i!=0) {
                    num = num - current[i - 1];
                }
                if(num==0){
                    failure[i]=0;
                    break;
                }
                failure[i]=(double)current[i]/num;
            }
            int k=0;
            for(double i:failure){
                temp[k]=i;
                k++;
            }
            k=0;
            Arrays.sort(temp);
            for(int i=N-1;i>=0;i--){
                for(int j=0;j<N;j++){
                    if(temp[i]==failure[j]){
                        answer[k++]=j+1;
                        System.out.println(j+1);
                        failure[j]=2;
                    }
                }
            }
            return answer;
        }
        
    
}
