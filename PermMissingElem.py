def solution(A):
    A.sort()

    if len(A) <= 1:
        return A[0]
    elif 1 not in A:
        answer = 1
        return answer
    elif len(A) == 2:
        if A[1] - A[0] != 1:
            answer = A[0]+1
            return answer
    else:
        for x in range(0,len(A)-1):
            if A[x+1] - A[x] != 1:
                answer = A[x]+1
                return answer

print(solution([2, 3, 1, 5]))