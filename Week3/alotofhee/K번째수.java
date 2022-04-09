import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            for (int j = 0; j < 3; j++) {
                int[] temp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
                Arrays.sort(temp);
                answer[i] = temp[commands[i][2] - 1];
            }
        }
        return answer;
    }
}
