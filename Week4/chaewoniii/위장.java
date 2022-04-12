import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
            Map<String, Integer> map=new HashMap<>();
            for(int i=0; i<clothes.length;i++) {
                if (map.containsKey(clothes[i][1])) {
                    int n = map.get(clothes[i][1]);
                    map.put(clothes[i][1], n+1);
                    continue;
                }
                map.put(clothes[i][1],1);
            }
            for(Map.Entry<String, Integer> e : map.entrySet()){
                int n=e.getValue();
                answer=answer*(n+1);
            }
            answer=answer-1;
        return answer;
    }
}
