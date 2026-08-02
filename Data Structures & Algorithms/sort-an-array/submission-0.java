class Solution {
    public int[] sortArray(int[] nums) {
        return mergeSort(nums,0,nums.length-1);
    }
    private int[] mergeSort(int[] nums, int i,int j){
        if(i == j){
            // System.out.println(i+" "+j);
            return new int[]{nums[i]};
        }

        int mid = i + (j-i)/2;
        int[] a1 = mergeSort(nums,i,mid);
        int[] a2 = mergeSort(nums,mid+1,j);
        int n = (j-i+1);
        // System.out.println(n);
        int[] ans = new int[n]; 
        
        int st1 = 0,st2 = 0;
        int ni = 0;


        while(st1 < a1.length && st2 < a2.length){
            if(a1[st1] >= a2[st2]){
                ans[ni++] = a2[st2++];
            }else{
                ans[ni++] = a1[st1++];
            }
        }

        while(st1 < a1.length){
            ans[ni++] = a1[st1++];
        }

        while(st2 < a2.length){
            ans[ni++] = a2[st2++];
        }
        return ans;
    }
}