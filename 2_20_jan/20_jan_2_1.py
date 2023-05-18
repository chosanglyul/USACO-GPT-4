def main():
    # Read input
    N = int(input().strip())
    b = list(map(int, input().strip().split()))

    # Initialize a with the first element
    a = [b[0] - 1]

    # Iterate through b and reconstruct a
    for i in range(1, len(b)):
        # Calculate the minimum possible value for the next ai
        min_ai = max(1, b[i] - (b[i - 1] - a[i - 1]))

        # Append min_ai to the sequence a
        a.append(min_ai)

    # Append the last element of a (b[-1] - a[-1])
    a.append(b[-1] - a[-1])

    # Print the output
    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()

