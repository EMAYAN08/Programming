public class Problem_22_trap {
      public int trap(int[] height) {
          if (height == null || height.length == 0) {
              return 0;
          }
          
          int left = 0, right = height.length - 1;
          int leftMax = 0, rightMax = 0;
          int result = 0;
          
          while (left < right) {
              if (height[left] < height[right]) {
                  if (height[left] >= leftMax) {
                      leftMax = height[left];
                  } else {
                      result += leftMax - height[left];
                  }
                  left++;
              } else {
                  if (height[right] >= rightMax) {
                      rightMax = height[right];
                  } else {
                      result += rightMax - height[right];
                  }
                  right--;
              }
          }
          
          return result;
      }
  }
  