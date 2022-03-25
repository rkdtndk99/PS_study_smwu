class Solution {
    public int solution(String s) {
        int answer = 0;
        String numArray[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < numArray.length; i++) {
            s = s.replace(numArray[i], Integer.toString(i));
        }
        answer = Integer.parseInt(s);
        return answer;
    }
}
