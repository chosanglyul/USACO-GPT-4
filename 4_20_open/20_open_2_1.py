def min_initial_infected(N, cows):
    cows.sort()
    infected_ranges = []
    for i in range(N):
        if cows[i][1] == 1:
            if not infected_ranges or cows[i][0] - infected_ranges[-1][1] > 1:
                infected_ranges.append([cows[i][0], cows[i][0]])
            else:
                infected_ranges[-1][1] = cows[i][0]

    return len(infected_ranges)

def main():
    N = int(input().strip())
    cows = []
    for _ in range(N):
        x, s = map(int, input().strip().split())
        cows.append((x, s))

    print(min_initial_infected(N, cows))

if __name__ == "__main__":
    main()

