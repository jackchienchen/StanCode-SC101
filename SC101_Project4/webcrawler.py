"""
File: webcrawler.py
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
        soup = BeautifulSoup(html, features='html.parser')

        # ----- Write your code below this line ----- #
        items = soup.tbody.find_all('tr')
        male_count = 0
        female_count = 0
        for item in items[:-1]:
            lst = item.find_all('td')
            male_count += int(get_number(lst[2].text))
            female_count += int(get_number(lst[4].text))

        print(male_count)
        print(female_count)


def get_number(n):
    ans = ''
    for x in n:
        if x.isdigit():
            ans += x
    return ans


if __name__ == '__main__':
    main()
