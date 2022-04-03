import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String,Integer> map=new HashMap<>();
        for(String name : completion){
            if(map.containsKey(name)){
                int num=map.get(name);
                map.replace(name,num+1);
                continue;
            }
            map.put(name,1);
        }
        for(String name : participant){
            if(map.containsKey(name)) {
                if(map.get(name)>0){
                    int num=map.get(name);
                    map.replace(name,num-1);
                    continue;
                }
            }
            answer=name;
            break;
        }
        return answer;
    }
}
