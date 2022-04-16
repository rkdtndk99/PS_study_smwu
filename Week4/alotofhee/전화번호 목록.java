import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> hm = new HashMap<>();
        for (String phone_num : phone_book) {
            hm.put(phone_num, 1);
        }
        for (String phone_num : phone_book) {
            for (int i = 0; i < phone_num.length(); i++) {
                String prefix = phone_num.substring(0, i);
                if (hm.containsKey(prefix)) {
                    return false;
                }
            }
        }
        return answer;
    }
}
