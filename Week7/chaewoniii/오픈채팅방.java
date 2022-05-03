import java.util.*;
class Solution {
    public static String[] solution(String[] record) {
        String[] answer = {};
        String[] idList=new String[record.length];
        String[] result=new String[record.length];
        int size=record.length;
        Map<String,String> map=new HashMap<>();
        Map<String,String> status=new HashMap<>();
        status.put("Enter","님이 들어왔습니다.");
        status.put("Leave","님이 나갔습니다.");
        for(int i=0;i<record.length;i++){
            StringTokenizer st = new StringTokenizer(record[i]," ");
            String stat=st.nextToken();
            String id=st.nextToken();
            String name="";
            if(st.hasMoreTokens()){
                name=st.nextToken();
            }
            if(status.containsKey(stat)){
                idList[i]=id;
                result[i]=status.get(stat);
                if(stat.equals("Enter")){
                    map.put(id,name);
                }

            }else{
                map.replace(id,name);
                result[i]="change";
                size--;
            }

        }
        answer=new String[size];
        int k=0;
        for(int i=0;i<record.length;i++){
            if(result[i].equals("change")){
                continue;
            }
            answer[k]=map.get(idList[i])+result[i];
            k++;
        }

        return answer;
    }
}
