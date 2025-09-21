class Solution {
    public String clearDigits(String s) {
        Stack<Character> st=new Stack<>();
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(Character.isDigit(c)){
                if(!st.isEmpty()){
                    st.pop();
                }
            }
            else{
                st.push(s.charAt(i));
            }
        }
        String res="";
        for(char ch:st){
            res+=ch;
        }
        return res;
    }
}