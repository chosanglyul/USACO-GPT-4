def main():
    # Read the input
    n, k = map(int, input().split())
    words = input().split()

    # Initialize variables
    line = ""
    line_length = 0

    # Iterate through the words
    for word in words:
        word_length = len(word)
        
        # If the word can fit on the current line, add it to the line
        if line_length == 0:
            line += word
            line_length += word_length
        elif line_length + word_length + 1 <= k:
            line += " " + word
            line_length += word_length + 1
        else:
            # Print the current line and start a new line with the current word
            print(line)
            line = word
            line_length = word_length

    # Print the last line
    print(line)

main()

