class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> newMap = new HashMap<>();

        for (String s: strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String news = new String(chars);
            newMap.putIfAbsent(news, new ArrayList<>());
            newMap.get(news).add(s);
        }
        return new ArrayList<>(newMap.values());
    }
}
