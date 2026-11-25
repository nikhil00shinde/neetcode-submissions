class Solution {

    public String encode(List<String> strs) {
       StringBuilder s = new StringBuilder();
       for (String t : strs){
            s.append(t.length()).append('#').append(t);
       }
       return s.toString();
    }


    public List<String> decode(String str) {
     
     List<String> ans = new ArrayList<>();
     int i = 0;

     while( i < str.length()){
         int j = i;
         while( str.charAt(j) != '#' ){
            j++;
         }

         String sl = str.substring(i,j);
         int length = Integer.valueOf(sl);
         
         i = j + 1;
         j = i + length;
         String os = str.substring(i,j);
         ans.add(os);
         i = j;

     }
     return ans;
      
    }
}
