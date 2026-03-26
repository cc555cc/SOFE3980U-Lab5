import pandas as pd
import great_expectations as gx

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
                 names=["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
                        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
                        "hours-per-week", "native-country", "income"])

df.head()

def main ():
    