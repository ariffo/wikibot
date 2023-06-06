import wikipedia
import openai
import os

openai.api_key = os.getenv('openai_api_key')

try:
    looking_for = input('¿Acerca de qué tema deseas saber?: ')

    wikipedia.set_lang('es')
    page = wikipedia.page(title=looking_for, auto_suggest=False).content[:10000]

    message = {'role': 'user', 'content': f'lístame los 3 puntos principales del artículo: {page}'}
    messages = []
    messages.append(message)

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

    print(response.choices[0].message.content)


except openai.error.InvalidRequestError as e:
    print('Error con tu consulta, asegúrate que los parámetros estén bien\n')
    print(e)

except openai.error.AuthenticationError as e:
    print('Error al autenticarte. Revisa que la api key sea válida!\n')
    print(e)

except openai.error.RateLimitError as e:
    print('Error! Límite de consultas y/o token por minuto alcanzado!\n')
    print(e)

except openai.error.APIError as e:
    print('Error! Ah ocurrido un problema con la api de OpenAi\n')
    print(e)

except openai.error.Timeout as e:
    print('Error! Timeout en el request\n')
    print(e)

except openai.error.APIConnectionError as e:
    print('Error! Revisa tu conexión a internet, proxys, firewall, etc.\n')
    print(e)

except openai.error.ServiceUnavailableError as e:
    print('Error! Problemas con el servidor de OpenAI!\n')
    print(e)
