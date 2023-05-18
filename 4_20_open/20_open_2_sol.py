def min_initial_infected(N, cows):
    cows.sort()
    min_gap = float('inf')
    for i in range(1, N):
        if cows[i][1] != cows[i - 1][1]:
            min_gap = min(min_gap, cows[i][0] - cows[i - 1][0])

    R = min_gap - 1

    count = 0
    i = 0
    while i < N:
        if cows[i][1] == 1:
            count += 1
            j = i + 1
            while j < N and cows[j][1] == 1:
                if cows[j][0] - cows[j - 1][0] > R:
                    count += 1
                j += 1
            i = j
        else:
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

