class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> m=new HashMap<>();
        int i=0;
        for(int n:nums){
            int r=target-n;
            if(m.containsKey(r)){
                return new int[]{m.get(r),i};
            }
            m.put(n,i);
            i+=1;
        }
        return new int[]{};
    }
}