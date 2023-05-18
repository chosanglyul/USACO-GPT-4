def main():
    n, k = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    if a1 > b1:
        a1, a2, b1, b2 = b1, b2, a1, a2

    cows = list(range(1, n + 1))
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        pos = i
        cycle_length = 0

        while True:
            if a1 <= pos <= a2:
                pos = a1 + a2 - pos
            if b1 <= pos <= b2:
                pos = b1 + b2 - pos

            cycle_length += 1
            if pos == i:
                break

        remainder = k % cycle_length
        for _ in range(remainder):
            if a1 <= pos <= a2:
                pos = a1 + a2 - pos
            if b1 <= pos <= b2:
                pos = b1 + b2 - pos

        result[pos] = i

    for i in range(1, n + 1):
        print(result[i])

if __name__ == '__main__':
    main()

