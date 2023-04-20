/*A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column 
represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal. */

public class Problem_12_HouseColoring {
    public static int minCost(int[][] costs) {
        int n = costs.length;
        int k = costs[0].length;

        // Initialize dp array with first row of costs
        int[] dp = new int[k];
        for (int i = 0; i < k; i++) {
            dp[i] = costs[0][i];
        }

        // Iterate over remaining rows of costs
        for (int i = 1; i < n; i++) {
            // Initialize temporary dp array for this row
            int[] temp = new int[k];

            // Compute minimum cost for each color for this row
            for (int j = 0; j < k; j++) {
                temp[j] = Integer.MAX_VALUE;
                for (int l = 0; l < k; l++) {
                    if (l != j) {
                        temp[j] = Math.min(temp[j], dp[l] + costs[i][j]);
                    }
                }
            }

            // Update dp array with minimum cost for this row
            for (int j = 0; j < k; j++) {
                dp[j] = temp[j];
            }
        }

        // Find minimum cost among all possible final colors
        int minCost = Integer.MAX_VALUE;
        for (int i = 0; i < k; i++) {
            minCost = Math.min(minCost, dp[i]);
        }

        return minCost;
    }

    public static void main(String[] args) {
        int[][] costs = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
        int minCost = minCost(costs);
        System.out.println("Minimum cost: " + minCost);
    }
}
