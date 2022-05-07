import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        String[] answer = {};
        HashMap<String, String> info = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        int count = record.length;
      
        for (int i = 0; i < record.length; i++) {
            String func = record[i].split(" ")[0];
            String id = record[i].split(" ")[1];
            String nickname = "";          
            if (!func.equals("Leave")) {
                nickname = record[i].split(" ")[2];
            }            
            switch(func) {
                case "Enter":
                    sb.append(id).append("님이 들어왔습니다.-");
                    info.put(id, nickname);
                    break;
                case "Leave":
                    sb.append(id).append("님이 나갔습니다.-");
                    break;
                case "Change":
                    info.put(id, nickname);
                    count--;
                    break;
            }
        }
        
        String str = sb.toString();
        answer = new String[count];
        answer = str.split("-");
        for(int i = 0; i < answer.length; i++){
            String key = answer[i].substring(0, answer[i].indexOf("님"));
            answer[i] = answer[i].replace(key, info.get(key));
        }                      
        return answer;
    }
}
