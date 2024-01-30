import json
from hitlist import Casino 
with open("casino.json","r") as f:
    content=f.read() 
    data=json.loads(content)
for tabled in data:
    table=Casino.Table(tabled['dealer'],tabled['players'])
    if table.search("Emma Smith"):
        print('WE FOUND HIM!'+tabled['dealer'])
    else:
        print('Unfortunately, he is not here 🥺'+tabled['dealer'])