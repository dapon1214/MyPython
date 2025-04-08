import pandas as pd

# version = pd.__version__
# print(version)

# 顯示所有欄位，不然預設只有幾個欄位
pd.set_option("display.max_columns", None)
# 顯示所有row
pd.set_option("display.max_rows", None)

titanic = pd.read_csv("data/titanic.csv")
# print(titanic.head())

ages = titanic['Age']
print(ages)

