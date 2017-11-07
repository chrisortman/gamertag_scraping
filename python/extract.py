from bs4 import BeautifulSoup
from glob import glob

output_file = open("extracted.csv","w")
html_files = glob("*.html")
for f in html_files:
   doc = BeautifulSoup(open(f), "lxml")
   rows = doc.find_all("tr",class_="row")
   for row in rows:
      tds = row.find_all("td")
      gamertag = tds[2].next_element.next_element
      points = tds[3].string.replace(",","")
      line = gamertag + "," + points + "\n"
      output_file.write(line)

output_file.close()
