class Solution {
    public String sortSentence(String s) {
        String[] sortedList = s.split(" ");
            List<String> sorted = new ArrayList<>();
            for (int i = 1; i < sortedList.length + 1; i++){
                for (String word : sortedList){
                    String index = "" + i;
                    if (word.contains(index)){
                        sorted.add(word.replaceAll(index, " "));
                    }
                }
            }
            String result = "";
            for (String word : sorted){
                result += word;
            }
            return result.trim();
        
    }
}
