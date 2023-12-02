# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_a(A):
    # Correctness = 80%, Performance = 50%
    
    A.sort()

    result = 0

    if A[-1] <= 0:                          #when last integer is negative
        result = 1
    elif len(A) == 1:                       #
        if A[0] != 1:
            result = 1
        # else: 
        #     result = 2
    else:
        for i in range(len(A)-1):
            if A[i] > i+1:                  #starting integers greater than 1
                result = 1
                break
            if A[i+1] == A[i]:              #repeating integers
                continue
            elif A[i+1] - A[i] != 1:
                if A[i] <= 0 and A[i+1] != 1:           #e.g. ... , -1, 3, ...
                    result = 1
                elif A[i] <= 0 and A[i+1] <=0:          #when both integers negative
                    continue
                else:
                    result = A[i]+1
                break
    
    if result == 0:
        result = A[len(A)-1] + 1
    
    return result
            


def solution(A):
    # Correctness = 100%, Performance = 100%
    # Time Complexity: O(N)

    boolean_result = [0]*len(A)

    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= len(A):
            boolean_result[A[i]-1] = 1
    
    try:
        result_index = boolean_result.index(0) + 1
    except:
        result_index = len(A) + 1

    return result_index


# A = [1, 3, 6, 4, 1, 2]
# A = [1, 2, 3]
# A = [-1, -3]
# A = [4, 5, 6, 3]
# A =  [-1000000, 1000000]
# A = [-1, -3, 5]
A = [-1000, 10]

print(solution(A))