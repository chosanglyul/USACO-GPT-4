def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    max_area = 0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and i != k and j != k:
                    corner, base, height = points[i], points[j], points[k]
                    if corner[1] == base[1] and corner[0] == height[0]:
                        area = abs((corner[0] - base[0]) * (corner[1] - height[1]))
                        max_area = max(max_area, area)

    print(max_area)


if __name__ == "__main__":
    main()

