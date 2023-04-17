/*Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability. */

import java.util.*;

public class Problem_8_randomElement {

    private static int randomElement(int[] stream, int size) {
        int result = 0;
        Random rand = new Random();

        for (int i = 0; i < size; i++) {
            // Generate a random index between 0 and i (inclusive)
            int j = rand.nextInt(i+1);

            // If the random index is i, set the result to the current element
            if (j == i) {
                result = stream[i];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] stream = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int size = stream.length;

        System.out.println("Random element from stream: " + randomElement(stream, size));
    }
}
