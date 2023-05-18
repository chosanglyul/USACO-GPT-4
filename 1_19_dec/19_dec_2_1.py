def unique_sequence(k, mailbox_colors):
    seen_sequences = set()
    for i in range(len(mailbox_colors) - k + 1):
        sequence = mailbox_colors[i:i+k]
        if sequence in seen_sequences:
            return False
        seen_sequences.add(sequence)
    return True

def main():
    n = int(input())
    mailbox_colors = input()
    
    k = 1
    while not unique_sequence(k, mailbox_colors):
        k += 1
    
    print(k)

if __name__ == "__main__":
    main()

