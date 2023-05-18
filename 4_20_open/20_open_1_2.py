def main():
    N = int(input().strip())
    stalls = input().strip()

    # Find the gaps between occupied stalls
    gaps = [len(gap) for gap in stalls.split('1') if len(gap) > 0]

    # Calculate the sum of the two largest gaps
    two_largest_gaps = sorted(gaps, reverse=True)[:2]
    max_distance = sum((gap + 1) // 2 for gap in two_largest_gaps) - 1

    print(max_distance)

if __name__ == "__main__":
    main()

