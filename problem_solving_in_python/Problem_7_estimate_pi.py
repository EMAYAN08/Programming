"""The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2."""

import random

def estimate_pi(num_points):
    points_inside_circle = 0
    points_total = num_points

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / points_total
    return pi_estimate

print(f"Estimated value of π: {estimate_pi(1000000):.3f}")
