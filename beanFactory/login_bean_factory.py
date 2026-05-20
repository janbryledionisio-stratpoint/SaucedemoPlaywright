from utils.excel_loader import ExcelLoader

from utils.excel_loader import ExcelLoader  # adjust the import based on your project structure

class LoginBeanFactory:
    def __init__(self):
        self.BeanFactory = ExcelLoader(
            file_path="data/Saucedemo.xlsx",
            sheet_name="Login"
        )
        # Preload the data
        self.username = self.BeanFactory.Username()       # Locator names or labels
        self.password = self.BeanFactory.Password()
        self.error_message = self.BeanFactory.ErrorMessage()
        self.test_case_IDs = self.BeanFactory.TestID() # Test case IDs