# Kevin Le

from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

name = ''
school = ''
dpmt = ''
phd = 0

soup = BeautifulSoup(urlopen('http://psych.colorado.edu/people-faculty.html'))

# Create csv file to import data
with open('test.csv', 'w', newline='') as csvfile:
    s = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Set Labels
    s.writerow(["Name", "Institution", "Department", "PHD Institution"])
    school = soup.find("h1").get_text() # Get school name
    for dept_tag in soup("ul", class_="longli"): # Separate data by department
        # Get department name
        dpmt = dept_tag.previous_element.previous_element.previous_element.previous_element.get_text()
        tag = dept_tag("li")
        for i in tag: # Iterate through each person in department
            strings = i.get_text().split(',')
            if (len(strings) == 4): # There inconsistent use of commas and periods, which throws off data
                name = strings[0].strip() 
                phd = strings[3].split('.')[0].strip() # Split up text to get PHD institution
                s.writerow([name, school, dpmt, phd])
