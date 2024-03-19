def distance(word1, word2):
    """
    Compute the Levenshtein distance between two words.
    How many characters must be changed to another character
    for the first word to be transformed into the second word.
    (Park, Cars) will yield a distance of 2; 1 for the swap of 'P' to 'C'
    and 1 more for the swap from 'k' to 's'. The middle 'ar' 
    is shared and thus contributes no value to the distance.
    """
    len_word1 = len(word1)
    len_word2 = len(word2)

    # Initialize a matrix to store the distances
    distances = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]
    # print(f"{distances=}")

    # Initialize the first row and column
    for i in range(len_word1 + 1):
        distances[i][0] = i
    for j in range(len_word2 + 1):
        distances[0][j] = j
    # print(f"{distances=}")

    # Compute the distances
    for i in range(1, len_word1 + 1):
        for j in range(1, len_word2 + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            distances[i][j] = min(
                distances[i - 1][j] + 1,  # Deletion
                distances[i][j - 1] + 1,  # Insertion
                distances[i - 1][j - 1] + cost  # Substitution
            )

    return distances[len_word1][len_word2]

