def min_initial_infected(N, cows):
    cows.sort()
    max_infected = 0

    for i in range(N):
        if cows[i][1] == 1:
            max_infected += 1

    min_infected = max_infected

    for i in range(N):
        if cows[i][1] == 1:
            infected = 1
            j = i + 1
            while j < N:
                if cows[j][1] == 1:
                    R = cows[j][0] - cows[i][0]
                    infected += 1
                    k = j + 1
                    while k < N and cows[k][0] - cows[j][0] <= R:
                        k += 1
                    j = k
                else:
                    j += 1
            min_infected = min(min_infected, max_infected - infected)

    return min_infected

def main():
    N = int(input().strip())
    cows = []
    for _ in range(N):
        x, s = map(int, input().strip().split())
        cows.append((x, s))

    print(min_initial_infected(N, cows))

if __name__ == "__main__":
    main()

