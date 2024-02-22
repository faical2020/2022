import pandas as pd

# Reading the demo1.xlsx
df1=pd.read_excel("demo1.xlsx")

# reading the demo2.xlsx
df2=pd.read_excel("demo2.xlsx")

# appending df2 after df1
# df3=df1.append(df2)  
# append method will be deprecated in future version
# so we will use concat method
df3=pd.concat([df1,df2])

# creating a new excel file and save the data
df3.to_excel("demo3.xlsx",index=False)