# Kevin Le

from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

# Column headers in csv file
name = ''
school = ''
dpmt = ''
phd = 0

# Parse website
soup = BeautifulSoup(urlopen('http://psych.colorado.edu/people-faculty.html'))

# Create csv file to import data
with open('Name List.csv', 'w', newline='') as csvfile:
    s = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Set Labels
    s.writerow(["Name", "Institution", "Department", "PHD Institution"])
    
    school = soup.find("h1").get_text() # Get school name
    dpmt = soup.find("div", id="header").h1.get_text() # Get department name

    for dept_tag in soup("ul", class_="longli"): # Separate data by department
        tag = dept_tag("li")
        for i in tag: # Iterate through each person in department
            strings = i.get_text().split(',')
            if (len(strings) == 4): # There is inconsistent use of commas and periods, which throws off data
                                    # Strings with len 4 have consistent format and separation
                name = strings[0].strip() 
                phd = strings[3].split('.')[0].strip() # Split up text to get PHD institution
                s.writerow([name, school, dpmt, phd])

    
