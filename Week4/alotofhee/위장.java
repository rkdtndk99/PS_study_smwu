import java.util.HashMap;
class Solution {
    public static int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        for(int i = 0; i < clothes.length; i++){
            String type = clothes[i][1];
            hm.put(type, hm.getOrDefault(type, 1) + 1);
        }
        for (String key : hm.keySet()) {
            answer *= hm.get(key);
        }
        answer -= 1;
        return answer;
    }
}
