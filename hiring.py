import pandas as pd
import numpy as np
from sklearn import linear_model
from word2number import w2n

d = pd.read_csv("book.csv")
d
#d.experience = d.experience.fillna("zero")
#d
d.experience = d.experience.apply(w2n.word_to_num)
d

import math
median_test_score = math.floor(d['test_score(out of 10)'].mean())
median_test_score

d['test_score(out of 10)'] = d['test_score(out of 10)'].fillna(median_test_score)
d

reg = linear_model.LinearRegression()
reg.fit(d[['experience','test_score(out of 10)','interview_score(out of 10)']],d['salary'])
reg.predict([[2,9,6]])
reg.predict([[12,10,10]])
