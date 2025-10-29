import sys, os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.cleaner import Cleaners
from src.methods_for_text import Calculations
from src.methods_for_csv import Calculation_for_csv

class Function_file:
    def __init__(self, file):
        self.file = file
    
    def process(self, suffix):
        if suffix == ".txt":
            c = Cleaners(self.file)
            last_template = c.process()
            cal = Calculations(last_template)
            all_calculation = cal.process()
            return all_calculation
        elif suffix == ".csv":
            cal = Calculation_for_csv(self.file)
            list_columns = cal.list_columns()
            return list_columns
        
    