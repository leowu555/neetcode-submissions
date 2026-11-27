class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) {
            return new ArrayList<>();
        }
        Map<String, List<String>> newMap = new HashMap<>();
        
        for (String s: strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String key = String.valueOf(charArray);

            if (!newMap.containsKey(key)) {
                newMap.put(key, new ArrayList<>());
            }

            newMap.get(key).add(s);
        }

        return new ArrayList<>(newMap.values());
    }
}

