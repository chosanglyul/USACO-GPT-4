def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    max_area = 0

    for i in range(N):
        for j in range(N):
            if points[i][0] == points[j][0] and points[i][1] < points[j][1]:
                for k in range(N):
                    if points[k][1] == points[i][1] and points[k][0] > points[i][0]:
                        area = (points[j][1] - points[i][1]) * (points[k][0] - points[i][0])
                        max_area = max(max_area, area)
                    elif points[k][1] == points[j][1] and points[k][0] > points[j][0]:
                        area = (points[j][1] - points[i][1]) * (points[k][0] - points[j][0])
                        max_area = max(max_area, area)

    print(2 * max_area)


if __name__ == "__main__":
    main()

