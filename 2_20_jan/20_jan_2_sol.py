def main():
    def is_valid_permutation(a, N):
        unique_elements = set(a)
        return all(1 <= ai <= N for ai in a) and len(unique_elements) == N

    # Read input
    N = int(input().strip())
    b = list(map(int, input().strip().split()))

    for i in range(1, N + 1):
        a = [0] * N
        a[0] = i
        for j in range(1, N):
            a[j] = b[j - 1] - a[j - 1]

        if is_valid_permutation(a, N):
            print(" ".join(map(str, a)))
            break


if __name__ == "__main__":
    main()

