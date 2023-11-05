import requests
from bs4 import BeautifulSoup
import json

# Define the URL for the advanced search page
url = "http://kenyalaw.org/caselaw/cases/advanced_search_courts?courtId=23"

# Set the search parameters for October 2023
search_params = {
    "start_date": "01-10-2023",
    "end_date": "31-10-2023",
}

response = requests.get(url, params=search_params)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    cases=soup.findAll('div',class_="post")
    for case in cases:
        caseTitle=case.find('h2').text.strip()
        #print(caseTitle)


with open("kenya_supreme_court_cases_october_2023.json", "w") as file:
    json.dump(caseTitle, file)

    print("Data saved successfully.")







