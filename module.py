'''g4f lib'''
from g4f.client import Client
from g4f.cookies import set_cookies
import g4f
from g4f.Provider import RetryProvider
from g4f.Provider import (
    Aichatos,
    DuckDuckGo,
    Ecosia
)

'''gpt answer question funtion'''
def gpt_answer(message):
    client_many_providers = Client(
        provider = RetryProvider([
            DuckDuckGo,
            # Aichatos,
            # Ecosia,
        ])
    )
    
    response = client_many_providers.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    
    return response.choices[0].message.content

'''find image with gemini'''
def gemini_image_answer(prompt):
    set_cookies(".google.com", {
      "__Secure-1PSID": "<Your cookie>",
      "__Secure-1PSIDTS": "<Your cookie>"
    })

    client_gemini = Client()

    response = client_gemini.images.generate(
      model="gemini",
      prompt=prompt,
    )

    image_url = response.data[0].url
    return image_url


'''translate'''
from googletrans import Translator

def translate_vietnamese_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='vi', dest='en')
    return translation.text