class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        char[] sort = s.toCharArray();
        char[] sort1 = t.toCharArray();
        Arrays.sort(sort);
        Arrays.sort(sort1);

        return Arrays.equals(sort, sort1);
    }
}
