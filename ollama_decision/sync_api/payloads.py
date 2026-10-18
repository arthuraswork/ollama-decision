from functools import reduce

def noul_question(
        name: str,
        instruction: str,
        ) -> dict:

    return {
        name: {
            'type': 'noul',
            'instructions': instruction, 
            'criteria': {}
        }
    }

def choice_question(
        name: str,
        instruction: str,
        criteria: list[dict] | dict
        ) -> dict:
    return {
        name: {
            'type': 'choice',
            'instructions': instruction, 
            'criteria': reduce(lambda o1, o2: o1 | o2, criteria) if isinstance(criteria, list) else criteria
        }
    }

def score_question(
        name: str,
        instruction: str,
        criteria: list[str]
        ):

    return {
        name: {
            'type': 'score',
            'instructions': instruction, 
            'criteria': criteria
        }
    }


    