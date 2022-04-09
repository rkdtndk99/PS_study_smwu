class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] score = new int[3];
        int[] person1 = {1, 2, 3, 4, 5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == person1[i % 5]) {
                score[0]++;
            }
            if (answers[i] == person2[i % 8]) {
                score[1]++;
            }
            if (answers[i] == person3[i % 10]) {
                score[2]++;
            }
        }
        int maxScore = Math.max(Math.max(score[0], score[1]), score[2]);
        int maxPerson = 0;
        for (int i = 0; i < 3; i++) {
            if (maxScore == score[i])
                maxPerson++;
        }
        answer = new int[maxPerson];
        int k = 0;
        for (int j = 0; j < 3; j++) {
            if (maxScore == score[j])
                answer[k++] = j + 1;
        }
        return answer;
    }
}
