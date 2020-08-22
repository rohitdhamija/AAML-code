import pandas as pd 
df = pd.read_csv("../input/cat_train_folds.csv")
print(df.kfold.value_counts())
print(df[df.kfold==0].target.value_counts())
print(df[df.kfold==1].target.value_counts())
print(df[df.kfold==2].target.value_counts())
print(df[df.kfold==3].target.value_counts())
print(df[df.kfold==4].target.value_counts())