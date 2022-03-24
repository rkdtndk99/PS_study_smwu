package com.company;

public class Main {
    class Solution {
        public String solution(int[] numbers, String hand) {
            String answer = "";
            //키패드 생성
            int[][] pad=new int[4][3];
            int num=1;
            for(int i=0;i<4;i++){
                for(int j=0;j<3;j++){
                    pad[i][j]=num++;
                }
            }
            //손가락의 위치 각각 생성
            Position left=new Position(3,0);
            Position right=new Position(3,2);
            //numbers 배열 돌면서 손가락 위치 바꿔줌
            for(int i=0;i<numbers.length;i++){
                int n=numbers[i];
                if(n==1||n==4||n==7){
                    left.x=0;
                    if(n==1){
                        left.y=0;
                    }
                    if(n==4){
                        left.y=1;
                    }
                    if(n==7){
                        left.y=2;
                    }
                    answer+="L";
                    continue;
                }
                if(n==3||n==6||n==9){
                    right.x=2;
                    if(n==3){
                        right.y=0;
                    }
                    if(n==6){
                        right.y=1;
                    }
                    if(n==9){
                        right.y=2;
                    }
                    answer+="R";
                    continue;
                }
                if(n==0){
                    n=11;
                }
                //2,5,8,0 l_count
                int l_count=0;
                int tmp_y=left.y;
                while(pad[tmp_y][1]!=n){
                    if(pad[tmp_y][1]>n){
                        tmp_y--;
                    }else if(pad[tmp_y][1]<n){
                        tmp_y++;
                    }
                    l_count++;
                }
                if(left.x==0){
                    l_count++;
                }
                //2,5,8,0 r_count
                int r_count=0;
                tmp_y=right.y;
                while(pad[tmp_y][1]!=n){
                    if(pad[tmp_y][1]>n){
                        tmp_y--;
                    }else if(pad[tmp_y][1]<n){
                        tmp_y++;
                    }
                    r_count++;
                }
                if(right.x==2){
                    r_count++;
                }
                //l_count vs r_count
                if(l_count>r_count){
                    right.x=1;
                    right.y=tmp_y;
                    answer+="R";
                }else if(l_count<r_count){
                    left.x=1;
                    left.y=tmp_y;
                    answer+="L";
                }else if(l_count==r_count){
                    //오른손잡이 vs 왼손잡이
                    if(hand.equals("right")){
                        right.x=1;
                        right.y=tmp_y;
                        answer+="R";
                    }else{
                        left.x=1;
                        left.y=tmp_y;
                        answer+="L";
                    }
                }


            }
            return answer;
        }
        class Position{
            int x;
            int y;
            Position(int y,int x){
                this.y=y;
                this.x=x;

            }
        }
    }
    public static void main(String[] args) {
	// write your code here
    }
}
