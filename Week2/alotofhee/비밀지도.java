class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            answer[i] = Integer.toBinaryString(arr1[i] | arr2[i]); //2진수변환 후 OR연산 수행
            answer[i] = answer[i].replace('0', ' ');
            answer[i] = answer[i].replace('1', '#');
            while (answer[i].length() < n) { //공백 길이n까지 채우기 
                answer[i] = ' ' + answer[i];
            }
        }
        return answer;
    }
}
