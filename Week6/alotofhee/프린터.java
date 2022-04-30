import java.util.*;

class Solution {
	public int solution(int[] priorities, int location) {
		int answer = 0;
		Queue<Integer> queue = new LinkedList<>(); //큐 생성

		for (int pri : priorities) { //큐에 priorities 추가
			queue.add(pri);
		}
    
		Arrays.sort(priorities); //우선순위 오름차순으로 정렬
		int priLength = priorities.length - 1; //우선순위가 가장 높은 원소의 인덱스 (해당 원소 처리하면 -1 하여 다음 우선순위에 접근)

    while (!queue.isEmpty()) { //큐가 빈큐가 아닐때까지
			int current = queue.poll(); //큐의 맨 앞에 있는 요소를 반환 (후 제거)
			if (current == priorities[priLength]) { //우선순위가 가장 높은 원소가 맞을 경우
				priLength--; //다음 우선순위의 인덱스
				answer++; //인쇄된 문서 1 증가
				location--; //요청한 문서의 우선순위가 높아짐 (가까워짐)
				if (location < 0) { //location이 current이었던 것. 즉 내가 요청한 문서가 인쇄됨.
					break;
				}
			} 
      else { //우선순위가 가장 높은 원소가 아닐 경우
				queue.add(current); //제거했던 해당 요소를 큐 맨 뒤에 다시 삽입.
				location--; //요청한 문서의 우선순위가 높아짐 (가까워짐)
				if (location < 0) { // location이 current였지만 우선순위가 가장높지 않았기 때문에 우선순위가 밀려 맨뒷순서가 됨.
					location = queue.size() - 1;
				}
			}
		}
		return answer;
	}
}
