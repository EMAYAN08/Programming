/*
 * Suppose you are given a table of currency exchange rates, represented as a 2D array. 
 * Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, 
 * so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.
 */
public class Problem_24_currencyExchange {
    
      // Method to check if there is a possible arbitrage
      public static boolean hasArbitrage(double[][] exchangeRates) {
          int n = exchangeRates.length;
          double[] distances = new double[n];
          
          // Initialize the distances to infinity
          Arrays.fill(distances, Double.POSITIVE_INFINITY);
          distances[0] = 0;
          
          // Apply the Bellman-Ford algorithm
          for (int i = 0; i < n - 1; i++) {
              for (int j = 0; j < n; j++) {
                  for (int k = 0; k < n; k++) {
                      if (distances[k] > distances[j] + Math.log(exchangeRates[j][k])) {
                          distances[k] = distances[j] + Math.log(exchangeRates[j][k]);
                      }
                  }
              }
          }
          
          // Check for negative cycles
          for (int j = 0; j < n; j++) {
              for (int k = 0; k < n; k++) {
                  if (distances[k] > distances[j] + Math.log(exchangeRates[j][k])) {
                      return true;
                  }
              }
          }
          
          return false;
      }
      
      // Main method to test the implementation
      public static void main(String[] args) {
          double[][] exchangeRates = {
                  {1.0, 0.23, 0.25, 16.43},
                  {4.34, 1.0, 1.11, 71.40},
                  {3.93, 0.90, 1.0, 64.52},
                  {0.061, 0.014, 0.015, 1.0}
          };
          
          if (hasArbitrage(exchangeRates)) {
              System.out.println("Arbitrage is possible");
          } else {
              System.out.println("Arbitrage is not possible");
          }
      }
  }
  