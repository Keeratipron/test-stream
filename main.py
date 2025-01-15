import streamlit as st

from pathlib import Path
import streamlit_authenticator as stauth
import yaml
import streamlit as st
from yaml.loader import SafeLoader
from utill.function import convert_json_to_yaml
from streamlit_authenticator.utilities import (CredentialsError,
                                               ForgotError,
                                               Hasher,
                                               LoginError,
                                               RegisterError,
                                               ResetError,
                                               UpdateError)


# Loading config file
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# --test--
# input_json = "utill/test-users.json"
# output_yaml = "utill/test-data.yaml"
# convert_json_to_yaml(input_json, output_yaml)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Creating a login widget
try:
    authenticator.login()
except LoginError as e:
    st.error(e)

# Authenticating user
if st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')

elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')

elif st.session_state['authentication_status']: 
    # st.write(f'Welcome *{st.session_state["name"]}*')
    # st.sidebar.write(f'{st.session_state["name"]}')
    with st.sidebar:
        menu = st.popover(f'{st.session_state["name"]}')
        menu.markdown("###### Line1")
        menu.markdown("###### Line2")
        menu.markdown("###### Line3")
        menu.markdown("###### Line4")
        menu.markdown("###### Line5")
        menu.markdown("###### Line6")
        menu.markdown("###### Line7")
 
    authenticator.logout('Logout', 'sidebar')

    pages = {
        "CREATE": [
            st.Page("views/1_texttospeech.py", title="Text to Speech", icon=":material/font_download:"),
            st.Page("views/2_voicechanger.py", title="Voice Changer", icon=":material/record_voice_over:"),
            st.Page("views/3_voices.py", title="Voices", icon=":material/graphic_eq:"),
            st.Page("views/4_soundeffects.py", title="Sound Effects", icon=":material/air:"),
            st.Page("views/14_Speech_to_text.py", title="Speech to Text", icon=":material/mic:"),
        ],
        "CONVERSATIONAL": [
            st.Page("views/5_agents.py", title="Agents", icon=":material/headset_mic:"),
            st.Page("views/6_conversations.py", title="Conversations", icon=":material/forum:"),
            st.Page("views/7_phonenumbers.py", title="Phone Numbers", icon=":material/call:"),
        ],
        # "WORKFLOWS": [
        #     st.Page("views/8_projects.py", title="Projects", icon=":material/collections_bookmark:"),
        #     st.Page("views/9_voiceover_studio.py", title="Voiceover Studio", icon=":material/radio:"),
        #     st.Page("views/10_dubbing_studio.py", title="Dubbing Studio", icon=":material/translate:"),
        #     st.Page("views/11_audio_native.py", title="Audio Native", icon=":material/volume_down:"),
        # ],
        # "TOOLS": [
        #     st.Page("views/12_voice_isolator.py", title="Voice Isolator", icon=":material/contactless:"),
        #     st.Page("views/13_ai_speech_classifier.py", title="AI Speech Classifier", icon=":material/branding_watermark:"),
        # ],
    }

    pg = st.navigation(pages)
    pg.run()





