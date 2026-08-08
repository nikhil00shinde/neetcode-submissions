class Solution {
    public int[] sortArray(int[] nums) {
        if(nums.length <= 1) return nums;
        quickSort(nums,0,nums.length-1);
        return nums;
    }

    private void quickSort(int[] nums, int st, int ed){
        if(st < ed){
            int pi = partitions(nums,st,ed);
            quickSort(nums,st,pi-1);
            quickSort(nums,pi+1,ed);
        }
    }

    private int partitions(int[] nums,int st,int ed){

        int pivot = nums[st];
        int i = ed;
        for(int j = ed; j > st; j--){
            if(nums[j] > pivot){
                swap(nums,i,j);
                i--;
            }
        }

        swap(nums,st,i);
        return i;
    }

    private void swap(int[] nums,int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
}