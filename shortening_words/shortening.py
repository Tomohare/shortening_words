#!/usr/bin/env python

# import argparse
import pyphen


class Shortening_Words(object):
    """docstring for Shortening_Words"""

    def __init__(self, words, max_len):
        self.dic = pyphen.Pyphen(lang='en')
        listWords = words.split(" ")
        self.max_len = int(max_len) - (len(listWords)
                                       if int(max_len) < len(words) else 0)
        self.phrase = self.short_words(listWords)

    def insert(self, index, element, _list):
        pos = 1
        for item in _list:
            if item[index] >= element[index]:
                pos += 1
            elif item[index] < element[index]:
                pos -= 1
                break
        _list.insert(pos, element)
        return _list

    def measure_word(self, sizes):
        newListWords = {}
        for i in range(max([len(x) for x in sizes])):
            for idx, s in enumerate(sizes):
                if i < len(s):
                    if i not in newListWords:
                        newListWords[i] = []
                    if i > 0:
                        summation = sum([a[2] for a in newListWords[i-1]])
                        element = (idx, s[i], s[i]+summation)
                    else:
                        element = (idx, s[i], s[i])
                    newListWords[i] = self.insert(2, element, newListWords[i])
        return newListWords

    def length_Word(self, newListWords):
        total = 0
        listWords = {}
        for x in newListWords:
            for y in newListWords[x]:
                if total + y[1] > self.max_len:
                    break
                total += y[1]
                if y[0] in listWords:
                    listWords[y[0]] += y[1]
                else:
                    listWords[y[0]] = y[1]
        return listWords

    def short_words(self, listWords):
        sizes = []
        for word in listWords:
            sizes.append(self.get_list_sizes(word))
        newListWords = self.measure_word(sizes)
        listWords2 = self.length_Word(newListWords)
        phrase = [""]*len(sizes)
        for idx, word in enumerate(listWords):
            if idx in listWords2:
                phrase[idx] = word[:listWords2[idx]]
            else:
                phrase[idx] = word[:1]
            if len(phrase[idx]) < len(word):
                phrase[idx] += "."

        return " ".join(phrase)

    def shortWord(self, word, max_len):
        s = self.dic.inserted(word).split("-")
        pos = 1
        for letters in s:
            if len(letters) < max_len:
                pos += 1
            else:
                "is too big, we get the rest"
                break
        res = "".join(s[:pos])
        res += "." if len(res) < len(word) else ""
        return res

    def get_list_sizes(self, word):
        return [len(x) for x in self.dic.inserted(word).split("-")]


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Shortening words')
#     parser.add_argument('-w',
#                         dest='words',
#                         help="words to shortening",
#                         type=str,
#                         action='store', default='')
#     parser.add_argument('-l',
#                         dest='max_len',
#                         help="word to shortening",
#                         type=str,
#                         action='store', default='')
#     args = parser.parse_args()

#     print(Shortening_Words(**vars(args)).phrase)
