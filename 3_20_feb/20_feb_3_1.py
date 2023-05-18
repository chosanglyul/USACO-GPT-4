def main():
    n, k = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    if (a1 < b1 and a2 < b1) or (b1 < a1 and b2 < a1):
        k = k % 2
    else:
        k = k % 6

    cows = [i for i in range(1, n+1)]
    for _ in range(k):
        cows[a1-1:a2] = reversed(cows[a1-1:a2])
        cows[b1-1:b2] = reversed(cows[b1-1:b2])

    for cow in cows:
        print(cow)

if __name__ == "__main__":
    main()
    
