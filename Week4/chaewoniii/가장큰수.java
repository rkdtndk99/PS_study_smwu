import java.util.Arrays;
class Solution {
    static int convert(String a, String b) {
		int c = Integer.parseInt(a+b);
		return c;
	}
    public String solution(int[] numbers) {
        String answer = "";
        String[] str=new String[numbers.length];
        for(int i=0;i<numbers.length;i++){
            str[i]=Integer.toString(numbers[i]);
        }
	        for (int i = 0; i < numbers.length-1; i++) {
	        	boolean k = true;
				for (int j = 1; j < numbers.length; j++) {
					
					if(convert(str[j],str[j-1])>convert(str[j-1],str[j])) {
						String temp = str[j];
						str[j] = str[j-1];
						str[j-1] = temp;
						k = false;
					}
				}
				if(k) {
					break;
				}
			}
	        
	       if(numbers[0]==0){
                    return "0";
                }
				answer =String.join("",str);
			
	       
	        return answer;
    }
}
