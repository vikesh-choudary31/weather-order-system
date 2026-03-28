
import json
import asyncio
import requests
import aiohttp 
import os
from dotenv import load_dotenv

#I want to load API Key 
# load_dotenv()
# API_KEY = os.getenv("API_KEY")
# print("API KEY: ",API_KEY)

def load_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    #print(f"API KEY: {api_key}")
    return api_key

def get_url():
    url = "http://api.openweathermap.org/data/2.5/weather"
    return url

def get_json_orders_file():
    with open("orders.json","r") as file:
        orders = json.load(file)
        return orders 

# for order in orders:
#     print(order,end="\n")
# print()

def generate_weather_aware_apology(customer,city,weather):
    return f"Hi {customer}, your order to {city} is delayed due to {weather}. Thank You for your patience!"

def get_city_name(order_data):
    city1 = order_data["city"]
    return city1

def get_parameters(order):
    city = order["city"]
    API_KEY = load_api_key()
    params = {
        "q": city,
        "appid": API_KEY
    }

    return params

def update_order_data(order,data):

    city = order["city"]
    given_weather = data["weather"][0]["main"]
    customer = order["customer"]

    print(f"City: {city} --> Weather: {given_weather}")
    
    if(given_weather in ["Rain","Snow","Extreme","Smoke"]):
        order["status"] = "Delayed"
        msg = generate_weather_aware_apology(customer,city,given_weather)
        print(msg)

# Fetching weather of order o using normal way, one by one API call
def weather_orders_json(orders):

    for order in orders:

        city = get_city_name(order)

        params = get_parameters(order)

        response = requests.get(url,params=params)

        data = response.json()

        if(data.get("cod") != 200):
            print(f"Invalid City: {city}")
            continue

        update_order_data(order,data)

async def fetch_weather(session,order):

    city = get_city_name(order)
    API_KEY = load_api_key()
    url = get_url()

    try:
        params = {
            "q" : city,
            "appid" : API_KEY
        }

        async with session.get(url,params=params) as response:
            data = await response.json()
            return city,data
    except Exception as e:
        print(f"Error fetching {city}: {e}")
        return city,None 

# Fetching weather of customer order location using async, much faster than normal way
async def main(orders):

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session,order) for order in orders]

        results = await asyncio.gather(*tasks)

    for order,(city,data) in zip(orders,results):
        if(data is None) or (data.get("cod") != 200):
            print(f"Invalid city: {city}")
            continue

        update_order_data(order,data) 

    with open("orders_updated.json","w") as file:
        json.dump(orders,file,indent = 2)

API_KEY = load_api_key()

print(API_KEY)

url = get_url()

orders = get_json_orders_file()

asyncio.run(main(orders))

#weather_orders_json(orders)

#with open("orders_updated.json","w") as file:
 #   json.dump(orders,file,indent=2)







