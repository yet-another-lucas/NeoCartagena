import itertools

FILENAME="words.txt"

def find_anagram(input_word: str) -> list[str]:
    """
    Return all anagrams for the input word.

    """
    if len(input_word) > 6:
        print(f"words longer than 6 chars are slooooow, skipping {input_word=}")
        return list()
    # Generate all spelling permutations of the input word
    input_permutations = ["".join(x) for x in itertools.permutations(input_word)]
    # create an empty list to store the anagrams
    anagrams = []
    # open the file
    with open(FILENAME) as f:
        # read the file
        lines = f.read()
        # split the file into a list of words
        words = lines.split()
        # loop through the list of words
        for word in words:
            for permutation in input_permutations:
                if permutation.__contains__(word):
                    anagrams.append(word)
                    break
                    # print(f"{permutation} contains {word}")
    return list(set(anagrams))

def scrabble_score(word: str) -> int:
    """
    Calculate the Scrabble score for a given word.
    """
    # Define the letter scores according to Scrabble rules
    letter_scores = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
        'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
        'y': 4, 'z': 10
    }

    # Convert the word to lowercase for case insensitivity
    word = word.lower()

    # Calculate the score for the word
    score = 0
    for letter in word:
        score += letter_scores.get(letter, 0)  # Add the score of each letter, default to 0 if not found

    return score
