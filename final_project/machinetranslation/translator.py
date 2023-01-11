"""
    Text Translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
lt = LanguageTranslatorV3(version="2018-05-01", authenticator=IAMAuthenticator(apikey))
lt.set_service_url(url)

def englishToFrench(englishText):
    """
    Translates english text to french.
    """
    model_id='en-fr'
    translation = lt.translate(text=englishText, model_id=model_id).get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText
def frenchToEnglish(frenchText):
    """
    Translates french text to english.
    """
    model_id='fr-en'
    translation = lt.translate(text=frenchText, model_id=model_id).get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
