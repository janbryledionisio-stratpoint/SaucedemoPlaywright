# factory/excel_bean_factory.py
import pandas as pd

class ExcelLoader:
    def __init__(self, file_path="testdata.xlsx", sheet_name="Sheet1"):
        self.df = pd.read_excel(file_path, sheet_name=sheet_name)

    def __getattr__(self, name):
        matching_columns = [col for col in self.df.columns if col.lower() == name.lower()]
        if matching_columns:
            column_name = matching_columns[0]
            return lambda: self.df[column_name].tolist()
        else:
            raise AttributeError(f"No such column '{name}' in Excel")