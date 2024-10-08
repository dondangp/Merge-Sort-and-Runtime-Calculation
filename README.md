# Time Complexity and Algorithm Analysis

## 1. Find the Runtime of the Algorithm Mathematically with Summations
The function provided is:
```python
function x = f(n)
  x = 1;
  for i = 1:n
    for j = 1:n
      x = x + 1;
```
![Capture](https://github.com/user-attachments/assets/1fc8bcc2-534a-4228-9897-20faceb9c0e9)
![1b](https://github.com/user-attachments/assets/28ea128b-d0cf-4ac9-9b6d-5d5a60a2d6f9)
![1c](https://github.com/user-attachments/assets/ed0a2583-e591-48a7-9ea4-14a789ab844d)


## 2. Plot "Time vs n"
### Benchmark Environment

- **Operating System**: macOS 14.4.1 (23E224)
- **Processor/Chip**: Apple M2 (8-core CPU)
- **Clock Speed**: Up to 3.49 GHz
- **RAM**: 8 GB
- **Storage**: 245.11 GB Macintosh HD
- **Python Version**: 3.12.0
- **Virtual Environment**: Yes (`venv`)
- **Major Dependencies**: `timeit`, `matplotlib`
- **Device Power Status**: Plugged in
- **Background Processes**: Minimal activity, no significant CPU load during benchmarking.
![Figure_1](https://github.com/user-attachments/assets/8018ebeb-8aef-4043-afae-44f232086a05)

## 3. Big O, Big Omega, Big Theta

### Big-O (Upper Bound)

**Big-O** notation represents the **upper bound** of the algorithm's growth rate. It provides an estimate of the worst-case scenario for how the runtime will grow as the input size increases.

In this problem, both loops run from `1` to `n`, which means that the function executes \(n^2\) iterations in the worst-case scenario.

Thus, the **upper bound** of the function is:

\[
T(n) = O(n^2)
\]

This means the function's runtime will never grow faster than \(n^2\), and **Big-O** gives the worst-case time complexity.

---

### Big-Omega (Lower Bound)

**Big-Omega (Ω)** represents the **lower bound** of the algorithm's growth rate, describing the best-case scenario for the runtime.

Since the two loops always execute exactly \(n^2\) iterations, even in the best-case scenario, the time complexity is still quadratic.

Thus, the **lower bound** of the function is:

\[
T(n) = Ω(n^2)
\]

This means the function will always take at least \(n^2\) steps to complete, regardless of the specific input.

---

### Big-Theta (Tight Bound)

**Big-Theta (Θ)** notation describes the **tight bound** for the algorithm's runtime. It represents a scenario where the upper and lower bounds are the same, giving an exact growth rate of the function.

Since both the upper and lower bounds are quadratic, we can say that the time complexity of this function is exactly \(n^2\).

Thus, the **tight bound** of the function is:

\[
T(n) = Θ(n^2)
\]

This means that the function's runtime will grow exactly proportional to \(n^2\) as the input size increases, regardless of the scenario.

---

### Result
- **Big-O (Upper Bound)**: \(O(n^2)\)
- **Big-Omega (Lower Bound)**: \(Ω(n^2)\)
- **Big-Theta (Tight Bound)**: \(Θ(n^2)\)
### Plot
![Figure_2](https://github.com/user-attachments/assets/c316624d-c629-48f6-818d-99d39e8f8973)


This analysis confirms that the time complexity of the algorithm is quadratic, and the runtime grows proportionally to \(n^2\) in all cases.

## 4. Determining n0
![n0](https://github.com/user-attachments/assets/5c792a8c-a105-4401-b803-ae073f31ab55)

## Questions 4 and 5: Effect of the Modification on Runtime and Results

### 4. Will This Increase How Long It Takes the Algorithm to Run (e.g., timing the function like in #2)?

Yes, I found that the modified function slightly increases the runtime because of the newly introduced operation `y = i + j` inside the inner loop. However, this operation is a **constant-time operation** \( O(1) \), so while it adds some overhead to each iteration of the loop, it **does not affect the overall time complexity** of the algorithm. The nested loops still run \( n^2 \) times, so the time complexity remains:

\[
T(n) = O(n^2)
\]

In conclusion:
- **Yes**, it increases the runtime slightly due to the additional operation, but the growth rate remains quadratic.

---

### 5. Will It Affect Your Results from #1?

No, the results from Question 1 remain unchanged. In Question 1, I determined the time complexity to be **O(n²)** because of the two nested loops, each iterating \( n \) times. The new operation `y = i + j` is a **constant-time** operation \( O(1) \), so while it adds some work inside each iteration, it does not change the overall growth rate of the function. Therefore, the time complexity is still \( O(n^2) \), and the results from Question 1 are still valid.

In conclusion:
- **No**, this modification does not affect the results from Question 1, as the time complexity remains **O(n²)**.

## 6. Merge Sort Implementation
Here, I implemented the Merge Sort algorithm to sort the provided array.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the array elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# I tested the Merge Sort on the provided array
arr = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
```

