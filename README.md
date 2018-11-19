
## UML Dining Hall Web Scraper
My first Python program which goes to the UMass Lowell Dining Hall menu website and retrieves the menu for each location i.e. Fox Dining Commons or Hawk's Nest for each mealtime selected

**BeautifulSoup** and **Requests** are required to run the program

#### Features:
- Specify dining hall locations
- Pick what meals for the location
- Ignore menu items during certain times 

## Set-up
### location file:
The location file expects the URL format for the dining hall menu location followed by a colon `:` and list of numbers ranging from `0 - 2` which are separated by commas `,` to indicate which meal times are selected.

**Note:  Lines that start with a `#` are ignored.**

To get the URL format for the dining hall menu you must take it from the location's actual URL:
https://umasslowell.campusdish.com/LocationsAndMenus/UniversityDiningCommons  
So the URL format for Fox Dining Hall is *UniversityDiningCommons*

For the range of numbers:
- `0` represents Breakfast
- `1` represents Lunch
- `2` represents Dinner

Example of a **location**  file:
```
UniversityDiningCommons: 0, 1, 2
HawksNestDining: 2
```
<hr>

### ignore_station file:
The ignore_station file expects the names of stations that you wish to ignore followed by a colon `:` and list of numbers ranging from `0 - 2` which are separated by commas `,` to indicate which meal times that station is ignored at.

**Note:  Lines that start with a `#` are ignored.**

To get the station name you will have to go to a location page and copy the names which you want to ignore. The program will handle any case issues.

Stations like "Sizzle" in the Fox Dining Hall will always have the same food for lunch and dinner, but not for breakfast. So we can ignore the lunch and dinner menu from Sizzle by writing `Sizzle: 1, 2` in our ignore_station file

For the range of numbers:
- `0` represents Breakfast
- `1` represents Lunch
- `2` represents Dinner

Example of a **ignore_station**  file:
```
Fruit Bar: 0
Rustic Health: 0, 1, 2
Deli-licious: 1, 2
Farmer's Market: 1, 2
Saute: 1
Sizzle: 1, 2
```
