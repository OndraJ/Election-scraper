"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Ondřej Janek
email: ondra.janek1@gmail.com
discord: Ondra J.#0489
"""

import csv
import sys
import requests as r
from bs4 import BeautifulSoup as bs

def main(url_address, file_name):
    print(f'Stahuji data z  URL: {url_address}')
    get_csv_file(soup,sys.argv[2])
    print(f'Uloženo do souboru: {file_name}')

def get_soup_generator(url):
    response = r.get(url)
    soup = bs(response.text, 'html.parser')
    return soup

soup = get_soup_generator(sys.argv[1])

def get_number_of_village(soup):
    numbers_of_villages = list()
    for elem in soup.find_all('td', class_ = 'cislo'):
        numbers_of_villages.append(elem.text)
    return numbers_of_villages

def get_name_of_village(soup):
    names_of_villages = list()
    for elem in soup.find_all('td', class_ = 'overflow_name'):
        names_of_villages.append(elem.text)
    return names_of_villages

def get_url_single_village(soup):
    helping_list = list()
    for elem in ('t1sa1 t1sb1', 't2sa1 t2sb1', 't3sa1 t3sb1'):
        helping_list += soup.select(f'td[headers="{elem}"]')
    urls = list()
    for i in helping_list:
        if i.find('a'):
            urls.append(i.find('a').get('href'))
    correct_urls = list()
    for url in urls:
        correct_urls.append('https://volby.cz/pls/ps2017nss/' + str(url))
    return correct_urls

def get_electors_and_votes(soup):
    electors = list()
    published_votes = list()
    valid_votes = list()
    for url in get_url_single_village(soup):
        village_url = r.get(url)
        soup = bs(village_url.text, 'html.parser')
        values = soup.find_all("td", class_="cislo")
        electors.append(values[3].text.replace('\xa0',''))
        published_votes.append(values[4].text.replace('\xa0',''))
        valid_votes.append(values[6].text.replace('\xa0',''))
    return electors,published_votes,valid_votes

def get_names_of_political_parties(soup):
    header_2 = list()
    single_url = r.get(get_url_single_village(soup)[0])
    soup = bs(single_url.text, 'html.parser')
    for name in soup.find_all('td', class_ = 'overflow_name'):
        header_2.append(name.text)
    return header_2

def get_votes_for_parties(soup):
    list_index= 0
    helping_list = list()
    votes = list()
    for url in get_url_single_village(soup):
        inner_url = r.get(url)
        soup = bs(inner_url.text, 'html.parser')
        votes.append([])
        for value in ('t1sa2 t1sb3', 't2sa2 t2sb3'):
            helping_list += soup.select(f'td[headers="{value}"]')
        for i in helping_list:
            if i.text != '-':
                votes[list_index].append(i.text.replace('\xa0',''))
        helping_list.clear()
        list_index += 1
    return votes

def grouping_political_parties(lists):
    list_of_parties = list()
    for i in range(len(lists[0])):
        one_party = list()
        for value in lists:
            one_party.append(value[i])
        list_of_parties.append(one_party)
    return list_of_parties


def get_csv_file(soup,file_name):
    header = ['Kód obce',
              'Název obce',
              'Voliči v seznamu',
              'Vydané obálky',
              'Platné hlasy']
    for element in get_names_of_political_parties(soup):
        header.append(element)

    data = [get_number_of_village(soup),
            get_name_of_village(soup),
            get_electors_and_votes(soup)[0],
            get_electors_and_votes(soup)[1],
            get_electors_and_votes(soup)[2]
    ]
    for element in grouping_political_parties(get_votes_for_parties(soup)):
        data.append(element)
    
    data_to_use = zip(*data)

    with open(file_name, mode='w', newline= '',encoding= 'UTF-8') as file:
        data_writer = csv.writer(file)
        data_writer.writerow(header)
        for row in data_to_use:
            data_writer.writerow(row)


if __name__ == '__main__':
    try:
        main(sys.argv[1],sys.argv[2])
    except IndexError:
        print('Špatně zadané argumenty')
    else:
        print('UKONČUJI election_scraper')








    