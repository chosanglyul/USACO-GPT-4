def main():
    k, n = map(int, input().split())
    speeds = [int(input()) for _ in range(n)]
    for x in speeds:
        lo, hi = 0, k
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * (mid + 1) // 2 + x * mid >= k:
                hi = mid
            else:
                lo = mid + 1
        print(lo)

if __name__ == "__main__":
    main()

