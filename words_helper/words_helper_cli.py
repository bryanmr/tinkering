#!/usr/bin/python3
from collections import Counter
from pathlib import Path
import sys
from os.path import expanduser

if len(sys.argv) > 1:
    letters = sys.argv[1]
else:
    letters = input("Input your letters and we will make words:\n").lower()

try:
    dictionary = Path(expanduser('~')+'/words.txt').read_text().lower().splitlines()
except:
    try:
        dictionary = Path('/usr/share/dict/words').read_text().lower().splitlines()
    except:
        print('Dictionary not found at /usr/share/dict/words')
        print('Dictionary not found at '+expanuser('~')+'/words.txt')
        sys.exit()

def anagramSet(dictionary, letters):
    anagrams = set()
    lettersSet = set(letters)
    for word in dictionary:
        if lettersSet.issuperset(word):
            anagrams.add(word)
    return anagrams

def checkPossible(candidates, letters):
    listCandidates = list()
    lettersLength = len(letters)
    lettersCounter = Counter(letters)
    for candidate in candidates:
        candidateLength = len(candidate)
        if (candidateLength > 2 and candidateLength <= lettersLength and
        not Counter(candidate) - lettersCounter):
             listCandidates.append(candidate)
    return listCandidates

def orderPrint(output, letters):
    for i in range(3, len(letters)+1):
        print(i, "letters in the word")
        for word in output:
            if len(word) == i:
                print(word)

possibilities = anagramSet(dictionary, letters)
checked = checkPossible(possibilities, letters)
orderPrint(checked, letters)
