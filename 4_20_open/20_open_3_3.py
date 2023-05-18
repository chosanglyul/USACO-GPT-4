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

        for K in range(0, 251):
            infected = [False] * (N + 1)
            infected[candidate] = True
            hoof_shakes = [0] * (N + 1)
            valid_K = True

            for t, x, y in sorted(interactions):
                if infected[x] and hoof_shakes[x] < K:
                    infected[y] = True
                    hoof_shakes[x] += 1
                if infected[y] and hoof_shakes[y] < K:
                    infected[x] = True
                    hoof_shakes[y] += 1

            for i in range(1, N + 1):
                if cows[i - 1] == '1' and not infected[i]:
                    valid_K = False
                    break

            if valid_K:
                possible_patient_zero.add(candidate)
                min_K = min(min_K, K)
                max_K = max(max_K, K)
                break

    if max_K == 250:
        max_K = "Infinity"

    print(len(possible_patient_zero), min_K, max_K)

main()

