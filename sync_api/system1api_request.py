from httpx import Client
from functools import reduce
import httpx


def questions2json(model: str, questions: list[dict], state: str) -> dict:
    return {
        'model': model,
        'state': state,
        'questions': questions[0] if len(questions) == 1 else reduce(lambda q1, q2: q1 | q2, questions)
    }


def request(body: dict, url: str = 'http://localhost:11434/v1/systemone', timeout=10, proxy=None) -> httpx.Response:
    headers = {
        'Content-Type': 'application/json'
        }
    
    with Client(timeout=timeout, proxy=proxy) as client:
        response = client.post(url, headers=headers, json=body)
        return response

