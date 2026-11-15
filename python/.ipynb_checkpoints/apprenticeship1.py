import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
run = True
app = Flask(__name__)
new_url="https://www.findapprenticeship.service.gov.uk/apprenticeships?sort=DistanceAsc&searchTerm=&location=SK16+5JA&distance=10&levelIds=6&routeIds=6&routeIds=7&routeIds=9&routeIds=15"
url = "https://www.findapprenticeship.service.gov.uk/apprenticeships"
params={
    "sort" : "DistanceAsc",
    "searchterm" : "",
    "location" : "Dukinfield Stalybridge, Greater Manchester",
    "distance": "10",
    "apprenticeshipTypes": "Standard",
    "levelIds": "6"
}


response = requests.get(new_url, params=params, headers={"User-Agent": "Mozilla/5.0"})
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text(strip=True))

response.raise_for_status()

for heading in soup.find_all("h2"):
    link = heading.find("a")
    if link:
        title= link.get_text(strip=True)
        href=link.get("href")
        print(title)
        print("https://www.findapprenticeship.service.gov.uk" + href)
        print()

@app.route("/")
def base():
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)