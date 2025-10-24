import sys, os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.cleaner import Cleaners
from src.methods import Calculations

def process(text):
    c = Cleaners(text)
    last_template = c.process()
    cal = Calculations(last_template)
    all_calculation = cal.process()
    return all_calculation
st.title("ANALYZER")
input_file = ["Upload file", "SQL", "FastAPI"]
file_list = ["Select format", ".txt", ".bin", ".csv"]
option = ["Count the number of words", "Calculate the average word length", 
"Calculate the sum of all letters", "Display the length of all words"]
input_file = st.radio("Select a file upload method", input_file)
st.write("Upload text without diacritics, they will not be recognized and the analysis will break.")
if input_file == "Upload file":
    col1, col2 = st.columns([2,1])
    col_1, col_2, col_3= st.columns([3,1,2])
    col_1_, col_2_ = st.columns([1,4])
    with col1:
        uploaded_file = st.file_uploader("Upload file", type=["txt"])
    with col2:
        if uploaded_file:
            file_action = st.radio("File action", ("Select action", "Process now", "See text"))
    if uploaded_file is not None and file_action == "Process now":
        raw = uploaded_file.read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("cp1251", errors="replace")
        st.session_state.raw_text = text
        with col_1:
            if st.session_state.raw_text:
                answer = st.radio("", option, key="result_radio")
        with col_2:
            if answer:
                submit = st.button("Execute")
        if submit:
            try:
                st.session_state.all_calc = process(st.session_state.raw_text)
            except Exception as e:
                st.session_state.all_calc = None
                st.error(f"Error during processing: {e}")
        with col_3:
            st.write("Answer:")
            if submit and st.session_state.all_calc:
                mapping = {
                    option[0]: st.session_state.all_calc[0],
                    option[1]: st.session_state.all_calc[1],
                    option[2]: st.session_state.all_calc[2],
                    option[3]: st.session_state.all_calc[3],
                }
                st.write(mapping.get(answer))
    elif uploaded_file is not None and file_action == "See text":
            with col_1_:
                show = st.button("Show text", key="show_text")
                if show:
                    raw = uploaded_file.read()
                    try:
                        text = raw.decode("utf-8")
                    except UnicodeDecodeError:
                        text = raw.decode("cp1251", errors="replace")
                    with col_2_:
                        st.write(text)
                        
elif input_file == "SQL":
    st.write("Now this methods is not currently supported.")
elif input_file == "FastAPI":
    st.write("Now this methods is not currently supported.") 