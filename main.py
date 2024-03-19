import sys
import anagram
from pig_latin import translate
import levenshtein
import rhyme
import cats_does_countdown


def solve_anagram(word):
    potentials = anagram.find_anagram(word)
    print(f"found {len(potentials)} anagrams")
    print(f"WORD\tSCORE")
    for word in potentials:
        score = anagram.scrabble_score(word)
        print(f"{word}\t{score}")

def compute_distance(word1, word2):
    distance = levenshtein.distance(word1, word2)
    print(f"The Levenshtein distance between '{word1}' and '{word2}' is {distance}.")

def cats_conundrum():
    cats_does_countdown.conundrum()

def find_rhymes(word):
    nurhymes = rhyme.get_rhymes_for(word)
    print(f"Rhymes for {word = } are: {nurhymes}")

def pig_latin(word):
    print(f"try to translate {word}")
    # translation = pig_latin.translate(word) # why does pig_latin.translate(word) gives AttributeError?
    translation = translate(word)
    print(f"Pig latin for {word = } is: {translation}")

def main():
    available_modes = ["solve-anagram", "compute-distance", "cats-conundrum", "find-rhymes", "pig-latin"]
    if len(sys.argv) < 2:
            print(f"Usage: pipenv run python main.py <mode> <arguments>, modes are: {available_modes}")
            sys.exit(1)

    mode = sys.argv[1]
    arguments = sys.argv[2:]

    if mode == "solve-anagram":
        if len(arguments) != 1:
            print("Usage: pipenv run python main.py solve-anagram <word>")
            sys.exit(1)
        solve_anagram(arguments[0])
    elif mode == "compute-distance":
        if len(arguments) != 2:
            print("Usage: pipenv run python main.py compute-distance <word1> <word2>")
            sys.exit(1)
        compute_distance(arguments[0], arguments[1])
    elif mode == "cats-conundrum":
        cats_conundrum()
    elif mode == "find-rhymes":
        if len(arguments) != 1:
            print("Usage: pipenv run python main.py find-rhymes <word>")
            sys.exit(1)
        find_rhymes(arguments[0])
    elif mode == "pig-latin":
        if len(arguments) != 1:
            print("Usage: pipenv run python main.py pig-latin <word>")
            sys.exit(1)
        pig_latin(arguments[0])
    else:
        print("Invalid mode. Available modes: solve-anagram, compute-distance, cats-conundrum, find-rhymes, pig-latin")
        sys.exit(1)
 

if __name__ == "__main__":
    main()

