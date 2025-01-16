import streamlit as st

# Load secrets from secrets.toml
USERS = st.secrets["user_credentials"]

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "login_error" not in st.session_state:
    st.session_state.login_error = False
if "username_input" not in st.session_state:
    st.session_state.username_input = ""
if "password_input" not in st.session_state:
    st.session_state.password_input = ""

# Login function
def handle_login():
    username = st.session_state.username_input
    password = st.session_state.password_input
    if username == USERS["username"] and password == USERS["password"]:
        st.session_state.logged_in = True
        st.session_state.login_error = False
        
    else:
        st.session_state.login_error = True

# Logout function
def handle_logout():
    st.session_state.logged_in = False
    
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

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
}
# App logic
    
if st.session_state.logged_in:
    # Main Page (Logged-in content)
    st.set_page_config(initial_sidebar_state="expanded")
    with st.sidebar:
        menu = st.popover(f'{USERS["name"]}')
        menu.markdown("###### Line1")
        menu.markdown("###### Line2")
        menu.markdown("###### Line3")
        menu.markdown("###### Line4")
        menu.markdown("###### Line5")
        menu.markdown("###### Line6")
        menu.markdown("###### Line7")
    st.sidebar.button("Logout", on_click=handle_logout)  # Logout button in sidebar
    # st.title("Welcome to the Dashboard!")
    # st.write("You are logged in.")
    
    pg = st.navigation(pages)
    pg.run()

elif not st.session_state.logged_in:
    st.set_page_config(initial_sidebar_state="collapsed")
    # Login Page
    st.title("Login")

    # Input fields
    username = st.text_input("Username", key="username_input", on_change=handle_login)
    password = st.text_input("Password", type="password", key="password_input", on_change=handle_login)

    # Button to login (optional for manual click)
    st.button("Login", on_click=handle_login)

    # Show error message if login fails
    if st.session_state.login_error:
        st.error("Invalid username or password!")
