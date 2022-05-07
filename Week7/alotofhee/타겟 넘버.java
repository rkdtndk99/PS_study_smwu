class Solution {
  int answer = 0;
  public int solution(int[] numbers, int target) {
    dfs(numbers, numbers.length, target, 0);
    return answer;
  }

  public void dfs(int[] num, int depth, int target, int total) {
    if (depth == 0) {
      if (total == target) {
        answer++;
      }
      return;
    }
    dfs(num, depth - 1, target, total + num[num.length - depth]);
    dfs(num, depth - 1, target, total - num[num.length - depth]);
  }
}
