class Solution {
    public int solution(String dartResult) {
        int answer = 0;
                int score[] = new int[3];
        int numIndex = 0;
        int num = 0;
        for (int i = 0; i < dartResult.length(); i++) {
            char c = dartResult.charAt(i);
            if (c >= '0' && c<= '9') {
                num = Character.getNumericValue(c);
                if (num == 1 && dartResult.charAt(i + 1) == '0') {
                    num = 10;
                    i++;
                }
            }
            else {
                switch(c) {
                case 'S':
                    score[numIndex++] = (int) Math.pow(num, 1);
                    break;
                case 'D':
                    score[numIndex++] = (int) Math.pow(num, 2);
                    break;
                case 'T':
                    score[numIndex++] = (int) Math.pow(num, 3);
                    break;
                case '*':
                    if (numIndex - 2 >= 0) {
                        score[numIndex - 2] *= 2;
                        score[numIndex - 1] *= 2;
                    }
                    else {
                        score[numIndex - 1] *= 2;
                    }
                    break;
                case '#':
                    score[numIndex - 1] *= -1;
                    break;
                }
            }
        }
        for (int j = 0; j < score.length; j++) {
            answer += score[j];
        }
        return answer;
    }
}
