import java.util.*;
class Solution {
    public static int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Node> que=new LinkedList<>();
        for(int i=0;i<priorities.length;i++){
            Node node=new Node(priorities[i],i);
            que.offer(node);
        }
        int count=0;
        while(!que.isEmpty()){
            Node temp=que.poll();
            boolean inOrdered=false;
            for(Node node : que){
                if(node.priority>temp.priority){
                    que.add(temp);
                    inOrdered=true;
                    break;
                }
            }
            if(!inOrdered){
                count++;
                if(temp.index==location){
                    break;
                }
            }
        }
        answer=count;
        return answer;
    }
    static class Node {
        int priority;
        int index;
        Node(int p,int i){
            this.priority=p;
            this.index=i;
        }

    }
}
