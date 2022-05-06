class Solution {
    public int answer;
    public int solution(int[] numbers, int target) {
        answer=0;
        dfs(numbers,target,0,0);
        return answer;
    }
    public void dfs(int[] numbers, int target, int index, int sum){
        //끝까지 탐색한 경우
        if(index==numbers.length){
            if(sum==target){
                answer++;
                return;
            }
            return;
        }
        dfs(numbers,target,index+1,sum+numbers[index]);
        dfs(numbers,target,index+1,sum-numbers[index]); 
    }
}
