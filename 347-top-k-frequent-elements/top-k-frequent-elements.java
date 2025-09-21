class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> m=new HashMap<>();
        for(int num: nums){
            m.put(num,m.getOrDefault(num,0)+1);
        }
        List<Map.Entry<Integer,Integer>> sorted=new ArrayList<>(m.entrySet());
        sorted.sort((a,b)->b.getValue()-a.getValue());
        List<Integer> keys=new ArrayList<Integer>();
        for(Map.Entry<Integer,Integer> entry: sorted){
            keys.add(entry.getKey());
        }
        int[] res=new int[k];
        for(int j=0;j<k;j++){
            res[j]=keys.get(j);
        }
        return res;
    }
}