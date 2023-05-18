def minimum_time(k, x):
    t = 0
    while True:
        max_distance = t * (t + 1) // 2
        min_distance = max_distance - t * x
        if min_distance <= k <= max_distance:
            break
        t += 1
    return t

def main():
    k, n = map(int, input().split())
    speeds = [int(input()) for _ in range(n)]

    for x in speeds:
        print(minimum_time(k, x))

if __name__ == "__main__":
    main()

