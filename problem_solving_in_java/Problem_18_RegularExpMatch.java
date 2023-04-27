/* 
 * Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
*/

public class Problem_18_RegularExpMatch {
    
      public static boolean isMatch(String text, String pattern) {
          if (pattern.isEmpty()) return text.isEmpty();
          
          boolean first_match = (!text.isEmpty() &&
                                 (pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.'));
          
          if (pattern.length() >= 2 && pattern.charAt(1) == '*'){
              return (isMatch(text, pattern.substring(2)) ||
                      (first_match && isMatch(text.substring(1), pattern)));
          } else {
              return first_match && isMatch(text.substring(1), pattern.substring(1));
          }
      }
      
      public static void main(String[] args) {
          String text = "ray";
          String pattern = "ra.";
          System.out.println(isMatch(text, pattern)); // true
          
          text = "raymond";
          System.out.println(isMatch(text, pattern)); // false
          
          text = "chat";
          pattern = ".*at";
          System.out.println(isMatch(text, pattern)); // true
          
          text = "chats";
          System.out.println(isMatch(text, pattern)); // false
      }
  }
  