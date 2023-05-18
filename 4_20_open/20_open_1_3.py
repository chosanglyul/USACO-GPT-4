def main():
    N = int(input().strip())
    stalls = input().strip()

    # Find the gaps between occupied stalls
    gaps = [len(gap) for gap in stalls.split('1') if len(gap) > 0]

    # Sort the gaps in descending order
    gaps.sort(reverse=True)

    # Find the largest possible D by placing two new cows optimally
    if len(gaps) == 1:
        max_distance = max((gaps[0] + 1) // 2, gaps[0] - 1)
    else:
        max_distance = max(gaps[1], (gaps[0] + 1) // 2)

    print(max_distance)

if __name__ == "__main__":
    main()

