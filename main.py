import re
from bs4 import BeautifulSoup
from get_url import simple_get
import datetime

base_url = 'https://umasslowell.campusdish.com/LocationsAndMenus/{0}?&periodId={1}&date={2}'

# raw_html = simple_get('https://umasslowell.campusdish.com/LocationsAndMenus/UniversityDiningCommons?locationId=488&storeId=&mode=Daily&periodId=1175&date=11%2F14%2F2018')


def clean_word(str1):
    """
            Clean the word from special and uppercase characters
    """
    return re.sub('\W+', '', str1.lower())


with open("locations", "r") as location_file:
    """
        Open location_list file and append each line to array location_list
        Lines that start with a '#' and only whitespace are ignored
    """
    location_list = []
    for line in location_file:
        if line.strip() and line[0] != '#':
            (k, v) = line.strip().split(":")
            time = [j.strip() for j in v.split(',')]
            location_list.append({'loc': k, 'time': time})
    location_file.close()


with open("ignore_station", "r") as ignore_file:
    """
        Open ignore_list file and make a key for each station name
        fill the key value with a dictionary of ignored times
        Lines that start with a '#' and only whitespace are ignored
    """
    ignore_list = {}
    for line in ignore_file:
        if line.strip() and line[0] != '#':
            (k, v) = line.strip().split(":")
            time = {j.strip() for j in v.split(',')}
            line = clean_word(k)
            ignore_list[line] = time
    ignore_file.close()


def check_ignore_list(str1, time):
    """
            Returns true if str is found within ignore_list during the given time
    """
    str1 = clean_word(str1)
    if str1 in ignore_list:
        if str(int(time) - 1173) in ignore_list[str1]:
            return True
    return False


for location in location_list:
    print("============================")
    print(location['loc'] + ':')
    print("============================")
    date = datetime.datetime.now().strftime("%m%%2F%d%%2F%Y")
    for time in location['time']:
        print("----------------------------")
        print("Time: " + time)
        print("----------------------------")
        time = str(int(time) + 1173)
        #print(base_url.format(location['loc'], time, date))

        raw_html = simple_get(base_url.format(location['loc'], time, date))
        html = BeautifulSoup(raw_html, 'html.parser')
        for station in html.find_all(class_="menu__station"):
            station_name = station.find('h2').text
            if not check_ignore_list(station_name, time):
                print(station_name + ":")
                for meal_item in station.find_all("li"):
                    name = meal_item.find(class_="item__name")
                    name_pre = "\t- "
                    if name and not name.find("a"):
                        print(name_pre + name.string.strip())
                    elif name and name.find("a"):
                        print(name_pre + name.find("a").string.strip())
