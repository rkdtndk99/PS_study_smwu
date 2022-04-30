import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        int[] tmp = new int[progresses.length];
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int percent = 100 - progresses[i];
            int days = percent / speeds[i];
            if (percent % speeds[i] != 0) {
                days++;
            }
            queue.add(days);
        }
        
        int endDay = queue.poll();
        int task = 1;
        int index = 0;
        while(!queue.isEmpty()) {
            int progress = queue.poll();
            if (progress <= endDay) {
                task++;
            }
            else {
                tmp[index] = task;
                index++;
                task = 1;
                endDay = progress;
            }
        }
        tmp[index] = task;
        answer = new int[index + 1];
        for (int i = 0; i < index + 1; i++) {
            answer[i] = tmp[i];
        }
        return answer;
    }
}
