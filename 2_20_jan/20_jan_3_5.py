def minimum_time(k, x):
    t = 1
    while t * (t + 1) // 2 < k:
        t += 1

    while (t * (t + 1) // 2 - k) > x * t:
        t += 1

    return t

def main():
    k, n = map(int, input().split())
    speeds = [int(input()) for _ in range(n)]

    for x in speeds:
        print(minimum_time(k, x))

if __name__ == "__main__":
    main()

