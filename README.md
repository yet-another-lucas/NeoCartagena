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
pipenv install --dev;
```
Pipenv based to minimize system python interference.

## Usage
```
pipenv run mypy ./*.py                      # typechecker
pipenv run python ./main.py <mode> <args>   # cli
pipenv run uvicorn app:app --reload         # fastapi server
```
Command line and rest interfaces.

## API Documentation
```
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/openapi.json
```
Swagger and redoc came for free with fastAPI.

## Testing
```
pipenv run st run --checks all --experimental=openapi-3.1 --hypothesis-max-examples=10 http://127.0.0.1:8000/openapi.json
```
Based on schemathesis (the `run st` bit)

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
pipenv run python ./main.py solve-anagram bird;
pipenv run python ./main.py compute-distance bird taco;
pipenv run python ./main.py find-rhymes bird;
pipenv run python ./main.py pig-latin bird;
pipenv run python ./main.py cats-conundrum;

curl -X POST http://127.0.0.1:8000/api/anagrams     -d '{"word": "bird"}' -H "Content-Type: application/json";
curl -X POST http://127.0.0.1:8000/api/scrabble     -d '{"word": "bird"}' -H "Content-Type: application/json";
curl -X POST http://127.0.0.1:8000/api/levenshtein  -d '{"word1": "bird", "word2": "taco"}' -H "Content-Type: application/json";
curl -X POST "http://127.0.0.1:8000/api/levenshtein" -d '{"word1": "bird", "word2": "taco"}' -H "Content-Type: application/json";
curl -X POST http://127.0.0.1:8000/api/rhymes       -d '{"word": "bird"}' -H "Content-Type: application/json";
curl -X POST http://127.0.0.1:8000/api/piglatin     -d '{"word": "bird"}' -H "Content-Type: application/json";
```
