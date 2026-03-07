import math

def calculate_hours_needed(pile_sizes, eating_speed):
    total_hours_needed = 0
    for pile_size in pile_sizes:
        total_hours_needed += math.ceil(pile_size / eating_speed)
    return total_hours_needed

def find_minimum_eating_speed(pile_sizes, available_hours):
    minimum_speed = 1
    maximum_speed = max(pile_sizes)
    optimal_speed = maximum_speed
    while minimum_speed <= maximum_speed:
        candidate_speed = minimum_speed + (maximum_speed - minimum_speed) // 2
        hours_needed = calculate_hours_needed(pile_sizes, candidate_speed)

        if hours_needed <= available_hours:
            optimal_speed = candidate_speed
            maximum_speed = candidate_speed - 1
        else:
            minimum_speed = candidate_speed + 1
    return optimal_speed
if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 5
    print(find_minimum_eating_speed(piles, h))