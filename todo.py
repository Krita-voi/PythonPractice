# fuction getBikeList , createBike , getBike , deletBike , updateBike
import requests
import json 

response=requests.get("http://localhost:8090/api/collections/bike/records")

if response.status_code == 200:
    response_content = response.content.decode('utf-8')   


    data= json.loads(response_content)


    format_json = json.dumps(data, indent= 2)

    print(format_json) 


else:
    print(f"Error in the HTTP requests{response.status_code}")

