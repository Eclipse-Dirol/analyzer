import pandas as pd

class Calculation_for_csv:
    def __init__(self, table):
        self.table = table
        self.col_name = self.column_definition()
        
    def column_definition(self) -> list:
        df = self.table
        col_name = list(df.columns)
        return col_name

    def csv_sum(self, column):
        return self.table[column].sum()
        
    def csv_min(self, column):
        return self.table[column].min()
    
    def csv_max(self, column):
        return self.table[column].max()
    
    def csv_mean(self, column):
        return self.table[column].mean().round(2)
    
    def list_columns(self):
        return self.col_name
        
    def count(self, column) -> tuple:
        sum_ = self.csv_sum(column)
        min_ = self.csv_min(column)
        max_ = self.csv_max(column)
        mean_ = self.csv_mean(column)
        return sum_, min_, max_, mean_