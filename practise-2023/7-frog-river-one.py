# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_a(X, A):
    # Correctness = 100%, Performance = 0%
    # Time complexity = O(N^2)
    
    position_filled_times = [0]*(X+1)

    for i in range(0,X+1):
        if i in A:
            timestamp = A.index(i)
            position_filled_times[i] = timestamp
        
    
    if position_filled_times.count(0) > 2:
        return -1
    else:
        return max(position_filled_times)

def solution(X, A):
    # Completeness = 100%, Performance = 100%
    # Time Complexity = O(N)

    position_filled = [0]*(X)
    minimum = -1

    for i in range(len(A)):
        if A[i] <= X and position_filled[A[i]-1] == 0:
            position_filled[A[i]-1] = 1
            minimum = i

        # if all(position_filled):    #no need, makes the function O(n^2)
        #     break
    
    if not all(position_filled):
        minimum = -1

    return minimum


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]

print(solution(X, A))