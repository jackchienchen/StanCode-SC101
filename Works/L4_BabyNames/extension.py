"""
File: extension.py
Name: Jack Chen
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        items = soup.find_all('table', {'class': 't-stripe'})
        texts = []
        for item in items:
            texts = item.tbody.text.split()  # acquire the whole tbody info in a list
        n = 2  # Male index start
        m = 4  # Female index start
        male_total = 0
        female_total = 0
        for i in range(200):  # To add up the amount of babies for both male and female
            # texts[n] will return ###,###, which is a str.
            # So we will need to apply .split to make it into a list of digit integers.
            # Then turning them into integers
            male_accurate_number = int(texts[n].split(',')[0])*1000 + int(texts[n].split(',')[1])
            male_total += male_accurate_number
            female_accurate_number = int(texts[m].split(',')[0]) * 1000 + int(texts[m].split(',')[1])
            female_total += female_accurate_number
            n += 5
            m += 5
        print(f'Male Number: {male_total}')
        print(f'Female Number: {female_total}')



if __name__ == '__main__':
    main()
