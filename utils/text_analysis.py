def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> int:
    return len(text)

def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

def search_and_replace(text: str, search_word: str, replace_word: str) -> str:
    return text.replace(search_word, replace_word)

def contains_python(text: str) -> bool:
    return 'Python' in text

def average_word_length(text: str) -> float:
    words = text.split()
    if not words:
        return 0.0
    return len(text) / len(words)  # Includes spaces per assignment requirement