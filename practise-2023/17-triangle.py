# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Correctness = 100%, Performance = 100%, Time Complexity = O(NlogN)
    
    A.sort()

    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2] and A[i+1]+A[i+2] > A[i] and A[i+2]+A[i] > A[i+1]:
            return 1
    
    return 0


# A = [10, 2, 5, 1, 8, 20]
A = [10, 50, 5, 1]

print(solution(A))