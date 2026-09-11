class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int n = heights.length;
        int[] nge = new int[n];
        Stack<Integer> st = new Stack<>();
        for(int i = n - 1; i >= 0; i--){
            int cnt = 0;
            if(st.size() == 0){
                nge[i] = cnt;
            }else{
                cnt = 1;
                while(!st.isEmpty() && heights[i] >= st.peek()){
                    st.pop();
                    cnt++;
                }
                if(st.size() == 0) nge[i] = cnt-1;
                else nge[i] = cnt;
            }
            st.push(heights[i]);
            
        }
        return nge;

    }
}