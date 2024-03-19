# NeoCartagena
A motley trove of word algorithms I've enjoyed.

qrtḥdšt = carthago = new town

carthago nova = cartagena = new new town

neo cartagena = new new new town



## Setup
Requires `pipenv`

```
pip install --user pipenv;
pipenv install;
```

## Usage
```
pipenv run python ./main.py <mode> <args>
```

## Modes

### solve-anagram
```
pipenv run python ./main.py solve-anagram <word>
```
Solve an anagram and provide a scrabble score for each solution.
TODO: fix grinding slowness for larger words
TODO: consider a scrabble dictionary for scoring and far less noisy dictionary for general purpose

### compute-distance
```
pipenv run python ./main.py compute-distance <word1> <word2>
```
Compute the edit distance (Levenshtein distance) between two words.

### cats-conundrum
```
pipenv run python ./main.py cats-conundrum
```
Solve an anagram in the style of a conundrum from "8 out of 10 Cats Does Countdown"
TODO: Write clues that are relevant to both the anagram and the solution.


### find-rhymes
```
pipenv run python ./main.py find-rhymes <word>
```
Find words that rhyme with the input word.
TODO: More nuanced rhymes are needed than last 2 phonetics, because words like `toxic` and `taco` give too much noise while short words like `stirred` seem to do well.

### pig-latin
```
pipenv run python ./main.py pig-latin <word>
```
Translate the input word into pig latin.
TODO: use the phonetics stuff from rhyming to translate words beginning with digraphs like `charlie` and `phoebe` into `arliechay` and `oebephay` instead of `harliecay` and `hoebepay`


### quick run
```
pipenv run python ./main.py solve-anagram bird
pipenv run python ./main.py compute-distance bird taco
 pipenv run python ./main.py find-rhymes bird
pipenv run python ./main.py pig-latin bird
pipenv run python ./main.py cats-conundrum

```