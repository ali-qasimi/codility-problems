# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Correctness = 100%, Performance = 80%
    
    counter = [0]*N
    maximum = 0

    if min(A) > N:
        pass
    else:
        for i in A:
            if i <= len(counter):
                counter[i-1] += 1
                if counter[i-1] > maximum:
                    maximum = counter[i-1]
            else:
                counter = [maximum]*N
            
    return counter


N = 5
A = [3, 4, 4, 6, 1, 4, 4]
# A = [1]

print(solution(N, A))