from sync_api.payloads import noul_question, score_question, choice_question
from sync_api.model import OllamaSystem1
import json



state_en = "I have been trying to downgrade my Pro plan to Basic for the last three days, but the button is greyed out. I was charged $49 again today. This is extremely frustrating and I want my money back immediately."

q1_en = noul_question(
    name='wants_refund',
    instruction='Does the user explicitly demand a refund or return of funds?'
)

q2_en = choice_question(
    name='primary_intent',
    instruction='What is the main category of this user request?',
    criteria={
        'billing_issue': 'Problems with charges, payments, or refunds',
        'technical_bug': 'UI errors, broken features, or access issues',
        'account_management': 'Requests to change plan, upgrade, or cancel',
        'other': 'None of the above'
    }
)

q3_en = score_question(
    name='sentiment_level',
    instruction='Rate the emotional tone of the user message',
    criteria=[
        'Highly negative and angry',
        'Mildly frustrated or disappointed',
        'Neutral and factual',
        'Positive or satisfied'
    ]
)

state_ru = "Ищу позицию Middle Python разработчика. Есть 3 года коммерческого опыта, уверенно владею Django, FastAPI и PostgreSQL. На последнем месте работы внедрял Celery и Redis. Рассматриваю только полностью удаленный формат работы с оформлением по ТК РФ."

q1_ru = noul_question(
    name='has_redis_experience',
    instruction='Упоминает ли кандидат опыт работы с технологией Redis?'
)

q2_ru = choice_question(
    name='work_format_preference',
    instruction='Какой формат работы предпочитает кандидат?',
    criteria={
        'remote': 'Полностью удаленная работа',
        'office': 'Работа только в офисе',
        'hybrid': 'Гибридный формат',
        'unspecified': 'Формат не указан или не важен'
    }
)

q3_ru = score_question(
    name='seniority_level',
    instruction='Оцените заявленный уровень квалификации кандидата',
    criteria=[
        'Junior (менее 1 года опыта)',
        'Middle (1-3 года опыта)',
        'Senior (3-5 лет опыта)',
        'Lead (более 5 лет опыта)'
    ]
)


model = OllamaSystem1('nimble-v3:9b-q4_K_M', timeout=30)
model['EN_state'] =  state_en
model << ('EN_state', q1_en) << ('EN_state', q2_en) << ('EN_state', q3_en)

response = model('EN_state')

print(response.json())


model['RU_state'] =  state_ru
model << ('RU_state', q1_ru) << ('RU_state', q2_ru) << ('RU_state', q3_ru)

response = model('RU_state')

print(response.json())