#def new_index(length,K):


def solution(A, K):
    # write your code in Python 3.6
    if A:
        A_rotated = [0]*len(A)
        if K >= len(A):
            K = K % len(A)

        A_buffer = A[len(A)-K:len(A)]

        #print(A_buffer)

        
        for x in range(0,len(A)-K):
            A_rotated[x+K] = A[x]

        #print(A_rotated[0:K])
        A_rotated[0:K] = A_buffer
    
    else:
        A_rotated = A

    return A_rotated



print(solution([1, 2, 3, 4],1))
