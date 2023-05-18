def main():
    N = int(input().strip())
    stalls = input().strip()

    # Add boundary markers to simplify edge case handling
    stalls = '1' + stalls + '1'

    # Find the gaps between occupied stalls
    gaps = [len(gap) for gap in stalls.split('1') if len(gap) > 0]

    # Initialize the values for the largest and second largest gaps
    largest_gap, second_largest_gap = 0, 0
    for gap in gaps:
        if gap > largest_gap:
            largest_gap, second_largest_gap = gap, largest_gap
        elif gap > second_largest_gap:
            second_largest_gap = gap

    # Case 1: Place both cows in the largest gap
    case1 = (largest_gap - 1) // 2

    # Case 2: Place one cow in the largest gap and another in the second largest gap
    case2 = min((largest_gap + 1) // 2, second_largest_gap)

    # Find the largest possible D by placing two new cows optimally
    max_distance = max(case1, case2)

    print(max_distance)

if __name__ == "__main__":
    main()

