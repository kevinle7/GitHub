# Kevin Le

from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import re

# Name variables
name = ''
school = ''
dpmt = ''
phd = ''

# Parse website
soup = BeautifulSoup(urlopen('http://www.adler.edu/page/faculty/'))

# Get links for each person
links = []
find_link = soup('div', {"class":re.compile("featureCapt")}) # Separate each person
for i in find_link:
    if(i(text=re.compile('(Ph.D.)'))): # Search if contains Ph.D.
        tag = i.find_previous_siblings("div", {"class":"featureCont"}) # Go step up to reach link
        found_link = tag[0].find("a", href=True)
        links.append(found_link['href'].strip()) # Add to array of all links
 
# Create csv file to import data
with open('Name List.csv', 'a', newline='') as csvfile: # Append to csv file
    s = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    # Set Labels
    # s.writerow(["Name", "Institution", "Department", "PHD Institution"])
    # If ran first, uncomment line above and change to write instead of append
    
    school = soup.find("a", href="/").get_text() # Get school name
    dpmt = 'Psychology' # Adler University is a school focus on psychology

    for link in links: # Iterate through pages for each person
        soup = BeautifulSoup(urlopen('http://www.adler.edu' + link))
        
        mainContent = soup('div', {"class":"contentLeft"})

        # Find title of person
        temp = mainContent[0].find('div', {"class":"html  position1"}) 
        name_temp = temp.next.next
        name = name_temp.get_text().split(',')[0].strip() # Get name
        
        temp = mainContent[0].find("li") # Find line that includes institution
        if (temp != None):
            phd_temp = temp.get_text().split(',') # Split to get PhD institution
            if len(phd_temp) == 3 or len(phd_temp) == 4: # All data not consistent, missing ','
                phd = phd_temp[2]
                s.writerow([name, school, dpmt, phd])
 



