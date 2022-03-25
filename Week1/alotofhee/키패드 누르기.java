class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int left = 10, right = 12;
        int lDistance, rDistance;

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
                answer += "L";
                left = numbers[i];
            }
            else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
                answer+= "R";
                right = numbers[i];
            }
            else {
                if (numbers[i] == 0) {
                    numbers[i] = 11;
                }
                lDistance = Math.abs(numbers[i] - left) / 3 + Math.abs(numbers[i] - left) % 3;
                rDistance = Math.abs(numbers[i] - right) / 3 + Math.abs(numbers[i] - right) % 3;
                if (lDistance == rDistance) {
                    if (hand.equals("left")){
                        answer += "L";
                        left = numbers[i];
                    }
                    else {
                        answer += "R";
                        right = numbers[i];
                    }
                }
                else if (lDistance < rDistance) {
                    answer += "L";
                    left = numbers[i];
                }
                else {
                    answer += "R";
                    right = numbers[i];
                }
            }
        }
        return answer;
    }
}

/* 해결 전략
  키패드 위치에 따라 값을 1 ~ 12로 설정. 시작위치는 왼쪽 10, 오른쪽 12
  1, 4, 7 입력받을시 answer에 L 더하고 left의 위치 저장
  3, 6, 9 입력받을시 answer애 R 더하고 right의 위치 저장
  숫자 0을 입력받으면 0의 위치인 11로 값을 변경 (나머지는 값이 일치)
  그 이외의 경우에는 왼쪽 손가락에서의 거리, 오른쪽 손가락에서의 거리 계산
  상하로 이동: 이동해야할 위치에서 현재위치를 뺀 값의 절댓값 / 3
  좌우로 이동: 이동해야할 위치에서 현재위치를 뺀 값의 절댓값 % 3
  이 둘을 합하여 총 거리를 계산, 더 가까운 쪽이 이동하게 하고 answer에 값 더하기
  총 거리가 같다면 매개변수로 받은 hand를 통해 해결
*/

//다른사람의 풀이
class Solution {
    //        0부터 9까지 좌표 {y,x}
    int[][] numpadPos = {
            {3,1}, //0
            {0,0}, //1
            {0,1}, //2
            {0,2}, //3
            {1,0}, //4
            {1,1}, //5
            {1,2}, //6
            {2,0}, //7
            {2,1}, //8
            {2,2}  //9
    };
    //초기 위치
    int[] leftPos = {3,0};
    int[] rightPos = {3,2};
    String hand;
    public String solution(int[] numbers, String hand) {
        this.hand = (hand.equals("right")) ? "R" : "L";

        String answer = "";
        for (int num : numbers) {
            String Umji = pushNumber(num);
            answer += Umji;

            if(Umji.equals("L")) {leftPos = numpadPos[num]; continue;}
            if(Umji.equals("R")) {rightPos = numpadPos[num]; continue;}
        }
        return answer;
    }

    //num버튼을 누를 때 어디 손을 사용하는가
    private String pushNumber(int num) {
        if(num==1 || num==4 || num==7) return "L";
        if(num==3 || num==6 || num==9) return "R";

        // 2,5,8,0 일때 어디 손가락이 가까운가
        if(getDist(leftPos, num) > getDist(rightPos, num)) return "R";
        if(getDist(leftPos, num) < getDist(rightPos, num)) return "L";

        //같으면 손잡이
        return this.hand;
    }

    //해당 위치와 번호 위치의 거리
    private int getDist(int[] pos, int num) {
        return Math.abs(pos[0]-numpadPos[num][0]) + Math.abs(pos[1]-numpadPos[num][1]);
    }
}
