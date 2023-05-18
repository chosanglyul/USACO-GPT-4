def main():
    from itertools import permutations
    cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
    n = int(input().strip())
    constraints = [input().strip().split(" must be milked beside ") for _ in range(n)]

    def valid_ordering(order):
        for a, b in constraints:
            if abs(order.index(a) - order.index(b)) != 1:
                return False
        return True

    for order in permutations(sorted(cows)):
        if valid_ordering(order):
            for cow in order:
                print(cow)
            break

if __name__ == "__main__":
    main()
