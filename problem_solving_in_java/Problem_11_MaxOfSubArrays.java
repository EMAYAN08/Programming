import java.util.Deque;
import java.util.LinkedList;
import java.util.Arrays;

public class Problem_11_MaxOfSubArrays 
{
    
    public static void printMaxOfSubarrays(int[] arr, int k) 
    {
        if (arr == null || arr.length == 0 || k <= 0 || k > arr.length) 
        {
            return;
        }
        Deque<Integer> deque = new LinkedList<>(); // store indices of maximum elements
        for (int i = 0; i < arr.length; i++) 
        {
            while (!deque.isEmpty() && deque.peekFirst() <= i - k) 
            {
                deque.removeFirst(); // remove indices outside the window
            }
            while (!deque.isEmpty() && arr[i] >= arr[deque.peekLast()]) 
            {
                deque.removeLast(); // remove smaller elements from the back
            }
            deque.addLast(i); // add current index to deque
            if (i >= k - 1) 
            { // print the maximum for each window
                System.out.print(arr[deque.peekFirst()] + " ");
            }
        }
    }
    
    public static void main(String[] args) 
    {
        int[] arr = {10, 5, 2, 7, 8, 7};
        int k = 3;
        System.out.print("Maximum of subarrays of length " + k + " in array " + Arrays.toString(arr) + ": ");
        printMaxOfSubarrays(arr, k);
    }
}
