class Solution {
    public String reversePrefix(String word, char ch) {
        String res="";
        int ind=word.indexOf(ch);
        if(ind==-1){
            return word;
        }
        Stack<Character> st=new Stack<>();
        for(int i=0;i<=ind;i++){
            st.push(word.charAt(i));
        }
        while(!st.isEmpty()){
            res+=st.pop();
        }
        for(int j=ind+1;j<word.length();j++){
            res+=word.charAt(j);
        }
        return res;
    }
}