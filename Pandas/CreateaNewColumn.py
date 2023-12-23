import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


data = pd.DataFrame([[1,3], [2,3], [1,4], [2, 5], [3,5]])
print(data)
data.columns.insert('bonus')
print(data)
