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

    # Find the largest possible D by placing two new cows optimally
    max_distance = max((largest_gap + 1) // 2, second_largest_gap)

    print(max_distance)

if __name__ == "__main__":
    main()

