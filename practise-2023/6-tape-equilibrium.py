# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Correctness = 100%, Performance = 100%
    
    aggregate_a_left = [0]*len(A)
    aggregate_a_right = [0]*len(A)

    aggregate_a_left[0] = A[0]
    aggregate_a_right[-1] = A[-1]

    for i in range(1,len(A)):
        aggregate_a_left[i] = aggregate_a_left[i-1] + A[i]
        aggregate_a_right[-(i+1)] += aggregate_a_right[-(i)] + A[-(i+1)]

    # P = 1
    minimum = abs(aggregate_a_left[0] - aggregate_a_right[1])
            
    for j in range(1,len(A)-1):
        difference = abs(aggregate_a_left[j] - aggregate_a_right[j+1])
        if difference < minimum:
            minimum = difference

    return minimum
    

    # return [aggregate_a_left, aggregate_a_right, difference, difference_abs]
    
        

A = [3, 1, 2, 4, 3]
print(solution(A))