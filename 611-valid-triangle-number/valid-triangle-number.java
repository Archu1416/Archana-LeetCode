class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int c=0;
        int n=nums.length;
        for(int k=n-1;k>1;k--){
            int i=0;
            int j=k-1;
            while(i<j){
                if(nums[i]+nums[j]>nums[k]){
                    c+=(j-i);
                    j-=1;
                }
                else{
                    i+=1;
                }
            }
        }
        return c;
    }
}