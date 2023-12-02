# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # Correctness = 100%, Performance = 100%
    # Time Complexity: O(1)

    counter = 0

    if A > 0:
        x = A // K
    else:
        x = 0

    if B > 0:
        y = B // K
    else:
        y = 0

    counter = y - x

    if A % K == 0:          #count this again because it got subtracted
        counter += 1

    
    return counter

# print(solution(6, 11, 2))
print(solution(0, 0, 11))
