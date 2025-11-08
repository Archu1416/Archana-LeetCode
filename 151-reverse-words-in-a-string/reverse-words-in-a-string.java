class Solution {
    public String reverseWords(String s) {
        s=s.trim();
        String a[]=s.split("\\s+");
        StringBuilder res=new StringBuilder();
        for(int i=a.length-1;i>=0;i--){
            res.append(a[i]);
            if(i>0){
                res.append(" ");
            }
        }
        return res.toString();
    }
}