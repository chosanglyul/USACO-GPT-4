def main():
    # Read the input
    n, k = map(int, input().split())
    words = input().split()

    # Initialize variables
    line = ""
    w = 0

    # Iterate through the words
    for i, word in enumerate(words):
        word_length = len(word)

        # If adding the next word would cause the number of non-space characters to exceed K, place it on a new line
        if w + word_length > k:
            print(line.strip())  # Print the current line without trailing spaces
            line = ""  # Start a new line
            w = 0  # Reset the number of non-space characters on the current line

        # Add the word to the current line
        line += word + " "
        w += word_length

        # If this is the last word, print the line
        if i == len(words) - 1:
            print(line.strip())

main()

