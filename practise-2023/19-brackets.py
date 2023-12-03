# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Correctness = 100%, Performance = 100%, Time Complexity = O(N)
    
    if len(S) % 2 != 0:
        return 0
    
    stack = []
    bracket_open = {'(', '{', '['}
    bracket_close = {')', '}', ']'}
    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for bracket in S:
        if bracket in bracket_open:
            stack.append(bracket)
        elif bracket in bracket_close:
            if len(stack) > 0:
                if  stack[-1] != bracket_pairs[bracket]:
                    return 0
                else:
                    stack.pop()
            else:
                return 0
    
    if len(stack) == 0:
        return 1
    else:
        return 0


# A = "{[()()]}"
# A = "([)()]"
A = ")("
print(solution(A))

