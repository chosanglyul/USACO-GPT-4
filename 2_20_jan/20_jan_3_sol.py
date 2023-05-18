def maximum_distance(t, x):
    distance = t * (t + 1) // 2
    extra = min(t, x)
    distance -= extra * (extra - 1) // 2
    return distance

def minimum_time(k, x):
    t = 1
    while maximum_distance(t, x) < k:
        t += 1
    return t

def main():
    k, n = map(int, input().split())
    speeds = [int(input()) for _ in range(n)]

    for x in speeds:
        print(minimum_time(k, x))

if __name__ == "__main__":
    main()

