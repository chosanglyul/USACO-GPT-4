def min_initial_infected(N, cows):
    cows.sort()
    count = 0
    i = 0
    while i < N:
        if cows[i][1] == 1:
            count += 1
            left = i
            right = i
            while right < N - 1 and cows[right + 1][0] - cows[left][0] <= 1:
                right += 1
                if cows[right][1] == 1:
                    left = right
            i = right
        i += 1
    return count

def main():
    N = int(input().strip())
    cows = []
    for _ in range(N):
        x, s = map(int, input().strip().split())
        cows.append((x, s))

    print(min_initial_infected(N, cows))

if __name__ == "__main__":
    main()

