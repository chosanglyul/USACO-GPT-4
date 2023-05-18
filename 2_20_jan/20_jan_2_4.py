def main():
    # Read input
    N = int(input().strip())
    b = list(map(int, input().strip().split()))

    # Initialize a with the first element
    a = [1]

    # Iterate through b and reconstruct a
    for i in range(1, N):
        # Calculate the possible value for the next ai
        ai = b[i - 1] - a[i - 1]
        if ai <= 0:
            ai = 1

        # Append ai to the sequence a
        a.append(ai)

    # Find the lexicographically smallest permutation
    used = [False] * (N + 1)
    for i in a:
        used[i] = True

    unused = [i for i in range(1, N + 1) if not used[i]]
    ans = []
    for i in a:
        if i in unused:
            ans.append(i)
            unused.remove(i)
        else:
            ans.append(unused.pop(0))

    # Print the output
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

