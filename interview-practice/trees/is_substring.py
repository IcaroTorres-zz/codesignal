'''Trie Tree script class to solve codefights interview practice - Trees "isSubstring"'''
class Trie:
    '''Trie(letter) -> Trie letters Tree Object {
    \t    self.letter = letter,
    \t    self.terminal = False,
    \t    self.children = {}
    }
    A Trie Object representing a Tree (or Sub-Tree) with a ".letter" property
    and any number of children Trie Nodes on ".children" property
    (Ex: children['A'], children['z'], children['8']...) starting as an empty
    dictionary, and a ".terminal" property set as False as default'''
    def __init__(self, letter):
        self.letter = letter
        self.terminal = False
        self.children = {}


    def add_text_fragment(self, text_fragment):
        '''Given a text fragment, for each char, check if there is such char already on
        Trie Object and create a new Trie Object with this char if it is not there yet.
        Set the last Trie Object Node ".terminal" == True as successfully forming a text
        fragment inside the Trie.'''
        cur = self
        for char in text_fragment:
            if char not in cur.children:
                cur.children[char] = Trie(char)
            cur = cur.children[char]
        cur.terminal = True

def enclose_substring(word, trie):
    '''Given word and a Trie Object, return word with the longest path from "parts"
    list within each "words" element enclosed by "[]" if the is such part as
    substring of element. If more than one part is substring of a "words" list element,
    return the one which occurs first.'''
    longest_length, longest_pos = 0, 0

    for start in range(len(word)):
        cur = trie
        for pos in range(start, len(word)):
            letter = word[pos]
            if letter not in cur.children:
                break
            cur, length = cur.children[letter], pos - start + 1
            if cur.terminal and length > longest_length:
                longest_length, longest_pos = length, start

    if longest_length == 0:
        return word

    end = longest_pos + longest_length
    return word[:longest_pos] + "[" + word[longest_pos: end] + "]" + word[end:]


def findSubstrings(word_list, part_list):
    '''Given two string lists (words, parts), return a list of strings similar to passed
    "words" list, with the longest part from "parts" list within each "words" element
    enclosed by "[]" if the is such part as substring of element. If more than one part
    is substring of a "words" list element, return the one which occurs first.'''
    trie = Trie('')
    for part in part_list:
        trie.add_text_fragment(part)
    return [enclose_substring(word, trie) for word in word_list]


words = ["neuroses", "myopic", "sufficient", "televise", "coccidiosis",
    "gules", "during", "construe", "establish", "ethyl"]
parts = ["aaaaa", "Aaaa", "E", "z", "Zzzzz", "a", "mel", "lon", "el", "An",
    "ise", "d", "g", "wnoVV","i", "IUMc", "P", "KQ", "QfRz", "Xyj", "yiHS"]
print(findSubstrings(words, parts))
help(Trie)
