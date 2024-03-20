import sys
import anagram
from pig_latin import translate
import levenshtein
import rhyme
import cats_does_countdown


def solve_anagram(word: str) -> list[str]:
    potentials = anagram.find_anagrams(word)
    return potentials

def compute_distance(word1: str, word2: str) -> int:
    distance = levenshtein.distance(word1, word2)
    return distance

def cats_conundrum() -> None:
    cats_does_countdown.conundrum()

def find_rhymes(word: str) -> list[str]:
    rhymes = rhyme.get_rhymes_for(word)
    return rhymes

def pig_latin(word: str) -> str:
    # translation = pig_latin.translate(word) # why does pig_latin.translate(word) gives AttributeError?
    translation = translate(word)
    return translation

def main() -> None:
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
        solutions = solve_anagram(arguments[0])
        print(f"found {len(solutions)} anagrams")
        print(f"WORD\tSCORE")
        for word in solutions:
            score = anagram.scrabble_score(word)
            print(f"{word}\t{score}")
    elif mode == "compute-distance":
        if len(arguments) != 2:
            print("Usage: pipenv run python main.py compute-distance <word1> <word2>")
            sys.exit(1)
        word1 = arguments[0]
        word2 = arguments[1]
        distance = compute_distance(word1, word2)
        print(f"The Levenshtein distance between '{word1}' and '{word2}' is {distance}.")
    elif mode == "cats-conundrum":
        cats_conundrum()
    elif mode == "find-rhymes":
        if len(arguments) != 1:
            print("Usage: pipenv run python main.py find-rhymes <word>")
            sys.exit(1)
        word = arguments[0]
        rhymes = find_rhymes(word)
        print(f"Rhymes for {word} are: {rhymes}")
    elif mode == "pig-latin":
        if len(arguments) != 1:
            print("Usage: pipenv run python main.py pig-latin <word>")
            sys.exit(1)
        word = arguments[0]
        translation = pig_latin(word)
        print(f"Pig latin for {word} is: {translation}")
    else:
        print("Invalid mode. Available modes: solve-anagram, compute-distance, cats-conundrum, find-rhymes, pig-latin")
        sys.exit(1)
 

if __name__ == "__main__":
    main()

