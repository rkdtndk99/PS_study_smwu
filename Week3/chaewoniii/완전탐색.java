class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] temp=new int[3];
        int[][] math={{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};
        for(int i=0;i<answers.length;i++){
            if(answers[i]==math[0][i%(math[0].length)]){
                temp[0]++;
            }
            if(answers[i]==math[1][i%(math[1].length)]){
                temp[1]++;
            }
            if(answers[i]==math[2][i%(math[2].length)]){
                temp[2]++;
            }
        }
        int max=0;
        int count=0;
        for(int i=0;i<3;i++){
            if(max<temp[i]){
                max=temp[i];
            }
        }
        for(int i=0;i<3;i++){
            if(max==temp[i]){
                count++;
            }
        }
        int k=0;
        answer=new int[count];
        for(int i=0;i<3;i++){
            if(max==temp[i]){
                answer[k++]=i+1;
            }
        }
        return answer;
    }
}
