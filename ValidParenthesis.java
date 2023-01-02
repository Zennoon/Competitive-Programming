class Solution {
    public boolean isValid(String s) {
        char[] openP = {'[', '(', '{'};
            char[] closeP = {']', ')', '}'};
            List<Character> opening = new ArrayList<>();
            List<Character> closing = new ArrayList<>();
            for (char chr : openP) {
                opening.add(chr);

            }
            for (char chr : closeP) {
                closing.add(chr);
            }
            List<Character> collector = new ArrayList<>();
            for (char chr : s.toCharArray()) {
                if (opening.contains(chr)) {
                    collector.add(chr);
                }
                else {
                    if (collector.isEmpty()){
                        return false;
                    }
                    int index_of_last = opening.indexOf(collector.get(collector.size() - 1));
                    if (closing.indexOf(chr) != index_of_last) {
                        return false;
                    }
                    else {
                        collector.remove(collector.size() - 1);
                    }
                }
            }
            return collector.isEmpty();
        
    }
}
