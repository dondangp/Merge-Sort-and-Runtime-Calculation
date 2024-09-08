import time
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

n_values = list(range(1, 1001))
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(n_values, times, label='Time vs n')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Function f(n)')
plt.show()

