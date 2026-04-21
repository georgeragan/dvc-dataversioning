import pandas as pd
import os

data={
    "Name":["Aman","Paru","Sharu"],
    "Age":[13,76,43],
    "city":["Knr","Clt","Tvm"]
}
df=pd.DataFrame(data)
new_row_loc={"Name":"Manu","Age":34,"city":"Tsr"}
df.loc[len(df.index)]=new_row_loc


dir="data"
os.makedirs(dir,exist_ok=True)

file_path=os.path.join(dir,"sample_data.csv")

df.to_csv(file_path,index=False)
print("Csv saved")