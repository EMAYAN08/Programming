/*You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible. */

public class Problem_9_orderLog {
      private int size;
      private int nextIndex;
      private int count;
      private int[] buffer;
  
      public Problem_9_orderLog(int size) {
          this.size = size;
          this.nextIndex = 0;
          this.count = 0;
          this.buffer = new int[size];
      }
  
      public void record(int orderId) {
          buffer[nextIndex] = orderId;
          nextIndex = (nextIndex + 1) % size;
          count = Math.min(count + 1, size);
      }
  
      public int getLast(int i) {
          if (i >= count) {
              return -1; // or throw an exception
          }
          int index = (nextIndex - 1 - i + size) % size;
          return buffer[index];
      }
  }
  