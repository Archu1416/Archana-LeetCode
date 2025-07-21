class Solution {
    public String makeFancyString(String s) {
        int c=1;
        StringBuilder res=new StringBuilder();
        res.append(s.charAt(0));
        for(int i=1;i<s.length();i++){
            if(s.charAt(i)==s.charAt(i-1)){
                c+=1;
            }
            else{
                c=1;
            }
            if(c<3){
                res.append(s.charAt(i));
            }
        }
        return res.toString();
    }
}