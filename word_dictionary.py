class WordDictionary:
    def __init__(self, word_file):
        self.word_file = word_file
        self.all_words = self.load_words(self.word_file)

    def load_words(self, word_file):
        with open(word_file, "r") as f:
            dictionary = f.read()

        return [x.lower() for x in dictionary.split("\n")]

    def is_valid_word(self, word):
        return word in self.all_words
