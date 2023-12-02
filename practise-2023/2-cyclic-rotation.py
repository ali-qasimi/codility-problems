# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here

    A_rotated = A.copy()
    K_reduced = int(K)
    
    if A:
        if K == len(A):
            return A
        elif A[0]*len(A) == A:
            return A
        else:
            if K//len(A) > 0:
                K_reduced = K_reduced % len(A)

            buffer_start_index = len(A) - K_reduced
            buffer = A[buffer_start_index:]
            A_index_before_buffer = len(A) - K_reduced

            for x in range(len(A[:A_index_before_buffer])):
                A_rotated[x+K_reduced] = A[x]
                
            for x in range(len(buffer)):
                A_rotated[x] = buffer[x]

    return A_rotated



A = [3, 8, 9, 7, 6]
K = 3

print(solution(A, K))