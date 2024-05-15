import streamlit as st
from speech_recognizer import SpeechRecognizer, Language_configuration
from chat_text import chatbot


st.title("Chatbot")
st.write("Hello! I'm a chatbot. Ask me anything about Principles of Chemistry.")

status = st.radio("Select Option: ", ('Input text', 'Record Audio'))
# Get the user's question
if status == 'Input text':
    question = st.text_input("Enter a question:")
    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        if response == '':
            st.error("Not related to Principles of Chemistry")
        else:
            st.success(response)
else:
    # Create an instance of SpeechRecognizer
    recognizer = SpeechRecognizer()

    # UI controls
    api = st.selectbox("Select API", ['google', 'wit', 'ibm'])
    language = st.selectbox('Language ', list(Language_configuration.keys()))

    language_code = Language_configuration.get(language)
    # Update recognizer settings
    recognizer.set_api(api)
    recognizer.set_language(language_code)

    # Transcribe speech on button click
    if st.button("Start Recording"):
        recognized_text = recognizer.transcribe_speech()
        if recognized_text != None:
            response = chatbot(recognized_text)
            if response == '':
                st.error("Not related to Principles of Chemistry")
            else:
                st.success('Chatbot: ' + response)

        
