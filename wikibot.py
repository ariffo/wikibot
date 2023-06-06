import wikipedia
import openai
import os

openai.api_key = os.getenv('openai_api_key')

try:
    looking_for = input('¿Acerca de qué tema deseas saber?: ')

    wikipedia.set_lang('es')
    page = wikipedia.page(title=looking_for, auto_suggest=False).content[:1000]

    message = {'role': 'user', 'content': f'resúmeme el siguiente artículo: {page}'}
    messages = []
    messages.append(message)

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

    print(response.choices[0].message.content)


except openai.error.RateLimitError as e:
    print(e)

except openai.error.InvalidRequestError as e:
    print(e)
