import speech_recognition as sr
import streamlit as st

Language_configuration = {
    "English (United States)": "en-US",
    "English (United Kingdom)": "en-GB",
    "Spanish (Spain)": "es-ES",
    "Spanish (Mexico)": "es-MX",
    "French (France)": "fr-FR",
    "French (Canada)": "fr-CA",
    "German (Germany)": "de-DE",
    "Italian (Italy)": "it-IT",
    "Japanese (Japan)": "ja-JP",
    "Chinese (Simplified, China)": "zh-CN",
    "Chinese (Traditional, Taiwan)": "zh-TW",
    "Russian (Russia)": "ru-RU",
    "Portuguese (Brazil)": "pt-BR",
    "Portuguese (Portugal)": "pt-PT",
    "Dutch (Netherlands)": "nl-NL",
    "Arabic (Egypt)": "ar-EG",
    "Korean (South Korea)": "ko-KR",
    "Swedish (Sweden)": "sv-SE",
    "Turkish (Turkey)": "tr-TR",
    "Polish (Poland)": "pl-PL"
}

class SpeechRecognizer:
    def __init__(self, api='google', language='en-US'):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.api = api
        self.language = language
        
    def set_language(self, language):
        self.language = language

    def set_api(self, api):
        self.api = api
        
    def transcribe_speech(self):
        if self.api == 'google':
            recognizer_func = sr.Recognizer().recognize_google
        elif self.api == 'wit':
            recognizer_func = sr.Recognizer().recognize_wit
        elif self.api == 'ibm':
            recognizer_func = sr.Recognizer().recognize_ibm
        else:
            raise ValueError("Unsupported API. Supported APIs are: 'google', 'wit', 'ibm'.")

        with self.microphone as source:
        
            st.info("Speak now...")
            
            self.recognizer.adjust_for_ambient_noise(source, duration=0.1)
            audio = self.recognizer.listen(source)
            st.info("Transcribing...")

            try:
               return recognizer_func(audio, key=None, language=self.language)
            except sr.UnknownValueError:
                st.error("Could not understand audio")
            except sr.RequestError as e:
                st.error("Error fetching results; {0}".format(e))
