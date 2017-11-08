#Worked with Lauren Baker on this homework

import requests
from bs4 import BeautifulSoup as bs

resp = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General")
soup = (resp.content, "html.parser")

#create list with election IDs
row = soup.find_all("tr", {"class":"election_item"}) #find the tag and look at election item in the class
election_item = []
for tag in row: election_item.append(tag.get("id"))
election_item = [x.split("-")[2] for x in election_item]

#create list with years
year = soup.find_all("td", {"class":"year"})
year = [row.text for row in year]

#combine lists and order by year, then election ID
ELECTION_ID = list(zip(year, election_item))

#export as txt file
with open("ELECTION_ID.txt", "w") as f:
f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in YEARS_IDS))
