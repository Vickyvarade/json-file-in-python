import json
from pathlib import Path


sname= input("enter scraper name:- ")
url=input("enter url:- ")
xp=input("enter xpath:-")
next_b=input("enter next xpath:-")
no_row=input("no. of cols:-")

data ={
    'scraper_name':sname,
    'url':url,
    'xp':xp,
    'next_b':next_b,
    'no_row': no_row,    
	}

with open(sname+".json","w") as write_file:
    json.dump(data,write_file,indent=1)

printf("Json file is created")
