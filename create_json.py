import json
from pathlib import Path


first= input("enter value")
second=input("enter value ")
third=input("enter value")
four=input("enter value")
five=input("enter value")

data ={
    'first': input of first,
    'second': input of second ,
    'third': input of third  ,
    'four': input of four  ,
    'five': input of five,    
	}

with open(sname+".json","w") as write_file:
    json.dump(data,write_file,indent=1)

printf("Json file is created")
