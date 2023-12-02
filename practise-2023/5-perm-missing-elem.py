# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_a(A):
    #Correctness = 100%, Performance = 20%

    if A:
        if len(A) == 1:
            if A[0] == 1:
                return 2
            else:
                return 1
        else:
            for i in range(1, len(A)+2):
                if i not in A:
                    return i
                    break
    else:
        return 1


def solution(A):
    # Corretness = 100%, Performance = 100%
    # Complexity = O(N)

    sum_A = sum(A)
    sum_N = 0

    for i in range(1, len(A)+2):
        sum_N += i

    result = sum_N - sum_A

    return result

print(solution([1, 3]))