def solution_a(A):
    # Correctness = 100%, Performance = 0%
    # Time Complexity = O(N^2), because of count() inside for loop

    car_counter = 0

    for i in range(len(A)):
        if A[i] == 0:
            cars_facing = A[i+1:]
            car_counter += cars_facing.count(1)

        elif A[i] == 1:
            cars_facing = A[0:i]
            car_counter += cars_facing.count(0)
        
        if car_counter > 1000000000:
            car_counter = -1 
            break

    car_counter = car_counter // 2

    return car_counter


def solution(A):
    # Correctness = 100%, Performance = 100%
    # Time Complexity = O(N)
    
    car_counter = 0
    traveling_east = 0

    for i in A:
        if i == 0:
            traveling_east += 1
        else:
            car_counter += traveling_east

        if car_counter > 1000000000:
            car_counter = -1
            break
    
    return car_counter

cars = [0, 1, 0, 1, 1]
print(solution(cars)) 