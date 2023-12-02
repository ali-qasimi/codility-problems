def solution(X, Y, D):
    diff = Y - X
    hops = diff//D

    result = X + D*hops

    if result >= Y:
        return hops
    else:
        hops += 1
        return hops

print(solution(10,85,30))

