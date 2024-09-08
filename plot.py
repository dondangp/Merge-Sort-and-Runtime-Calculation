import time
import matplotlib.pyplot as plt

# Function f(n) from the problem statement
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x

# List of n values
n_values = [1, 10, 50, 100, 500, 1000, 2000]

# List to store time taken for each n
times = []

# Loop through each n and time the function
for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    times.append(elapsed_time)
    
    print(f"Time taken for n={n}: {elapsed_time:.6f} seconds")

# Plotting the results
plt.plot(n_values, times, marker='o')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of f(n)')
plt.grid(True)
plt.show()
