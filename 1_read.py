"""
fetch("http://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date=2024-06-30", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7,hi;q=0.6",
    "cookie": "_ga=GA1.1.503742203.1720070934; _ga_2RYZG7Y4NC=GS1.1.1720074942.2.1.1720076437.0.0.0; FCNEC=%5B%5B%22AKsRol8wFKsNEYImWro2VGPkz9rY13RtrxwoeAZpzP04rLMUV8upySv02N6bXxIlt-6wQWW9yMP5He1f90RDpTXGbTqCEiIm9z39PUMyhMKkKKoTytWtFAyKdrVDX247yNgFRmCpz8ou-0hx4Ipj8mVZqX4Eca_m0Q%3D%3D%22%5D%5D",
    "Referer": "http://vegetablemarketprice.com/market/himachalpradesh/today",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
});
"""
import requests


url="http://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date=2024-06-30"

header={
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7,hi;q=0.6",
    "cookie": "_ga=GA1.1.503742203.1720070934; _ga_2RYZG7Y4NC=GS1.1.1720074942.2.1.1720076437.0.0.0; FCNEC=%5B%5B%22AKsRol8wFKsNEYImWro2VGPkz9rY13RtrxwoeAZpzP04rLMUV8upySv02N6bXxIlt-6wQWW9yMP5He1f90RDpTXGbTqCEiIm9z39PUMyhMKkKKoTytWtFAyKdrVDX247yNgFRmCpz8ou-0hx4Ipj8mVZqX4Eca_m0Q%3D%3D%22%5D%5D",
    "Referer": "http://vegetablemarketprice.com/market/himachalpradesh/today",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }


data= requests.get(url,headers=header)
print(data)
print(data.text)



