def main():
    K, N = map(int, input().split())
    rankings = [list(map(int, input().split())) for _ in range(K)]

    better_than = [[0] * (N + 1) for _ in range(N + 1)]

    for ranking in rankings:
        for i in range(N):
            for j in range(i + 1, N):
                if ranking.index(ranking[i]) < ranking.index(ranking[j]):
                    better_than[ranking[i]][ranking[j]] += 1
                else:
                    better_than[ranking[j]][ranking[i]] += 1

    consistent_pairs = sum(better_than[i][j] == K or better_than[j][i] == K for i in range(1, N + 1) for j in range(i + 1, N + 1))
    print(consistent_pairs)

if __name__ == "__main__":
    main()
