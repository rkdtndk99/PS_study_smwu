import java.util.Arrays;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int lostNum = 0, trueNum = 0;
        for (int i = 0; i < 6; i++) {
            if (lottos[i] == 0){
                lostNum++;
            }
            for (int j = 0; j < 6; j++){
                if (lottos[i] == win_nums[j]){
                    trueNum++;
                    break;
                }
            }
        }
        if (trueNum == 0){
            answer[1] = 6;
        }
        else {
            answer[1] = 7 - trueNum;
        }
        if (trueNum + lostNum >= 6) {
            answer[0] = 1;
        }
        else if (trueNum + lostNum == 0) {
            answer[0] = 6;
        }
        else {
            answer[0] = 7 - (trueNum + lostNum);
        }
        return answer;
    }
}
