import random

def conundrum():
    """
    Return a conundrum in the style of "8 out 10 Cats Does Countdown"
    These conundrums follow a familiar pattern.
    A lewd anagram:                             "rudenobs"
    A clue for the anagram and the answer:      "People like these after a break-up."
    And finally the answer:                     "rebounds"
    """
    # chatGPT really struggled to understand lewdness,
    # but was otherwise able to choose anagrams that
    # contain words themselves. chatGPT was unable to make 
    # hints that weren't obvious so I must write them myself.
    conundrums = {
        "ELEPHANT": ("NEATHELP","tbd"),
        "BREAKFAST": ("BAKEFARTS","tbd"),
        "WATERMELON": ("MENTALOWER","tbd"),
        "LAVENDER": ("LADREVEN","tbd"),
        "SUNFLOWER": ("FLOWNUSER","tbd"),
        "CHOCOLATE": ("COOLTEACH","tbd"),
        "FIREPLACE": ("PEACEFIRL","tbd"),
        "STRAWBERRY": ("WRYBREAST","tbd"),
        "WATERFALL": ("FEARWALT","tbd"),
        "MOONLIGHT": ("MIGHTLOON","tbd"),
    }

    words = list(conundrums.keys())
    random.shuffle(words)

    # Iterate over the shuffled list and prompt the user for the answer
    for word in words:
        # Get the anagram, hint pair
        anagram, hint = conundrums[word]

        # Print the anagram and hint
        print("Anagram:", anagram)
        print("Hint:", hint)

        # Prompt the user for their guess
        guess = input("Your answer: ").upper()

        # Check if the guess is correct
        if guess == word:
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is:{word}, \n")
        break # I don't really want to iterate over every puzzle
