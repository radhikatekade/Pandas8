# Group by the unique subjects taught by each teacher, return the DF.

import pandas as pd
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    return df.rename(columns = {'subject_id': 'cnt'})