import java.lang.Math;
class Solution {
    public int reverse(int x) {
        int reve=0,rem;
        while(x!=0){
        rem=x%10;
        if(reve>Integer.MAX_VALUE/10||reve<Integer.MIN_VALUE/10){
            return 0;
        }
        reve=(reve*10)+rem;
        x=x/10;
        }    
            return reve;
    }
}