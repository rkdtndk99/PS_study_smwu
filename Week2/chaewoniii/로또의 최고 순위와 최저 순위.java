class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int count=0;
        int zero_num=0;
        for(int n : lottos){
            int num=n;
            if(n==0){
                zero_num++;
                continue;
            }
            for(int k : win_nums){
                if(n==k){
                    count++;
                }
            }
        }
        answer[0]=rank(count+zero_num);
        answer[1]=rank(count);
        return answer;
    }
    
    public int rank(int n){
        int r=0;
        switch(n){
            case 6: r=1;
                break;
            case 5 : r=2;
                break;
            case 4 : r=3;
                break;
            case 3 : r=4;
                break;
            case 2 : r=5;
                break;
            default : r=6;
                break;
        }
        return r;
    }
}
