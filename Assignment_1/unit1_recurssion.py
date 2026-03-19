#Factorial recursive
# n1=int(input("Enter the number for factorial"))
def factorial(n):
    
    """
    Base Case:
        If n == 1 or n<1that would be invalid
    Time Complexity:
        O(n), function makes n recursive calls.
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
def fibonaive(n):
    """
    Base Case:
        If n == 0, return 0
        If n == 1, return 1
    Time Complexity:O(2^n), because each call branches into two recursive calls.
    Space Complexity:O(n), due to recursion stack depth.
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
        return fibonaive (n-1)+fibonaive (n-2)
# n2=int(input("Enter the number for naive series"))

#Showing the fibonacci series for naive function   
def fibnaive_series(n):
    series=[]
    for i in range(n+1):
        series.append(fibonaive(i))
    return series



#Fib_memo function
count_m=0
memo={}#creating a dictionary to store all the values , so as to memorize
def fibomemo(n):
    """
    Base Case:
        If n == 0, return 0
        If n == 1, return 1
    Time Complexity:O(n), since each Fibonacci number is computed once and stored.
    Space Complexity:O(n), for the memo dictionary and recursion stack.
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
        memo[n]=fibomemo(n-1)+fibomemo(n-2)
    return memo[n]

#Showing the fibonacci series for memo function
def fibomemo_series(n):
    series=[]
    for i in range(n+1):
        series.append(fibomemo(i))
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
def hanoi(n,start,aux,end):
    """
    Base case=>n==1
    simply move disk from start to end
    Time Complexity=>base case=O(1)
    Recursive case=>O(2^n)because each call branches into two recursive calls.
    """
    if n==1:
        print("Move disk 1 from{} to {}".format(start,end))

    else:
        hanoi(n-1,start,end,aux)
        print("Move disk {} from{} to {}".format(n,start,end))
        hanoi(n-1,aux,start,end)
    # print("Move disk {} from{} to {}".format(n,))



def BinarySearch(a, target, lo, hi):
    """
    Arguments:
        a (list): Sorted 
        target: Value to search 
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
        return BinarySearch(a, target, lo, mid - 1)
    else:
        return BinarySearch(a, target, mid + 1, hi)