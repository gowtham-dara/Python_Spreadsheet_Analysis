" Analyzing Spreadsheet Data with Python"

import requests
import os

if not os.path.isfile("./Airport_Data.xlsx"):
    r = requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/analysing-spreadsheet-data-with-python/Airport_Data.xlsx")
    f = open("./Airport_Data.xlsx", mode = "wb+")
    f.write(r.content)
    f.close()

import pandas as pd

df_facilities = pd.read_excel("./Airport_Data.xlsx", sheet_name="Facilities") 

#types for aviation facilities in alaska 
df_facilities["Type"].unique() 

#provide a table containing the information for all seaplane base in alaska
df_facilities["Type"] == "SEAPLANE BASE"
print(df_facilities[df_facilities["Type"]=="SEAPLANE BASE"]) 

#the 5 highest aviation facilities in Alaska?
df_facilities.sort_values(by = "ARPElevation", ascending = False)
print(df_facilities.sort_values(by = "ARPElevation", ascending = False).head(n=5)) 

# the average elevation of aviation facilities?
print(df_facilities["ARPElevation"].mean())

# the highest and lowest elevation values of the aviation facilities? 
print(df_facilities["ARPElevation"].max()) 
print(df_facilities["ARPElevation"].min()) 

#Write to xlsx Files!
df_seaplane=df_facilities[df_facilities["Type"]=="SEAPLANE BASE"] 
df_seaplane.to_excel("./seaplane.xlsx",index=False)
