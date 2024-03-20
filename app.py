from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from typing import List, Dict
from pig_latin import translate
import anagram
import levenshtein
import rhyme
import cats_does_countdown

app = FastAPI()

# def custom_openapi():
#     """Customize the swagger doc, mainly to 3.0.0"""
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi( # why does fastapi.openapi.utils give NameError: name 'get_openapi' is not defined?
#         title="Neo Cartagena",
#         version="0.0.1",
#         summary="This is a very custom OpenAPI schema",
#         description="Here's a longer description of the custom **OpenAPI** schema",
#         routes=app.routes,
#     )
#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema
# # apply the openapi customizations
# app.openapi = custom_openapi

class Word(BaseModel):
    word: str

class WordPair(BaseModel):
    word1: str
    word2: str

@app.get('/api/anagrams')
@app.post('/api/anagrams')
async def get_anagrams(word: Word) -> List[str]:
    anagrams = anagram.find_anagrams(word.word)
    print(f"received {word.word} and will return {anagrams}")
    return anagrams

@app.get('/api/scrabble')
@app.post('/api/scrabble')
async def get_scored_anagrams(word: Word) -> Dict[str, int]:
    scorecard = {}
    solutions = anagram.find_anagrams(word.word)
    for solution in solutions:
        score = anagram.scrabble_score(solution)
        scorecard.setdefault(solution, score)
        print(f"{solution}\t{score}")
    return scorecard

@app.get('/api/levenshtein')
@app.post('/api/levenshtein')
async def get_edit_distance(pair: WordPair) -> str:
    distance = levenshtein.distance(pair.word1, pair.word2)
    return str(distance)

@app.get('/api/rhymes')
@app.post('/api/rhymes')
async def get_rhymes(word: Word) -> List[str]:
    rhymes = rhyme.get_rhymes_for(word.word)
    return rhymes

@app.get('/api/piglatin')
@app.post('/api/piglatin')
async def translate_into_pig_latin(word: Word) -> str:
    translation = translate(word.word)
    return translation

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)

