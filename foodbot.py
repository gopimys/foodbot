import http.client
import _json

conn = http.client.HTTPSConnection("gym-calculations.p.rapidapi.com")

payload = "{\r\"weight\": 70,\r\"height\": 1.8\r}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "bd127f8fd0mshaeb5f068befc84fp11c069jsn7471fe467031",
    'X-RapidAPI-Host': "gym-calculations.p.rapidapi.com"
}

conn.request("POST", "/bmi", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
print(res.status)