import java.util.*;
class Solution {
    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Node> que=new LinkedList<>();
        int count=0;
        int i=0;
        int sum=0;
        while(i<truck_weights.length){
            count++;
            if(que.isEmpty()){
                sum+=truck_weights[i];
                Node node=new Node(truck_weights[i]);
                que.add(node);
                i++;
                continue;
            }
            for(Node node : que){
                node.time++;
            }
            if((sum+truck_weights[i])<=weight){
                    sum+=truck_weights[i];
                    Node node=new Node(truck_weights[i]);
                    que.add(node);
                    i++;
            }
            if(que.peek().time==bridge_length){
                int w=que.poll().weight;
                sum-=w;
            }
        }
        answer=count+bridge_length;
        return answer;
    }
    public static class Node{
        int time;
        int weight;
        Node(int i){
            this.weight=i;
            this.time=1;
        }
    }
}
