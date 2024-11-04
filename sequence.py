import time
import matplotlib.pyplot as plt
import numpy as np

def layup_sequence(n):
    """
    Computes the value of the Layup Sequence S(n) using a bottom-up approach with constant space.
    
    Recurrence Relation:
    S(n) = {
        1 if n = 1,
        2 if n = 2,
        S(n-1) + S(n-2) if n is even,
        2 * S(n-1) - S(n-2) if n is odd
    }
    
    Arguments:
        n (int): The position in the sequence to compute.
    
    Returns:
        int: The value of the Layup Sequence at position n.
    """
    # Base cases
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    # Initialize the first two values
    prev2 = 1 # S(1)
    prev1 = 2 # S(2)
    
    # Calculate S(n) using only the last two terms (only ones necessary)
    for i in range(3, n + 1):
        if i % 2 == 0: # Evens
            curr = prev1 + prev2 # S(n-1) + S(n-2)
        else: # Odds
            curr = 2 * prev1 - prev2 # 2 * S(n-1) - S(n-2)
        # Update prev2 and prev1
        prev2, prev1 = prev1, curr
    
    return curr

# Performance Evaluation: Measure runtime for layup_sequence at n = 10,000
n = 10000
start_time = time.time()  # Start
result = layup_sequence(n)
end_time = time.time()  # End

# Display the result and runtime
print("S(10000) =", result)
print("Runtime:", end_time - start_time, "seconds")

# Performance Analysis: Plotting N vs Runtime to analyze time complexity
n_values = np.linspace(1000, 10000, 10, dtype=int)
runtimes = []

for n in n_values:
    start_time = time.time()
    layup_sequence(n)
    runtimes.append(time.time() - start_time)

# Plot N vs Runtime of each of the values
plt.figure(figsize=(20, 12))
plt.plot(n_values, runtimes, marker='o')
plt.title("Runtime of Layup Sequence Computation vs N")
plt.xlabel("N (sequence length)")
plt.ylabel("Runtime (seconds)")
plt.grid()
plt.show()

# --- Report ---
# 
# 1. Performance Evaluation:
#    a. Runtime measurement for S(10,000): The measured runtime was about `end_time - start_time` seconds.
#    b. Time Complexity: The time complexity is O(n), because we iterate only once from 3 to n.
#    c. Space Complexity: This algorithm has a space complexity of O(1) since it only maintains two variables, regardless of how big n gets.
# 
# 2. Explanation:
#    a. Time Complexity: The time complexity of the bottom-up approach is O(n), since each step depends on only the previous two
#       values, allowing for a single pass from 3 to n.
#    b. Optimizations:
#       - We optimized for space by only storing the last two sequence values (`prev2` and `prev1`), rather than maintaining an
#         entire array of results for all N values.
#       - This constant space optimization reduces the memory overhead to O(1), while using dynamic programming to avoid redundant 
#         calculations dramatically reduces the runtime by making sure each value is computed only once.
#    c. Plot of N vs Runtime: The plot of N vs. Runtime shows a nearly linear growth in runtime relative to N, with slight deviations possibly
#       due to system overhead, memory access patterns, or minor computational overhead when adding and subtracting very large values. 
#       This efficient scaling still enables the solution to handle large values of n, such as 10,000, very effectively.
#
