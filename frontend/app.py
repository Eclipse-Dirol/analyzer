import sys, os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.cleaner import Cleaners
from src.methods import Calculations
from frontend.read_downloaded_file import FileReader

def process(text):
    c = Cleaners(text)
    last_template = c.process()
    cal = Calculations(last_template)
    all_calculation = cal.process()
    return all_calculation

class AnalyzerApp:
    def __init__(self):
        st.title("ANALYZER")
        st.write("Upload text without diacritics, they will not be recognized and the analysis will break.")
        self.input_methods = ["Upload file", "SQL", "FastAPI"]
        self.file_types = [".txt", ".bin", ".csv"]
        self.options = [
			"Count the number of words",
			"Calculate the average word length",
			"Calculate the sum of all letters",
			"Display the length of all words"
		]
        self.mapping = {}
    def run(self):
        col1, col2 = st.columns([2, 1])
        col_1, col_2, col_3 = st.columns([3, 1, 2])
        col_1_, col_2_ = st.columns([1, 4])
        with col1:
            input_method = st.radio("Select a file upload method", self.input_methods)
        if input_method == "Upload file":
            with col2:
                select_file_type = st.radio("Select file type", self.file_types)
            if select_file_type == ".txt":
                with col1:
                    uploaded_file = st.file_uploader("Upload file", type=["txt"])
                with col2:
                    if uploaded_file is not None:
                        file_action = st.radio("File action", ("Select action", "Process now", "See text"))
                    
                if uploaded_file is not None and file_action == "Process now":
                    reader = FileReader(file_type=select_file_type)
                    try:
                        text = reader.read(uploaded_file)
                        st.session_state.raw_text = text
                    except Exception as e:
                        st.error(f"Error: {e}")
                        return
                    with col_1:
                        if 'raw_text' in st.session_state:
                            answer = st.radio("", self.options, key="result_radio")
                    with col_2:
                        if answer:
                            submit = st.button("Execute")
                    if submit:
                        try:
                            all_calc = process(st.session_state.raw_text)
                            st.session_state.all_calc = all_calc
                            self.mapping = dict(zip(self.options, all_calc))
                        except Exception as e:
                            st.session_state.all_calc = None
                            st.error(f"Error during processing: {e}")
                    with col_3:
                        st.write("Answer:")
                        if 'all_calc' in st.session_state and st.session_state.all_calc and submit:
                            st.write(self.mapping.get(answer))
                elif uploaded_file and file_action == "See text":
                    with col_1_:
                        show = st.button("Show text", key="show_text")
                        if show:
                            reader = FileReader(file_type=select_file_type)
                            text = reader.read(uploaded_file)
                            with col_2_:
                                st.write(text)
            else:
                st.write("This file type is not currently supported.")
        else:
            st.write("This method is not currently supported.")
            
if __name__ == "__main__":
    app = AnalyzerApp()
    app.run()