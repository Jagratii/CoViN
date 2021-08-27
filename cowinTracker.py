import requests
import json
from datetime import datetime, timedelta

today=datetime.today()

#print(today)

pin=["208011","208021"]

num_days=7

all_dates=[]

for i in range(num_days):
    all_dates.append(today+ timedelta((i)))

#print(all_dates)

final_dates=[]

for i in all_dates:
    final_dates.append(i.strftime("%d%m%y"))

#print(final_dates)    
 

while True:
    for p in pin:
        for d in final_dates:
            URL ="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(p,d)

            result=requests.get(URL)
            #print(result.text)
            
            json_result=result.json()
            
            if json_result["centers"]:
                for center in json_result["centers"]:
                    for session in center["sessions"]:
                        print("pincode: "+p)
                        print("date: "+d)
                        print("Center Name: ", center["name"])
                        print("Center Address: ",center["address"])
                        print("\n")
