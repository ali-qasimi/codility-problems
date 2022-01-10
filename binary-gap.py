
def solution(N):
    #N_binary = bin(N)
    integer = N
    counter = [0]*10
    x = 0

    while (integer % 2) == 0:
        integer // 2

    while integer >= 1:
        if (integer % 2) == 0:
            counter[x] = counter[x] + 1
        elif (integer % 2) == 1:
            x = x + 1

        integer = integer // 2

    result = max(counter)
    return result


print(solution(1041))
