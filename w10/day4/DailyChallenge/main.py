# Daily Challenge : Text Analysis

import re
import string


class Text:
    def __init__(self, text: str):
        self.text = text

    def check_frequency(self, word: str):
        occurrences = self.text.count(word)
        return occurrences

    def most_common_word(self):
        frequency = 0
        common_word = ""
        word_list = self.text.replace("\n", "").split(" ")
        for word in word_list:
            if word == "":
                continue
            word_freq = self.check_frequency(word)
            if word_freq > frequency:
                frequency = word_freq
                common_word = word
        return common_word

    def unique_words(self):
        words_list = []
        for word in self.text.split():
            if self.check_frequency(word) == 1:
                words_list.append(word)
        print(words_list)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            file_text = f.read()
        return cls(file_text)


class TextModification(Text):
    def no_punctuation(self):
        new_text = re.sub(f'[{string.punctuation}]', '', self.text)
        return new_text

    def no_stopwords(self):
        with open('stopwords.txt') as file:
            stopwords_list = file.read().split()
            new_list = [word for word in self.text.split() if word not in stopwords_list]
            print(' '.join(new_list))

    def no_special_characters(self):
        new_text = re.sub(r'[^\w\s]', "", str(self.text))
        return new_text


test = Text.from_file('the_stranger.txt')

# print(test.check_frequency("THE"))
# print(test.check_frequency("bada"))
# print(test.unique_words())
# print(TextModification(test.text).no_punctuation()[:20])
# print(TextModification(test.text).no_special_characters()[:20])
