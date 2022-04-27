import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Queue<Node> que=new LinkedList<>();
        for(int i : prices){
            Node node=new Node(i);
            que.add(node);
        }
        int k=0;
        while(!que.isEmpty()){
            Node temp=que.poll();
            int count=0;
            for(Node node : que){
                 count++;
                if(temp.price>node.price){
                   break;
                }
            }
            answer[k++]=count;
        }
        
        return answer;
    }
    class Node{
        int price;
        Node(int x){
            this.price=x;
        }
    }
}
