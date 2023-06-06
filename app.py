import openai
import os

openai.api_key = os.getenv('openai_api_key.')

try:
    message = {'role': 'user', 'content': 'cuanta gente vive en el mundo?', 'hola': 'amigo'}
    messages = []
    messages.append(message)

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

    print(response.choices[0].message.content)

except openai.error.AuthenticationError as e:
    print('Error con la autenticación! Comprueba que la api key aún sea válida.\n')
    print(e)

except openai.error.InvalidRequestError as e:
    print('Error, resquest no válida. Revisa que estés enviando los parámetros adecuados')

