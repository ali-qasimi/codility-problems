# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    distance = Y - X
    jump_count = distance // D

    if distance % D > 0: 
        return jump_count + 1
    else:
        return jump_count

print(solution(10, 85, 30))