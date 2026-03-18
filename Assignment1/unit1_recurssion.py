#Factorial recursive
# n1=int(input("Enter the number for factorial"))
def factorial(n):
    
    """
    Compute the factorial of a positive integer n using recursion.

    Base Case:
        - If n == 1, return 1.
        - If n < 1, return None (invalid input).

    Time Complexity:
        O(n), since the function makes n recursive calls.

    Space Complexity:
        O(n), due to the recursion stack depth.
    """
    if n<1:
        return None
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
# print("Factorial of",n1,"! is:",end=" ")
# print(factorial(n1))

#Fibonacci
#Fib_naive() fuunction
count_n=0
def fib_naive(n):
    """
    Compute the nth Fibonacci number using naive recursion.

    Base Case:
        - If n == 0, return 0.
        - If n == 1, return 1.

    Time Complexity:
        O(2^n), because each call branches into two recursive calls.

    Space Complexity:
        O(n), due to recursion stack depth.
    """
    global count_n
    count_n+=1
    a=0
    b=1
    if n==1 :
        return 1
    elif n==0:
        return 0
    else:
        return fib_naive (n-1)+fib_naive (n-2)
# n2=int(input("Enter the number for naive series"))

#Showing the fibonacci series for naive function   
def fibnaive_series(n):
    series=[]
    for i in range(n+1):
        series.append(fib_naive(i))
    return series



#Fib_memo function
count_m=0
memo={}#creating a dictionary to store all the values , so as to memorize
def fib_memo(n):
    """
    Compute the nth Fibonacci number using recursion with memoization.

    Base Case:
        - If n == 0, return 0.
        - If n == 1, return 1.

    Time Complexity:
        O(n), since each Fibonacci number is computed once and stored.

    Space Complexity:
        O(n), for the memo dictionary and recursion stack.
    """
    global count_m
    count_m+=1
    if n in memo:
        return memo[n]
    elif n==0:
        memo[0]=0
    elif n==1:
        memo[1]=1
    else:
        memo[n]=fib_memo(n-1)+fib_memo(n-2)
    return memo[n]

#Showing the fibonacci series for memo function
def fmemo_series(n):
    series=[]
    for i in range(n+1):
        series.append(fib_memo(i))
    return series
#Outputs
# n3=int(input("Enter the number for memo series"))
# print("Results from fib_naive are:")
# print(fibnaive_series(n2))
# print("Number of times function has been called:")
# print(count_n)
# print("Results from fib_memo are:")
# print(fib_memo(n3))
# print("Number of times function has been called:")
# print(count_m)
#HANAOI TOWER
def hanoi(n, src, aux, dst):
    """
    Solve Tower of Hanoi problem for n disks.

    Prints moves in the format:
        "Move disk X from SRC to DST"

    Base Case:
        If n == 1, move the single disk directly from src to dst.

    Recursive Case:
        - Move n-1 disks from src → aux (using dst as helper).
        - Move the nth disk from src → dst.
        - Move n-1 disks from aux → dst (using src as helper).
    """
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
    else:
        hanoi(n-1, src, dst, aux)
        print(f"Move disk {n} from {src} to {dst}")
        hanoi(n-1, aux, src, dst)


def rec_binary_search(a, target, lo, hi):
    """
    Recursive Binary Search on a sorted list.

    Args:
        a (list): Sorted list of elements.
        target: Value to search for.
        lo (int): Lower index of search range.
        hi (int): Upper index of search range.

    Returns:
        Index of target if found, else -1.
    """
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == target:
        return mid
    elif target < a[mid]:
        return rec_binary_search(a, target, lo, mid - 1)
    else:
        return rec_binary_search(a, target, mid + 1, hi)