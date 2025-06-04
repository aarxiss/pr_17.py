from collections import Counter
import string

class TextStats:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.strip().split()
        return len(words)

    def most_common_letter(self):
        letters_only = [char.lower() for char in self.text if char.isalpha()]
        if not letters_only:
            return None
        counter = Counter(letters_only)
        return counter.most_common(1)[0]  # Повертає (літера, кількість)
