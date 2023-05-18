def min_machine_uses(n, a, b):
    machine_uses = 0

    i = 0
    while i < n:
        if a[i] != b[i]:
            machine_uses += 1
            while i < n and a[i] != b[i]:
                i += 1
        i += 1

    return machine_uses

if __name__ == "__main__":
    n = int(input().strip())
    a = input().strip()
    b = input().strip()

    result = min_machine_uses(n, a, b)
    print(result)

