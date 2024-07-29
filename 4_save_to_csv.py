import requests
import pandas as pd
import json

url = "http://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date=2024-06-30"

header = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7,hi;q=0.6",
    "cookie": "_ga=GA1.1.503742203.1720070934; _ga_2RYZG7Y4NC=GS1.1.1720074942.2.1.1720076437.0.0.0; FCNEC=%5B%5B%22AKsRol8wFKsNEYImWro2VGPkz9rY13RtrxwoeAZpzP04rLMUV8upySv02N6bXxIlt-6wQWW9yMP5He1f90RDpTXGbTqCEiIm9z39PUMyhMKkKKoTytWtFAyKdrVDX247yNgFRmCpz8ou-0hx4Ipj8mVZqX4Eca_m0Q%3D%3D%22%5D%5D",
    "Referer": "http://vegetablemarketprice.com/market/himachalpradesh/today",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

# Requesting data from the API
response = requests.get(url, headers=header)

# Checking if request was successful
if response.status_code == 200:
    # Parsing JSON data
    js_data = json.loads(response.text)
    
    new_arr = []
    for api in js_data["data"]:
        new_js = {
            "date": "2024-06-30",
            "veg_name": str(api["vegetablename"]),
            "whole_price": str(api["price"]),
            "retail_price": str(api["retailprice"]),
            "shoping_mall_price": str(api["shopingmallprice"]),
            "unit": str(api["units"])
        }
        new_arr.append(new_js)
    
    # Creating a DataFrame from the list
    df = pd.DataFrame(new_arr)
    
    # Saving DataFrame to CSV file
    df.to_csv("output.csv", index=False)
    print("Data saved to 'output.csv' successfully.")
else:
    print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")




