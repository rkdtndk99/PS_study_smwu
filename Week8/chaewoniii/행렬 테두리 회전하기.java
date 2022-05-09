class Solution {
    public static int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        //판
        int[][] rot=new int[rows][columns];
        int k=1;
        for(int i=0;i<rows;i++){
            for(int j=0;j<columns;j++){
                rot[i][j]=k++;
            }
            
        }
        //영역 이차원배열 [행][열]
        for(int i=0;i<queries.length;i++){
            int[] cor=new int[4];
            for(int j=0;j<4;j++){
                cor[j]=queries[i][j];
            }
            //회전
            int r1=cor[0]-1; //행
            int c1=cor[1]-1; //열
            int r2=cor[2]-1;
            int c2=cor[3]-1;

            int tmp=rot[r1][c1];
            int min=tmp;
            for(int r=r1;r<r2;r++){
                if(min>rot[r+1][c1]){
                    min=rot[r+1][c1];
                }
                rot[r][c1]=rot[r+1][c1];
            }
            for(int c=c1;c<c2;c++){
                if(min>rot[r2][c+1]){
                    min=rot[r2][c+1];
                }
                rot[r2][c]=rot[r2][c+1];
            }
            for(int r=r2;r>r1;r--){
                if(min>rot[r-1][c2]){
                    min=rot[r-1][c2];
                }
                rot[r][c2]=rot[r-1][c2];
            }

            for(int c=c2;c>c1;c--){
                if(min>rot[r1][c-1]){
                    min=rot[r1][c-1];
                }
                rot[r1][c]=rot[r1][c-1];
            }

            rot[r1][c1+1]=tmp;
            answer[i]=min;

        }

        return answer;
    }
}
