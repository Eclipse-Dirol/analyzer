import sys, os
import streamlit as st
from src.cleaner import Cleaners
from src.methods import Calculations
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.title("ANALYZER")
input_file = ["Upload file", "SQL", "FastAPI"]
file_list = [".txt", ".bin", ".csv"]
input_answer = st.selectbox("Select a file upload method", input_file)
if input_answer == "Upload file":
    file_answer = st.selectbox("Select file extension", file_list)
    if file_answer == ".txt":
        calculation = ["Select action","Count the number of words", "Calculate the average word length", "Calculate the sum of all letters", "Display the length of all words"]
        file = st.file_uploader("Upload file", type=".txt")
        try:
            text = file.read().decode("utf-8")
            c = Cleaners(text)
            last_template = c.process()
            cal = Calculations(last_template)
            all_calculation = cal.process()
            answer_action = st.selectbox("",calculation)
            if answer_action == "Count the number of words":
                st.write(all_calculation[0])
            if answer_action == "Calculate the average word length":
                st.write(all_calculation[1])
            if answer_action == "Calculate the sum of all letters":
                st.write(all_calculation[2])
            if answer_action == "Display the length of all words":
                st.write(all_calculation[3])
        except Exception as e:
            st.error(f"Ошибка: {e}")
        








    elif file_answer == ".bin":
        st.write("Now this methods is not currently supported.")
    elif file_answer == ".csv":
        st.write("Now this methods is not currently supported.")
elif input_answer == "SQL":
    st.write("Now this methods is not currently supported.")
elif input_answer == "FastAPI":
    st.write("Now this methods is not currently supported.")