import sys, os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from frontend.read_downloaded_file import FileReader
from function_file_app import Function_file
from src.methods_for_csv import Calculation_for_csv

class AnalyzerApp:
    def __init__(self):
        st.title("ANALYZER")
        st.write("Upload text without diacritics, they will not be recognized and the analysis will break.")
        self.input_methods = ["Upload file", "SQL", "FastAPI"]
        self.file_types = [".txt", ".bin", ".csv"]
        self.mapping = {}
        
    def run(self):
        
        
        col1, col2 = st.columns([2, 1])
        col_1, col_2, col_3 = st.columns([3, 1, 2])
        col_1_, col_2_ = st.columns([1, 4])
        col_1_csv, col_2_csv, col_3_csv, col_4_csv = st.columns([2, 1, 1, 2])
        
        
        
        with col1:
            input_method = st.radio("Select a file upload method", self.input_methods)
        if input_method == "Upload file":
            with col2:
                select_file_type = st.radio("Select file type", self.file_types)
            if select_file_type == ".txt":
                options = [
			    "Count the number of words",
                "Calculate the average word length",
                "Calculate the sum of all letters",
                "Display the length of all words"
		        ]
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
                        func = Function_file(st.session_state.raw_text)
                        methods = func.process(select_file_type)
                    except Exception as e:
                        st.error(f"Error: {e}")
                        return
                    with col_1:
                        if 'raw_text' in st.session_state:
                            answer = st.radio("",options , key="result_radio")
                    with col_2:
                        if answer:
                            submit = st.button("Execute")
                    if submit:
                        try:
                            st.session_state.methods = methods
                            self.mapping = dict(zip(options, methods))
                        except Exception as e:
                            st.session_state.all_calc = None
                            st.error(f"Error during processing: {e}")
                    with col_3:
                        st.write("Answer:")
                        if 'methods' in st.session_state and st.session_state.methods and submit:
                            st.write(self.mapping.get(answer))
                elif uploaded_file and file_action == "See text":
                    with col_1_:
                        show = st.button("Show text", key="show_text")
                        if show:
                            reader = FileReader(file_type=select_file_type)
                            text = reader.read(uploaded_file)
                            with col_2_:
                                st.write(text)  
                            
                            
                            
                            
                            
            elif select_file_type == ".csv":
                csv_options = ["sum", "min", "max", "mean"]
                with col1:
                    uploaded_file = st.file_uploader("Upload file", type=["csv"])
                with col2:
                    if uploaded_file is not None:
                        file_action = st.radio("File action", ("Select action", "Process now", "See table"))
                if uploaded_file is not None and file_action == "Process now":
                    reader = FileReader(file_type=select_file_type)
                    try:
                        table = reader.read(uploaded_file)
                        func = Function_file(table)
                        cal = Calculation_for_csv(table)
                        check = func.process(select_file_type)
                    except Exception as e:
                        st.error(f"Error: {e}")
                        return
                    with col_1_csv:
                        columns = cal.column_definition()
                        col_csv = st.selectbox("", columns)
                        if col_csv:
                            methods = cal.count(column=col_csv)
                            self.mapping = dict(zip(csv_options, methods))
                    with col_2_csv:
                        answer_csv = st.radio("Select action", csv_options)
                    with col_3_csv:
                        button = st.button("Execute")
                    with col_4_csv:
                        st.write("Answer:")
                        if col_csv and answer_csv and button and table is not None:
                            st.write(self.mapping.get(answer_csv))
                            
                            
                            
                                
                elif uploaded_file and file_action == "See table":
                    with col_1_:
                        show = st.button("Show table", key="show_table")
                        if show:
                            reader = FileReader(file_type=select_file_type)
                            table = reader.read(uploaded_file)
                            with col_2_:
                                st.table(table)
                
                
                
                
                
                
                
                
                
                
                
                
                
            else:
                st.write("This file type is not currently supported.")
        else:
            st.write("This method is not currently supported.")
            
if __name__ == "__main__":
    app = AnalyzerApp()
    app.run()