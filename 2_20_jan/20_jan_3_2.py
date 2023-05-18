def minimum_time(k, x):
    lo, hi = 0, 2 * k
    while lo < hi:
        mid = (lo + hi) // 2
        max_distance = mid * (mid + 1) // 2
        if max_distance - mid * x >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    k, n = map(int, input().split())
    speeds = [int(input()) for _ in range(n)]

    for x in speeds:
        print(minimum_time(k, x))


if __name__ == "__main__":
    main()

