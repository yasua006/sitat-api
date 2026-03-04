from difflib import restore

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from random import choice, randint

app: FastAPI = FastAPI(title="LOTR Quotes")

quotes: dict[int, str] = {
    1: "sitaten er ikke tom",
    2: "det er Python språket",
    3: "det er en sitat"
}

class Quote(BaseModel):
    quote: str

@app.get("/sitat", response_model=Quote)
def quote():
    an_id: int = randint(1, len(quotes))
    return {"quote":quotes[an_id]}

@app.get("/sitat/total", response_model=Quote)
def quote_total():
    return {"antall:":len(quotes)}

@app.get("/sitat/random", response_model=Quote)
def quote_random():
    return {"random:":choice(quotes)}

@app.get("/sitat/random?mengde=%s", response_model=Quote)
def quote_random(amount: int):
    random_quotes = []

    for i in range(amount):
        random_quotes.append({f"random_{i}:": choice(quotes)})

    return random_quotes

@app.get("/sitat?id=%s", response_model=Quote)
def quote_id(an_id: int): # navn bytt grunn: "shadows built-in name" warning
    return {"quote":quotes[an_id]}

@app.get("/sitat/alle", response_model=Quote)
def quote_all():
    return {"alle:":quotes}

@app.get("/sitat?vis=%s", response_model=Quote)
def show_quote(an_id: int):
    return {"quote:":quotes[an_id]}