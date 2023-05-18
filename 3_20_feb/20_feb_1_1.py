def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    max_area = 0

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                p1, p2, p3 = points[i], points[j], points[k]
                if (p1[0] == p2[0] and p1[1] != p2[1] and
                        (p1[0] == p3[0] or p2[0] == p3[0]) and
                        (p1[1] == p3[1] or p2[1] == p3[1])):
                    area = abs((p1[1] - p2[1]) * (p1[0] - p3[0]))
                    max_area = max(max_area, area)

    print(2 * max_area)


if __name__ == "__main__":
    main()

