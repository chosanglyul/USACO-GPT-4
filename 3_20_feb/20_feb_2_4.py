def min_machine_uses(n, a, b):
    machine_uses = 0

    for i in range(n):
        if a[i] != b[i]:
            machine_uses += 1
            b = b[:i + 1] + ''.join(['H' if x == 'G' else 'G' for x in b[i + 1:]])

    return machine_uses

if __name__ == "__main__":
    n = int(input().strip())
    a = input().strip()
    b = input().strip()

    result = min_machine_uses(n, a, b)
    print(result)

