class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
     int merged[]=new int[nums1.length+nums2.length];
     for(int i=0;i<nums1.length;i++){
        merged[i]=nums1[i];
     }
     for(int i=0;i<nums2.length;i++){
        merged[(nums1.length)+i]=nums2[i];
     }
     Arrays.sort(merged);
     int m=merged.length/2;   
     if(merged.length==1){
        return merged[0];
     }
     if(merged.length%2==0){
        return (merged[m-1]+merged[m])/2.0;
     }
     else{
        return merged[m];
     }
    }
}