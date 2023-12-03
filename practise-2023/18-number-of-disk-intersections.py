# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_a(A):
    # Correctness = 100%, Performance = 0%, Time Complexity = O(N^2)
    
    counter = 0
    iterate_right = True
    iterate_left = True

    for i in range(len(A)-1):
        j = i+1
        while iterate_right:

            distance_right = j - i
            sum_radius_right = A[i] + A[j] 

            if distance_right <= sum_radius_right:
                counter += 1

                if j+1 <= len(A)-1:
                    j += 1
                else:
                    break
            else:
                if j+1 <= len(A)-1:
                    j += 1
                else:
                    break
    
    return counter


def solution(A):
    #!!! Correctness = 100%, Performance = 100%, Time Complexity = Nlog(N)

    boundaries = []
    for i, radius in enumerate(A):
        boundaries.append((i - radius, True))  # Left boundary = True
        boundaries.append((i + radius, False))  # Right boundary = False

    # Sort the boundaries
    boundaries.sort(key=lambda x: (x[0], not x[1]))

    intersections, active_circles = 0, 0
    for _, is_left in boundaries:
        if is_left:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1

        if intersections > 10000000:
            return -1

    return intersections



A = [1, 5, 2, 1, 4, 0]
print(solution(A))