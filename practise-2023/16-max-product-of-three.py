# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Correctness = 100%, Performance = 100%, Time Complexity = O(NlogN)
    
    A.sort()
    option1 = None

    if A[0] < 0 and A[1] < 0:
        option1 = A[0]*A[1]*A[-1]

    option2 = A[-1]*A[-2]*A[-3]

    if option1:
        if option1 > option2:
            return option1
        else:
            return option2
    else:
            return option2


# A = [-3, 1, 2, -2, 5, 6]
# A = [-5, 5, -5, 4]
A = [10, 10, 10]

print(solution(A))
