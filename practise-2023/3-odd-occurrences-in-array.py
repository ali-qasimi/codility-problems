# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_a(A):
    # Correctness = 100%. Performance = 50%. O(N^2)
    for x in A:
        if A.count(x) == 1:
            return x

def solution_b(A):
    # Correctness = 100%. Performance = 66%. O(N^2)

    A.sort()
    
    while len(A) > 1:
        if A[0] == A[1]:
            A.pop(0)
            A.pop(0)
        else:
            return A[0]
    
    return A[0]

def solution_c(A):
    # Correctness = 100%, Performance = 66%

    while len(A) != 1:
        A_popped = A.copy()
        A_popped.pop(0)

        if A[0] in A_popped:
            value = A[0]
            A.pop(0)

            # print(A.index(value))
            
            A.pop(A.index(value))
        else:
            return(A[0])
            break
            
    return A[0]

def solution(A):
    # Correctness = 100%. Performance = 100%.
    unpaired_integers = set()

    for i in A:
        if i in unpaired_integers:
            unpaired_integers.remove(i)
        else:
            unpaired_integers.add(i)
    
    result = list(unpaired_integers)
    return result[0]





A = [ 1000000, 2000000, 1000000, 30000000, 5000000, 2000000, 30000000 ]

print(solution(A))

