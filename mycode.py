import pandas as pd
import os

data={
    "Name":["Aman","Paru","Sharu"],
    "Age":[13,76,43],
    "city":["Knr","Clt","Tvm"]
}
df=pd.DataFrame(data)

dir="data"
os.makedirs(dir,exist_ok=True)

file_path=os.path.join(dir,"sample_data.csv")

df.to_csv(file_path,index=False)
print("Csv saved")