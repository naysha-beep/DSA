from unit1_recurssion import factorial, fib_memo, hanoi, rec_binary_search

# T1. Factorial
print("T1. Factorial Tests")
print("Input: 0 Expected: 1 Got:", factorial(0))
print("Input: 5 Expected: 120 Got:", factorial(5))

# T2. Fibonacci (using memoized version for efficiency)
print("\nT2. Fibonacci Tests")
print("Input: 0 Expected: 0 Got:", fib_memo(0))
print("Input: 1 Expected: 1 Got:", fib_memo(1))
print("Input: 10 Expected: 55 Got:", fib_memo(10))

# T3. Tower of Hanoi
print("\nT3. Tower of Hanoi Test (n=3)")
hanoi(3, 'A', 'B', 'C')  # should print exactly 7 moves

# T4. Binary Search
print("\nT4. Binary Search Tests")
arr = [1, 3, 5, 7, 9, 11]
print("Input: target=7 Expected: 3 Got:", rec_binary_search(arr, 7, 0, len(arr)-1))
print("Input: target=2 Expected: -1 Got:", rec_binary_search(arr, 2, 0, len(arr)-1))