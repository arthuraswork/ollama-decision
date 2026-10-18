# ollama-decision

Python SDK for Ollama's Decision API (`/v1/systemone`). Convert text into structured, typed responses without prose generation.

## Installation

```bash
pip install ollama-decision
```

## Quick start

from ollama_decision import OllamaSystem1, noul_question, choice_question, score_question

model = OllamaSystem1('nimble-v3:9b-q4_K_M', timeout=30)

# Define questions
refund_q = noul_question('wants_refund', 'Does user demand a refund?')
intent_q = choice_question('intent', 'Request category?', {
    'billing': 'Payment issues',
    'technical': 'Bugs and errors',
    'other': 'Other'
})
sentiment_q = score_question('sentiment', 'Emotional tone', [
    'Negative', 'Neutral', 'Positive'
])

# Bind state and questions
model['ticket'] = "I want my money back, this is frustrating!"
model << ('ticket', refund_q) << ('ticket', intent_q) << ('ticket', sentiment_q)

# Execute
response = model('ticket')
print(response.json())

## Question types

Boolean question returning a probability (0.0 to 1.0).

`noul_question(name, instruction)`


```python
q = noul_question('is_urgent', 'Is this request urgent?')
# Returns: {"noul": 0.95}
```

Single selection from a dictionary of options.

`choice_question(name, instruction, criteria)`

```python
q = choice_question('department', 'Route to?', {
    'sales': 'New purchases',
    'support': 'Technical help',
    'billing': 'Payment issues'
})
# Returns: {"choice": "billing", "confidence": 0.87, "probabilities": {...}}
```

Ordered scale evaluation (must be sorted from lowest to highest).

`score_question(name, instruction, criteria)`

```python
q = score_question('priority', 'Priority level', [
    'Low', 'Medium', 'High', 'Critical'
])
# Returns: {"score": 2.3, "confidence": 0.78, "probabilities": {...}}
```

## OllamaSystem1 API

Methods & Operators

model = OllamaSystem1('nimble-v3:9b-q4_K_M') -- Constructor
model[state_name] = text -- Bind input text to a state name.
model << (state_name, question) -- Attach a question object to the specified state.
model(state_name) -- Execute the API request and return the HTTP response object.


## Supported Models

nimble-v3:9b-q4_K_M — Best for multilingual tasks and high accuracy.
tev1:4b — Fast English classification.
tev1:0.8b — Ultra-lightweight for constrained environments.
..etc

## License
MIT