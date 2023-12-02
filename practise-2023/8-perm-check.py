# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Correctness = 100%, Performance = 100%
    # Time Complexity = O(N)

    if A:
        A.sort()
        result = 0

        if A[0] != 1:
            result = 0
        elif len(A) == 1:
            if A[0] == 1:
                result = 1
            else:
                result = -1
        else:
            for i in range(1,len(A)):
                if A[i] == A[i-1] +1:
                    result = 1
                else:
                    result = 0
                    break
    
    return result


A = [1,3]

print(solution(A))