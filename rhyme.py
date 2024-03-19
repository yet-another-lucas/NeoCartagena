import os
import pickle
import nltk
from nltk.corpus import cmudict

def get_rhymes_for(input_word):
    """
    Rhymetime: take in input word and return the rhymes.
    Break up the word into syllables and find other words
    that match the final syllable. 
    """
    le_phonetical = get_phonetic_representation(input_word)
    return find_rhyming_words_with_phonetic_representation(input_word, le_phonetical)


def get_phonetic_representation(word):
    """
    Get the phonetic representation of a word using the CMU Pronouncing Dictionary.
    """
    # Convert the word to lowercase for consistency
    word = word.lower()
    
    # Check if the word is in the dictionary
    import pickle

    # Load the pronouncing dictionary from the local file
    with open('pronouncing_dict.pickle', 'rb') as f:
        pronouncing_dict = pickle.load(f)

    # Now you can use the pronouncing dictionary as before
    if word in pronouncing_dict:
        return pronouncing_dict[word][0] # pop [['c', 'a', 't']] into ['c', 'a', 't']
    else:
        return None

def find_rhyming_words_with_phonetic_representation(word, phonetic_representation):
    """
    Find words in the CMU Pronouncing Dictionary that rhyme with the given word
    based on the provided phonetic representation.
    """
    rhyming_words = []

    # Load the pronouncing dictionary from the local file
    with open('pronouncing_dict.pickle', 'rb') as f:
        pronouncing_dict = pickle.load(f)

    # Check each word in the dictionary,
    for dict_word, dict_phonetic_repr_nested in pronouncing_dict.items():
        dict_phonetic_repr = dict_phonetic_repr_nested[0] # pop [['c', 'a', 't']] into ['c', 'a', 't']
        # if ["third","stirred","blurred",].__contains__(dict_word ):
        #     print(f"{dict_word=} has {dict_phonetic_repr=}")
        #     print(f"{word=} has {phonetic_representation=}")
        #     print(f"{dict_phonetic_repr[-2:]=} and {phonetic_representation[-2:]=}")
        #     print(f"{dict_phonetic_repr[-1]=} and {phonetic_representation[-1]=}")
        #     print(f"{dict_phonetic_repr[-2:] == phonetic_representation[-2:]}")

        # Skip words that don't have the same last phonemes as the target word
        if dict_phonetic_repr[-2:] == phonetic_representation[-2:] and dict_word != word:
            rhyming_words.append(dict_word)

    return rhyming_words

#TODO: save pronunciations as ['c', 'a', 't'] instead of [['c', 'a', 't']]
# then get rid of the result[0] dance that does it elsewhere
def download_dictionary():
    # Download the CMU Pronouncing Dictionary if you haven't already
    nltk.download('cmudict')

    # Load the CMU Pronouncing Dictionary
    pronouncing_dict = nltk.corpus.cmudict.dict()

    # Save the pronouncing dictionary to a local file using pickle
    with open('pronouncing_dict.pickle', 'wb') as f:
        pickle.dump(pronouncing_dict, f)