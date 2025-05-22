class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        sorted_word = sorted(self.word)
        return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted_word]
