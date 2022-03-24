package com.company;

public class Main {
    class Solution {
        public int solution(int[][] board, int[] moves) {
            int answer = 0;
            int[] arr=new int[1000];
            int top=-1;
            for(int i=0;i<moves.length;i++){
                int j=0;
                int k=moves[i]-1;
                while(j<board.length){
                    if(board[j][k]!=0){
                        arr[++top]=board[j][k];
                        board[j][k]=0;
                        break;
                    }
                    j++;
                }
                if(top>0){
                    if(arr[top]==arr[top-1]){
                        arr[top]=0;
                        arr[top-1]=0;
                        top-=2;
                        answer+=2;
                    }
                }


            }
            return answer;
        }
    }
    public static void main(String[] args) {
	// write your code here
    }
}
