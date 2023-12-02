# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    crossedOut = [0]*len(A)

    for x in range(0,len(A)):
        if crossedOut[x] == 1:
            continue
        for y in range(0,len(A)):
            if y == x:
                continue
            elif crossedOut[y] == 1:
                continue
            else:
                if A[y] == A[x]:
                    crossedOut[y] = 1
                    crossedOut[x] = 1
                    break
    

    oddLocation = crossedOut.index(0)
    oddOccurrence = A[oddLocation]

    #print(crossedOut)
    #print(oddOccurrence)

    return oddOccurrence



solution([9, 3, 9, 3, 9, 7, 9])
