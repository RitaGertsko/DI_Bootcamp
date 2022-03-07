# Mini-Project #2 : Anagram Checker

class AnagramChecker:
    def __init__(self):
        with open("sowpods.txt") as f:
            self.text_list_file = f.read().split()
            self.dictionary = {}
            self.init_mapping()

    def init_mapping(self):
        for list_word in self.text_list_file:
            word = str(sorted(list_word))
            if word in self.dictionary.keys():
                self.dictionary[word].append(list_word.lower())
            else:
                self.dictionary[word] = [list_word.lower()]

    def is_valid_word(self, word):
        return word in self.text_list_file

    def get_anagrams(self, user_word):
        if str(sorted(user_word)) not in self.dictionary.keys():
            return ["no anagrams"]
        else:
            anagrams_list = self.dictionary[str(sorted(user_word))]
            if user_word.lower() in anagrams_list:
                anagrams_list.remove(user_word.lower())
            return anagrams_list

    @staticmethod
    def is_anagram(word1, word2):
        # Compares between user_word and list_word
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) == len(word2) and word2 != word1:
            word1 = sorted(word1)
            word2 = sorted(word2)
            if word1 == word2:
                return True
            else:
                return False

# test = AnagramChecker()
# print(test.get_anagrams('meat'))
