def word_counter(text):
    # Remove punctuation marks and split the text into words
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

def main():
    # Get input text from the user
    text = input("Enter some text: ")
    # Call the word_counter function to count words
    count = word_counter(text)
    print("Number of words:", count)

if __name__ == "__main__":
    main()