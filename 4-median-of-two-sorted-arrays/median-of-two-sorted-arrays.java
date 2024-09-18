class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n=nums1.length+nums2.length;
        int arr[]=new int[n];
        for(int i=0;i<nums1.length;i++){
            arr[i]=nums1[i];
        }
        int j=0;
        for(int i=nums1.length;i<n;i++){
            arr[i]=nums2[j];
            j++;
        }
        for(int i=0;i<n;i++){
            for(int k=i+1;k<n;k++){
                if(arr[i]>arr[k]){
                    int temp=arr[i];
                    arr[i]=arr[k];
                    arr[k]=temp;
                }
            }
        }
        int val=n/2;
        double res;
        if(n%2==0){
            res=(arr[val-1]+arr[val])/2.0;
            return res;
        }
        else{
            res=arr[val];
            return res;
        }
    }
}