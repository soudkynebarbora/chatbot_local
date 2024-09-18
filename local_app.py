import streamlit as st
from local_chains import load_chain
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
import io
import base64



def message_sent_function():
    st.session_state.send_input = True
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

def main():
    st.set_page_config(page_title = "Walkie", page_icon="🤖")
    st.title("🤖 Walkie")

    #sidebar creation and design
    with st.sidebar:
        st.image("chat_icons\\robot.png")
        st.markdown("<h1 style='text-align:center;font-family: Helvetica;font-size:30px;'>Walkie, the Health Companion </h1>",
                    unsafe_allow_html=True)
        st.markdown("<h7 style='text-align: justify;font-family: Helvetica;font-size:25px;'> Hi, my name is Walkie. " 
                    "You can talk to me about your walking journey or just have a quick chat about weather. I am always here for you! </h7>", unsafe_allow_html=True)

    #chat initialisation
    chat_container = st.container()
    chat_history = StreamlitChatMessageHistory(key = "history") #logs llm output in history


    if "online_status" not in st.session_state:
        st.session_state.online_status = False
    
    if "write_size" not in st.session_state:
        st.session_state.write_size = "#### "

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""
        chat_history.add_ai_message("Hi, my name is Walkie. You can talk to me about your walking journey or just have a quick chat about weather. I am always here for you!")

    
    llm_chain = load_chain(chat_history)
    user_input = st.text_input(r"$\large\textsf{Write your message here:}$", key = "user_input", on_change=message_sent_function)

    send_button_column,voice_record_column, col3rand= st.columns([1,3,5]) 

    with send_button_column:  
        send_button = st.button(r"$\large\textsf{Send}$", key = "send_button", type="primary")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            with chat_container:
                with st.spinner(r"$\large\textsf{Thinking...}$"):
                    response = llm_chain.run(st.session_state.user_question)
                    st.session_state.user_question = ""

    if chat_history.messages != []:
        with chat_container:
            for message in chat_history.messages:
                st.chat_message(message.type).write(st.session_state.write_size + message.content)




if __name__ == "__main__":
    main()
