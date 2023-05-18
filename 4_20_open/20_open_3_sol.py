def main():
    N, T = map(int, input().split())
    cows = input()
    interactions = [tuple(map(int, input().split())) for _ in range(T)]

    possible_patient_zero = set()
    min_K = float("inf")
    max_K = -1

    for candidate in range(1, N + 1):
        if cows[candidate - 1] == '0':
            continue

        for K in range(T + 1):
            infected = [cows[i] == '1' for i in range(N)]
            infected[candidate - 1] = True
            hoof_shakes = [0] * N

            for t, x, y in sorted(interactions):
                if infected[x - 1] and hoof_shakes[x - 1] < K:
                    infected[y - 1] = True
                    hoof_shakes[x - 1] += 1
                if infected[y - 1] and hoof_shakes[y - 1] < K:
                    infected[x - 1] = True
                    hoof_shakes[y - 1] += 1

            if all(infected[i] == (cows[i] == '1') for i in range(N)):
                possible_patient_zero.add(candidate)
                min_K = min(min_K, K)
                max_K = max(max_K, K)

    if max_K == T:
        max_K = "Infinity"

    print(len(possible_patient_zero), min_K, max_K)

main()

