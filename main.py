import requests
import json

url = "https://api.fda.gov/device/classification.json"
params = {
    "search": "medical_specialty:DE",
    "limit": 10
}

r = requests.get(url, params=params)

print(f"Status Code: {r.status_code}")
print(r.json())


# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()

# @app.get("/devices")
# # in function specify type
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}