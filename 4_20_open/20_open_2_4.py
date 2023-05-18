def min_initial_infected(N, cows):
    cows.sort()
    max_R = -1
    min_infected = N

    for i in range(N):
        if cows[i][1] == 0:
            continue

        j = i - 1
        while j >= 0 and cows[j][1] == 0:
            max_R = max(max_R, cows[i][0] - cows[j][0] - 1)
            j -= 1

    for R in range(1, max_R + 1):
        count = 0
        i = 0
        while i < N:
            if cows[i][1] == 1:
                count += 1
                j = i
                while j < N and cows[j][0] - cows[i][0] <= R:
                    j += 1
                i = j - 1
            i += 1
        min_infected = min(min_infected, count)

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

