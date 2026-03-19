from unit1_recurssion import factorial, fibomemo, hanoi, BinarySearch

# T1. Factorial
print("T1. Factorial Tests")
print("Input: 0 Expected: 1 Got:", factorial(0))
print("Input: 5 Expected: 120 Got:", factorial(5))

# T2. Fibonacci (using memoized version for efficiency)
print("T2. Fibonacci Tests")
print("Input: 0 Expected: 0 Got:", fibomemo(0))
print("Input: 1 Expected: 1 Got:", fibomemo(1))
print("Input: 10 Expected: 55 Got:", fibomemo(10))

# T3. Tower of Hanoi
print("T3. Tower of Hanoi Test (n=3)")
hanoi(3, 'A', 'B', 'C')  # should print exactly 7 moves

# T4. Binary Search
print("T4. Binary Search Tests")
arr = [1, 3, 5, 7, 9, 11]
print("Input: target=7 Expected: 3 Got:", BinarySearch(arr, 7, 0, len(arr)-1))
print("Input: target=2 Expected: -1 Got:", BinarySearch(arr, 2, 0, len(arr)-1))
