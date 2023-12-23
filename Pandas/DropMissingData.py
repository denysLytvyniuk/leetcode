import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students)[students['name'].notnull()]


data = pd.DataFrame([[101, 3, 3], [2, 3, 3], [1, 4, 3], [2, 5, 3], [3, 5, 3]], columns=['student_id', 'name', 'age'])
print(data)
p = dropMissingData(data)
print(p)