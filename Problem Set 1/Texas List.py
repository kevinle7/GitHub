# Kevin Le

from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import re

# Column headers in csv file
name = ''
school = ''
dpmt = ''
phd = 0

# Parse website
soup = BeautifulSoup(urlopen('http://www.utexas.edu/cola/depts/psychology/faculty/list.php'))

# Create csv file to import data
with open('Name List.csv', 'a', newline='') as csvfile: # Append to csv file
    s = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    # Set Labels
    # s.writerow(["Name", "Institution", "Department", "PHD Institution"])
    # If ran first, uncomment line above and change file to write instead of append
    
    school = soup.find("title").get_text() # Get school name
    dpmt = 'Psychology'
    for tag in soup("div", class_="list_item"): # Separate each person
        if(tag(text=re.compile('^Ph.D.'))): # Check if they have a PHD
            name = tag.find("a", href = True).get_text() # Find name from tag
            phd = tag(text=re.compile('^Ph.D.')) # Find tag with PHD institution
            temp = [] 
            for i in phd: 
                temp.append(str(i)) # Convert ResultSet to string
            phd = temp[0][7:].strip() # Select only institution name from string
            s.writerow([name, school, dpmt, phd])


