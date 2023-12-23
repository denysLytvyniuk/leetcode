import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]


data = pd.DataFrame([[101, 3, 3], [2, 3, 3], [1, 4, 3], [2, 5, 3], [3, 5, 3]], columns=['student_id', 'name', 'age'])
print(data)
p = selectData(data)
print(p)