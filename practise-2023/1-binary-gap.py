# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    n_binary = bin(N)
    n_binary = n_binary[2:]
    occurrence = 0
    counts = [0]*10

    for x in range(len(n_binary)):

        if n_binary[x] == '1' and x == 0:
            continue
        elif n_binary[x] == '0' and x == len(n_binary)-1:
            counts[occurrence] = 0
            occurrence -= 1
        elif n_binary[x] == '0':
            counts[occurrence] += 1
        elif n_binary[x] == '1' and n_binary[x-1] == '0':
            occurrence +=1
        

    return max(counts)



# print(solution(32))
# print(solution(1041))
print(solution(66561))