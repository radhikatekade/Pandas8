# Group the classes that a student is attending and get the total count of classes. Return student DF who
# attend more than 5 classes.

import pandas as pd
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    return df[df['student'] >= 5][['class']]