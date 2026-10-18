from dataclasses import dataclass
from typing import Literal
from sync_api import request, questions2json
from sync_api.__consts import DecisionModel
import httpx

@dataclass
class OllamaSystem1:
    model: str | DecisionModel
    url:   str = 'http://localhost:11434/v1/systemone'
    timeout: float = 10.
    states: None | dict = None


    def __setitem__(self, name: str, state_text: str):
        if not self.states:
            self.states = {}
        self.states[name] = ([], state_text)
        return self
    
    def append_state(self, state_name, question: dict):
        self.states[state_name][0].append(question)

    def __lshift__(self, state_name_question: tuple[str, str]):
        """
        model << ('state', *_question(...))
        """
        self.append_state(*state_name_question)
        return self

    def __getitem__(self, state_name: str):
        return self.states.get(state_name)

    def __call__(self, state_name: str):
        return self.chat(state_name)

    def chat(self, state_name: str) -> httpx.Response:
        if state_name in self.states:
            body = questions2json(self.model, *self.states.get(state_name))
            try:
                response = request(body=body, url=self.url, timeout=self.timeout)
                return response
            except httpx.TimeoutException as te:
                raise te # Maybe set timeout bigger?
            except Exception as e:
                raise e
        raise Exception(f'Not found state {state_name}; Use model[{state_name}] = `state-text`')

