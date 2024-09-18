import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
      int i=0,j=0,length=0;
      ArrayList<Character> list=new ArrayList<>();
      while(j<s.length()){
        if(!list.contains(s.charAt(j))){
            list.add(s.charAt(j));
            j++;
            length=Math.max(length,list.size());
        }
        else{
            list.remove(Character.valueOf(s.charAt(i)));
            i++;
        }
      }
      return length;
    }
}