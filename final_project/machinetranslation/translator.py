import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    if englishText is None :
        return None
    response = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    if len(response['translations'])>0 :
        return response['translations'][0]['translation']
    return "Error"

def frenchToEnglish(frenchText):
    if frenchText is None :
        return None
    response = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    if len(response['translations'])>0 :
        return response['translations'][0]['translation']
    return "Error"
