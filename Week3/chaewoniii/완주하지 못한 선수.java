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
          //어차피 완주하지 못한 선수는 한명이므로 찾으면 break해줘도 됨 그러면 성능이 훨씬 좋아짐..!
            break;
        }
        return answer;
    }
}
