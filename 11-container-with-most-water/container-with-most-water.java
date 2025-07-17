class Solution {
    public int maxArea(int[] height) {
        int n=height.length;
        int i=0;
        int j=n-1;
        int max_val=0;
        int cur_val;
        while(i!=j){
            cur_val=Math.min(height[i],height[j])*(j-i);
            if(cur_val>max_val){
                max_val=cur_val;
            }
            if(height[i]<height[j]){
                i+=1;
            }
            else{
                j-=1;
            }
        }
        return max_val;
    }
}