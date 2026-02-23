# word_counter.py

import string
from collections import Counter

def load_text(file_path: str) -> str:
    """Read the content of a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def count_words(text: str) -> int:
    """Count total number of words in the text."""
    words = text.split()
    return len(words)


def count_unique_words(text: str) -> int:
    """Count number of unique words (case insensitive)."""
    words = text.lower().split()
    return len(set(words))


def most_common_words(text: str, n: int = 10) -> list:
    """Return the top n most common words."""
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()

    counter = Counter(words)
    return counter.most_common(n)


def main():
    file_path = input("Enter the path of your essay/blog text file: ")
    text = load_text(file_path)

    if not text:
        return

    total_words = count_words(text)
    unique_words = count_unique_words(text)
    top_words = most_common_words(text)

    print("\n--- Word Count Report ---")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print("\nMost common words:")
    for word, freq in top_words:
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()
