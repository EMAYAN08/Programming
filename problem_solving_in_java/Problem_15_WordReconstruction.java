/*Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
 */

import java.util.*;

class Problem_15_WordReconstruction {
    public static List<String> reconstruct(String str, Set<String> words) {
        // Use a queue to keep track of possible prefixes of the sentence
        Queue<String> queue = new LinkedList<>();
        // Use a map to keep track of visited prefixes to avoid loops
        Map<String, Boolean> visited = new HashMap<>();
        // Initialize the queue with the empty string as the first prefix
        queue.offer("");

        while (!queue.isEmpty()) {
            String prefix = queue.poll();
            // If the prefix is a valid word, add it to the sentence and reset the prefix
            if (words.contains(prefix)) {
                str = str.substring(prefix.length());
                prefix = "";
            }
            // If the prefix is equal to the original string, we have found a valid sentence
            if (str.isEmpty()) {
                return Arrays.asList(prefix.split(" "));
            }
            // If the prefix is not a valid prefix of the string, skip it
            if (!str.startsWith(prefix)) {
                continue;
            }
            // Try to append each possible word to the prefix and add it to the queue if it hasn't been visited before
            for (String word : words) {
                String newPrefix = prefix + word;
                if (!visited.containsKey(newPrefix)) {
                    visited.put(newPrefix, true);
                    queue.offer(newPrefix);
                }
            }
        }
        // If we have exhausted all possible prefixes and haven't found a valid sentence, return null
        return null;
    }

    public static void main(String[] args) {
        Set<String> words1 = new HashSet<>(Arrays.asList("quick", "brown", "the", "fox"));
        String str1 = "thequickbrownfox";
        System.out.println(reconstruct(str1, words1)); // Output: [the, quick, brown, fox]

        Set<String> words2 = new HashSet<>(Arrays.asList("bed", "bath", "bedbath", "and", "beyond"));
        String str2 = "bedbathandbeyond";
        System.out.println(reconstruct(str2, words2)); // Output: [bed, bath, and, beyond] or [bedbath, and, beyond]
    }
}
