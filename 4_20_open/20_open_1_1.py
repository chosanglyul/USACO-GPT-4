def main():
    N = int(input().strip())
    stalls = input().strip()

    # Find the gaps between occupied stalls
    gaps = [len(gap) for gap in stalls.split('1') if len(gap) > 0]

    # Calculate the maximum distance after placing the new cows
    max_distance = 0
    for gap in gaps:
        if gap % 2 == 0:
            max_distance = max(max_distance, (gap // 2) + 1)
        else:
            max_distance = max(max_distance, (gap + 1) // 2)

    print(max_distance)

if __name__ == "__main__":
    main()

