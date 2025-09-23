
def main():
    filename = "task6_read_me.txt"
    word_count = count_words_in_file(filename)
    print(f"The file has {word_count} words")

# Reads file and gets word count
def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # Split on whitespace cjharacters to get words
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()
