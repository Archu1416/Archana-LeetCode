class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer,Integer> m=new HashMap<>();
        for(int n:nums){
            m.put(n,m.getOrDefault(n,0)+1);
        }
        int max=0;
        for(int v:m.values()){
            if(v>max){
                max=v;
            }
        }
        int c=0;
        for(int val: m.values()){
            if(val==max){
                c+=1;
            }
        }
        return c*max;
    }
}