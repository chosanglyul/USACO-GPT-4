def main():
    # Read input
    N = int(input().strip())
    b = list(map(int, input().strip().split()))

    # Initialize a
    a = [0] * N
    a[0] = b[0] - 1

    # Iterate through b and reconstruct a
    for i in range(1, N - 1):
        a[i] = b[i] - b[i - 1] + a[i - 1]
        if a[i] < 1:
            a[i] = 1

    # Calculate the last element of a
    a[-1] = b[-1] - a[-2]

    # Print the output
    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()

