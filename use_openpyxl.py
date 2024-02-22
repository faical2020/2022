import pandas as pd

# read the demo2.xlsx file
df=pd.read_excel("demo2.xlsx")

# appending the data of df after the data of demo1.xlsx
with pd.ExcelWriter("demo1.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
    df.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)