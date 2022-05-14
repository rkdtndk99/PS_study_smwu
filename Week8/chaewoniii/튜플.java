import java.util.*;
class Solution {
    public static int[] solution(String s) {
        int[] answer = {};
        StringBuilder sb=new StringBuilder();
        Map<Integer,Integer> map=new HashMap<>();
        for(int i=1;i<s.length();i++){
            char c=s.charAt(i);
            if(c=='{'){
                continue;
            }
            if(c=='}'){
                char tmp=s.charAt(i-1);
                if(tmp>='0'&&tmp<='9'){
                    String str=sb.toString();
                    int x=Integer.parseInt(str);
                    if(map.containsKey(x)){
                        map.replace(x,map.get(x)+1);
                        sb.setLength(0);
                        continue;
                    }
                    map.put(x,1);
                    sb.setLength(0);
                }
                
                continue;
            }
            if(c==','){
                if(s.charAt(i-1)!='}'){
                    String str=sb.toString();
                    int x=Integer.parseInt(str);
                    if(map.containsKey(x)){
                        map.replace(x,map.get(x)+1);
                        sb.setLength(0);
                        continue;
                    }
                    map.put(x,1);
                    sb.setLength(0);
                }
                continue;
            }
            if(c>='0'&&c<='9'){
                sb.append(c);
                continue;
            }
        }
        answer=new int[map.size()];
        //map 값으로 내림차순 정렬
        List<Integer> keySetList = new ArrayList<>(map.keySet());
        Collections.sort(keySetList, (o1, o2) -> (map.get(o2).compareTo(map.get(o1))));
        int idx=0;
        for(Integer key : keySetList){
            answer[idx++]=key;
        }
        return answer;
    }
}
