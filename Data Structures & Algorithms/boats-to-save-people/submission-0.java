class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);

        int n = people.length;

        int i = 0;
        int j = n-1;
        int res = 0;
        while ( i <=  j){
            int rem = limit - people[j--];
            res++;
            if( i <= j && rem >= people[i]){
                i++;
            }
        }
        return res;
    }
}
