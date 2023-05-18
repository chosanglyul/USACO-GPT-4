def main():
    # Read the input
    n, k = map(int, input().split())
    words = input().split()

    # Initialize variables
    line = ""
    line_length = 0

    # Iterate through the words
    for i, word in enumerate(words):
        word_length = len(word)

        # If the word can fit on the current line, add it to the line
        if line_length + word_length <= k:
            if line_length > 0:
                line += " "
                line_length += 1
            line += word
            line_length += word_length
        else:
            # Print the current line and start a new line with the current word
            print(line)
            line = word
            line_length = word_length

        # If this is the last word, print the line
        if i == len(words) - 1:
            print(line)

main()

