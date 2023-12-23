import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


data = pd.DataFrame([[1,3], [2,3], [1,4], [2, 5], [3,5]])