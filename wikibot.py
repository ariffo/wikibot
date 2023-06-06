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
    print('Ha ocurrido un error con el límite de consultas por minutos y/o tokens por minutos.')
    print(f'\n{e}')

except openai.error.InvalidRequestError as e:
    print('Ha ocurrido un error con tu consulta, está mal formulada o le faltan/sobran parámetros')
    print(f'\n{e}')

except openai.error.AuthenticationError as e:
    print('Ha ocurrido un error con tu key de autenticación, comprueba que sea válida')
    print(f'\n{e}')

except openai.error.ServiceUnavailableError	as e:
    print('Se produjo un error con los servidores de OpenAI')
    print(f'\n{e}')

except openai.error.APIConnectionError	as e:
    print('''Problemas con la conexión. Asegúrate que esté bien tu internet, no tengas una proxy o firewall
    que bloquee la conexión, o tengas problemas con los certificados SSL''')
    print(f'\n{e}')
