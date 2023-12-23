import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

data = pd.DataFrame([[101, 3, 3], [2, 3, 3], [1, 4, 3], [2, 5, 3], [3, 5, 3]], columns=['student_id', 'email', 'age'])
print(data)
p = dropDuplicateEmails(data)
print(p)