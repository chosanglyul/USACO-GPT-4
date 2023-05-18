def minimum_time(k, x):
    t = 0
    while True:
        max_distance = t * (t + 1) // 2
        if max_distance >= k:
            if t * (t - 1) // 2 < k:
                return t
            extra = max_distance - k
            if extra <= x * t:
                return t
        t += 1

def main():
    k, n = map(int, input().split())
    speeds = [int(input()) for _ in range(n)]

    for x in speeds:
        print(minimum_time(k, x))

if __name__ == "__main__":
    main()

