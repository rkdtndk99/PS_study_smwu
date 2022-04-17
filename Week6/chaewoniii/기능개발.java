import java.util.*;
class Solution {
    public static int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        //queue
        int size=progresses.length;
        int[] temp=new int[size];
        Queue<Integer> que=new LinkedList<>();
        for(int i=0;i<size;i++){
            //순서대로 넣음
            //2.xxx일이 소요된다면 3일 뒤에 배포됨
            //그리고 올림할라면 double로 받고 올림하고 정수로 바꿔줘야함
            que.add((int)Math.ceil((double)(100-progresses[i])/speeds[i]));
        }
        //앞에서부터 뽑음
        int k=0;
        while(!que.isEmpty()){
            double x=que.poll();
            temp[k]++;
            if(que.isEmpty()){
                k++;
                break;
            }
            while(x>=que.peek()){
                temp[k]++;
                que.poll();
                if(que.isEmpty()) break;
            }
            k++;
        }
        //5 10 1 1 20 1
        //1 3

        answer=new int[k];
        for(int i=0;i<k;i++){
            answer[i]=temp[i];
        }
        return answer;
    }
}
