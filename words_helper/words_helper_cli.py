#!/usr/bin/python3
from collections import Counter
from pathlib import Path

dictionary = Path('/usr/share/dict/american-english').read_text().lower().splitlines()

letters = input("Input your letters and we will make words:\n")
letters = letters.lower()

def anagramSet(letters, dictionary):
    listOfLetters = list(letters)
    anagrams = set()
    for word in dictionary:
        if set(listOfLetters).issuperset(word):
            anagrams.add(word)
    return anagrams

def checkPossible(candidates, letters):
    listCandidates = list()
    for candidate in candidates:
        if (len(candidate) > 2 and len(candidate) <= len(letters) and
        not Counter(candidate) - Counter(letters)):
             listCandidates.append(candidate)
    return listCandidates

def orderPrint(output, letters):
    for i in range(3, len(letters)+1):
        print(i, "letters in the word")
        for word in output:
            if len(word) == i:
                print(word)

possibilities = anagramSet(letters, dictionary)
checked = checkPossible(possibilities, letters)
orderPrint(checked, letters)
