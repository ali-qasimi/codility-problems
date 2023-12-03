# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # WIP, Correctness = 25%
    iterate = True
    i = 0
    if len(A) > 1:
        while iterate:
            if B[i]:
                alive = True
                fish_size = A[i]

                j = i + 1
                while alive:
                    if B[j] == 0:
                        if fish_size > A[j]:
                            A.pop(j)
                            B.pop(j)
                        else:
                            A.pop(i)
                            B.pop(i)
                            alive = False
                    elif j + 1 < len(A):
                        j += 1
                        continue
                    else:
                        alive = False
                        if i + 1 < len(A)-1:
                            i += 1
                            break
                        else:
                            iterate = False
                            break
                    
                    if j < len(A):
                        continue
                    else:
                        alive = False
                        iterate = False
            elif i + 1 < len(A):
                i += 1

    result = len(A)

    return result



A = [4, 3, 2, 1, 5]  #size
B = [0, 1, 0, 0, 0]  #direction

# A = [1]
# B = [0]

# A = [0, 1]
# B = [1, 1]

print(solution(A,B))