import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students

data = pd.DataFrame([[101, 3, 3], [2, 3, 3], [1, 4, 3], [2, 5, 3], [3, 5, 3]], columns=['student_id', 'name', 'age'])
print(data)
p = renameColumns(data)
print(p)