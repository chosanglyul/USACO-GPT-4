def main():
    N = int(input())
    stalls = list(map(int, list(input().strip())))

    # List to store the lengths of the gaps
    gap_lengths = []
    count = 0

    for i in range(N):
        if stalls[i] == 0:
            count += 1
        else:
            if count > 0:
                gap_lengths.append(count)
            count = 0

    # Append the last gap if any
    if count > 0:
        gap_lengths.append(count)

    # Sort the gaps in descending order
    gap_lengths.sort(reverse=True)

    # If there's only one gap, split it into two as evenly as possible
    if len(gap_lengths) == 1:
        d1 = (gap_lengths[0] + 1) // 2
        d2 = gap_lengths[0] // 2
    # If there's more than one gap, put one cow in the largest gap, and the other in the second largest
    else:
        d1 = gap_lengths[0]
        d2 = max((d1 + 1) // 2, gap_lengths[1])

    print(min(d1, d2))


if __name__ == "__main__":
    main()

