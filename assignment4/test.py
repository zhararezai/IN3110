#import the module
import requests
from requesting_urls import*
from filter_urls import*
from collect_dates import*

import pandas as pd
from bs4 import BeautifulSoup
from requesting_urls import get_html
from time_planner import TableEntry
from copy import copy

# grabbing the content of https://en.wikipedia.org/wiki/URL
#resp = requests.get("https://en.wikipedia.org/wiki/URL")

# get() method returns a response object
#print(resp.text)

"""url = "https://uio-in3110.github.io"
dest = "output.txt"


#test = get_html(url, output=str(dest))

html_test = 
    #<a href="#fragment-only">anchor link</a>
    #<a id="some-id" href="/relative/path#fragment">relative link</a>
    #<a href="//other.host/same-protocol">same-protocol link</a>
    #<a href="https://example.com">absolute URL</a>
   
#test2 = find_urls(html, base_url="https://en.wikipedia.org")
#articles = find_articles(html)

#html = get_html("https://en.wikipedia.org/wiki/Serena_Williams", output="output.txt")
#dates = find_dates(html)

year_test = [
    "vwfbivbg 2000 bvihfwbv",
    "vwfbivbg 300 bvihfwbv",
    "vwfbivbg 2000 bvihfwbv",
    "1111 dddd",
    "ddddddd 22222",
    "dddddddd 4444"
]

for element in year_test:
    test_regex =  re.search(r'[1-2][0-9]{3}', element)
    #print(test_regex)

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


jan = r"\b[jJ]an(?:uary)?\b"
feb = r"\b[fF]eb(?:ruary)?\b"
mar = r"\b[mM]ar(?:ch)?\b"
apr = r"\b[aA]pr(?:il)?\b"
may = r"\b[mM]a(?:y)?\b"
jun = r"\b[jJ]un(?:e)?\b"
jul = r"\b[jJ]ul(?:y)?\b"
aug = r"\b[aA]ugu(?:st)?\b"
sep = r"\b[sS]ep(?:tember)?\b"
oct = r"\b[oO]ct(?:ober)?\b"
nov = r"\b[nN]ov(?:ember)?\b"
dec = r"\b[dD]ec(?:ember)?\b"
iso_month_format = r"\b(?:0\d|1[0-2])\b"



for element in month_names:
    test = re.search(rf"{iso_month_format}", element)
    #print(test)

for month in month_names:
    ...
    #print(month_names.index(month) + 1)

days = [
    "1",
    "01",
    "9",
    "09",
    "10",
    "19",
    "29",
    "31"
]

pattern_day = r"\b(?:0\d|1[0-9]{1}|2[0-9]{1}|3[0-1]{1}|\d{1})\b"

for element in days:
    test = re.search(rf"{pattern_day}", element)
    #print(test)
    if (int(element[0]) != 0 and len(element) < 2): 
        element = "0" + element
        #print(element)
        #print(element.isdigit())


# reformat DMY as Y/M/D
day = "03"
month = "01"
year = "1962"
date_element = "03 01 1962"

date_element = re.sub(rf"({day})\s({month})\s({year})", r"\3/\2/\1", date_element)


#print(date_element)"""


#task 6
sample_table = """
<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>Venue</th>
      <th>Type</th>
      <th>Info</th>
    </tr>
  </thead>
    <tr>
      <td>October</td>
      <td rowspan="2">UiO</td>
      <td>Assignment 3</td>
      <td>image filters</td>
    </tr>
    <tr>
      <td>November</td>
      <td colspan="2">Assignment 4</td>
    </tr>
  
</table>
"""

"""table = BeautifulSoup(sample_table, "html.parser")
headings = table.find_all("th") #printer: [<th>Date</th>, <th>Venue</th>, <th>Type</th>, <th>Info</th>]
#print(f"headings {headings}")
labels = [th.text.strip() for th in headings] #printer: ['Date', 'Venue', 'Type', 'Info']

rows = table.find_all("tr")
rows = rows[1:2]
data = []

print(rows)

for tr in rows:
  cells = tr.find_all("td")
  row = []

  for cell in cells:
    colspan = cell.get("colspan")
    rowspan = cell.get("rowspan")

    if colspan is None: colspan = 0
    if rowspan is None: rowspan = 0
    
    text = cell.get_text(strip=True)
   
    row.append(
      TableEntry(
        text=text,
        rowspan=int(rowspan),
        colspan=int(colspan)
      )
    )

  data.append(row)

# Dict over all types of events
event_types = {
    "DH": "Downhill",
    "SL": "Slalom",
    "GS": "Giant Slalom",
    "SG": "Super Giant slalom",
    "AC": "Alpine Combined",
    "PG": "Parallel Giant Slalom",
}

wanted = ["Date", "Venue", "Type"]

filtered_data = [['October', 'UiO', 'Assignment 3'], ['November', 'UiO', 'Assignment 4']]
df = pd.DataFrame(filtered_data, columns=wanted)

#print(df.to_markdown())

#print(event_types.get(event_types["SL"][:2], event_types["SL"])) #printer Slalom


value_list = df["Type"].tolist() #printer ['Assignment 3', 'Assignment 4']"""


#task 8

sample_table2 = """
<table>
  <thead> 
    <tr>
      <th>Name, Pos, No</th>
    </tr>
  </thead>
    <tbody>
      <tr>
        <td>Pos: c</td>
        <td>No: 23</td>
        <td> <a href="/wiki/Charles_Bassey" title="Charles Bassey">Bassey, Charles</a></td>
      </tr
      <tr>
        <td>Pos: g</td>
        <td>No: 16</td>
        <td> <a href="/wiki/Brown_Charlie" title="Charlie Brown">Brown, Charlie</a></td>
      </tr
      <tr>
        <td>Pos: a</td>
        <td>No: 1</td>
        <td> <a href="/wiki/Joel_Embiid" title="Joel Embiid">Embiid, Joel</a></td>
      </tr
      <tr>
        <td>Pos: b</td>
        <td>No: 2</td>
        <td> <a href="/wiki/spiller2" title="spiller 2">spiller 2</a></td>
      </tr
    </tbody>
</table>
"""

table2 = BeautifulSoup(sample_table2, "html.parser")
base_url = "https://en.wikipedia.org"
players = []
player_links = {} #player name : player url

# Loop over every row and get the names from roster
rows = table2.find_all("tr")
#print(rows)
#rows = rows[1:]
#print(f"\nrows etter slicing {rows}")
#print(f"\nlen rows {len(rows)}")

for row in rows:
  cols = row.find_all("td")
  #print(f"\nrow: {row}")
  #print(f"\ncols: {cols}")
  #print(f"\nlen cols: {len(cols)}")

  for cell in cols:
    #print(f"cell: {cell}")
    if cell.find("a"):
      name = cell.find("a")
      player_links[name.get_text(strip=True)] = urljoin(base_url, name["href"])
      if player_links not in players:
        players.append(player_links)
    
#print(players)



# Get the table
""" html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Roster").find_next("table")
    
    players = []
    player_links = {} #player name : player url


    # Loop over every row and get the names from roster
    rows = table.find_("tr")
    rows = rows[1:2] #only fetching the rows from the column with players
    #print(f"len rows {len(rows)}")
    for row in rows:
        # Get the columns
        cols = row.find_all("td")
        # find name links (a tags)
        for cell in cols:
            if cell.find("a"):
                name = cell.find("a")
                # and add to players a dict with
                # {'name':, 'url':}
                player_links[name.get_text(strip=True)] = urljoin(base_url, name["href"])
                if player_links not in players:
                    players.append(player_links)"""

#task 10

def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    """  """

    # Get the table with stats
    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    table = None

    if soup.find(class_="mw-headline", string=re.compile("^Regular season")) is not None:
        table = soup.find(class_="mw-headline", string=re.compile("^Regular season")).find_next("table")
    else: 
        table = soup.find(id="NBA").find_next("table")
    
    headings = table.find_all("th")
    labels = [th.get_text(strip=True) for th in headings]
       

    stats = {"points" : 0,
            "assists" : 0,
            "rebounds" : 0
            } # keys: 'points', 'assists', and 'rebounds' 


    rows = table.find_all("tr")
    rows = rows[1:]
    # Loop over rows and extract the stats
    for row in rows:
        cols = row.find_all("td")
 
        year = cols[labels.index("Year")].get_text(strip=True)

        # Check correct team (some players change team within season)
        if cols[1].get_text(strip=True) == team and "2021–22" in year:
            # load stats from columns
            # keys should be 'points', 'assists', etc.
            stats["points"] = float(cols[12].get_text(strip=True).replace("*", ""))
            stats["assists"] = float(cols[9].get_text(strip=True).replace("*", ""))
            stats["rebounds"] = float(cols[8].get_text(strip=True).replace("*", ""))
        
    return stats


all_players = {'Phoenix': [{'name': 'Ayton, Deandre', 'url': 'https://en.wikipedia.org/wiki/Deandre_Ayton'}, {'name': 'Biyombo, Bismack', 'url': 'https://en.wikipedia.org/wiki/Bismack_Biyombo'}, {'name': 'Booker, Devin', 'url': 'https://en.wikipedia.org/wiki/Devin_Booker'}, {'name': 'Bridges, Mikal', 'url': 'https://en.wikipedia.org/wiki/Mikal_Bridges'}, {'name': 'Craig, Torrey', 'url': 'https://en.wikipedia.org/wiki/Torrey_Craig'}, {'name': 'Crowder, Jae', 'url': 'https://en.wikipedia.org/wiki/Jae_Crowder'}, {'name': 'Holiday, Aaron', 'url': 'https://en.wikipedia.org/wiki/Aaron_Holiday'}, {'name': 'Johnson, Cameron', 'url': 'https://en.wikipedia.org/wiki/Cameron_Johnson'}, {'name': 'Lundberg, Gabriel(TW)', 'url': 'https://en.wikipedia.org/wiki/Gabriel_Lundberg'}, {'name': 'McGee, JaVale', 'url': 'https://en.wikipedia.org/wiki/JaVale_McGee'}, {'name': 'Paul, Chris', 'url': 'https://en.wikipedia.org/wiki/Chris_Paul'}, {'name': 'Payne, Cameron', 'url': 'https://en.wikipedia.org/wiki/Cameron_Payne'}, {'name': 'Payton, Elfrid', 'url': 'https://en.wikipedia.org/wiki/Elfrid_Payton_(basketball)'}, {'name': 'Šarić, Dario', 'url': 'https://en.wikipedia.org/wiki/Dario_%C5%A0ari%C4%87'}, {'name': 'Shamet, Landry', 'url': 'https://en.wikipedia.org/wiki/Landry_Shamet'}, {'name': 'Wainright, Ish', 'url': 'https://en.wikipedia.org/wiki/Ish_Wainright'}], 'Milwaukee': [{'name': 'Allen, Grayson', 'url': 'https://en.wikipedia.org/wiki/Grayson_Allen'}, {'name': 'Antetokounmpo, Giannis', 'url': 'https://en.wikipedia.org/wiki/Giannis_Antetokounmpo'}, {'name': 'Antetokounmpo, Thanasis', 'url': 'https://en.wikipedia.org/wiki/Thanasis_Antetokounmpo'}, {'name': 'Carter, Jevon', 'url': 'https://en.wikipedia.org/wiki/Jevon_Carter'}, {'name': 'Connaughton, Pat', 'url': 'https://en.wikipedia.org/wiki/Pat_Connaughton'}, {'name': 'Hill, George', 'url': 'https://en.wikipedia.org/wiki/George_Hill_(basketball)'}, {'name': 'Holiday, Jrue', 'url': 'https://en.wikipedia.org/wiki/Jrue_Holiday'}, {'name': 'Ibaka, Serge', 'url': 'https://en.wikipedia.org/wiki/Serge_Ibaka'}, {'name': 'Lopez, Brook', 'url': 'https://en.wikipedia.org/wiki/Brook_Lopez'}, {'name': 'Mamukelashvili, Sandro(TW)', 'url': 'https://en.wikipedia.org/wiki/Sandro_Mamukelashvili'}, {'name': 'Matthews, Wesley', 'url': 'https://en.wikipedia.org/wiki/Wesley_Matthews'}, {'name': 'Middleton, Khris', 'url': 'https://en.wikipedia.org/wiki/Khris_Middleton'}, {'name': 'Nwora, Jordan', 'url': 'https://en.wikipedia.org/wiki/Jordan_Nwora'}, {'name': 'Portis, Bobby', 'url': 'https://en.wikipedia.org/wiki/Bobby_Portis'}, {'name': 'Tucker, Rayjon', 'url': 'https://en.wikipedia.org/wiki/Rayjon_Tucker'}, {'name': 'Vildoza, Luca', 'url': 'https://en.wikipedia.org/wiki/Luca_Vildoza'}, {'name': 'Wigginton, Lindell(TW)', 'url': 'https://en.wikipedia.org/wiki/Lindell_Wigginton'}], 'Dallas': [{'name': 'Bertāns, Dāvis', 'url': 'https://en.wikipedia.org/wiki/D%C4%81vis_Bert%C4%81ns'}, {'name': 'Brown, Sterling', 'url': 'https://en.wikipedia.org/wiki/Sterling_Brown_(basketball)'}, {'name': 'Brunson, Jalen', 'url': 'https://en.wikipedia.org/wiki/Jalen_Brunson'}, {'name': 'Bullock, Reggie', 'url': 'https://en.wikipedia.org/wiki/Reggie_Bullock'}, {'name': 'Burke, Trey', 'url': 'https://en.wikipedia.org/wiki/Trey_Burke'}, {'name': 'Chriss, Marquese', 'url': 'https://en.wikipedia.org/wiki/Marquese_Chriss'}, {'name': 'Dinwiddie, Spencer', 'url': 'https://en.wikipedia.org/wiki/Spencer_Dinwiddie'}, {'name': 'Dončić, Luka', 'url': 'https://en.wikipedia.org/wiki/Luka_Don%C4%8Di%C4%87'}, {'name': 'Finney-Smith, Dorian', 'url': 'https://en.wikipedia.org/wiki/Dorian_Finney-Smith'}, {'name': 'Green, Josh', 'url': 'https://en.wikipedia.org/wiki/Josh_Green_(basketball)'}, {'name': 'Hardaway, Tim, Jr.', 'url': 'https://en.wikipedia.org/wiki/Tim_Hardaway_Jr.'}, {'name': 'Kleber, Maxi', 'url': 'https://en.wikipedia.org/wiki/Maxi_Kleber'}, {'name': 'Marjanović, Boban', 'url': 'https://en.wikipedia.org/wiki/Boban_Marjanovi%C4%87'}, {'name': 'Ntilikina, Frank', 'url': 'https://en.wikipedia.org/wiki/Frank_Ntilikina'}, {'name': 'Pinson, Theo(TW)', 'url': 'https://en.wikipedia.org/wiki/Theo_Pinson'}, {'name': 'Powell, Dwight', 'url': 'https://en.wikipedia.org/wiki/Dwight_Powell'}, {'name': 'Wright, Moses(TW)', 'url': 'https://en.wikipedia.org/wiki/Moses_Wright'}], 'Memphis': [{'name': 'Adams, Steven', 'url': 'https://en.wikipedia.org/wiki/Steven_Adams'}, {'name': 'Aldama, Santi', 'url': 'https://en.wikipedia.org/wiki/Santi_Aldama'}, {'name': 'Anderson, Kyle', 'url': 'https://en.wikipedia.org/wiki/Kyle_Anderson_(basketball)'}, {'name': 'Bane, Desmond', 'url': 'https://en.wikipedia.org/wiki/Desmond_Bane'}, {'name': 'Brooks, Dillon', 'url': 'https://en.wikipedia.org/wiki/Dillon_Brooks'}, {'name': 'Clarke, Brandon', 'url': 'https://en.wikipedia.org/wiki/Brandon_Clarke'}, {'name': 'Culver, Jarrett', 'url': 'https://en.wikipedia.org/wiki/Jarrett_Culver'}, {'name': 'Jackson, Jaren, Jr.', 'url': 'https://en.wikipedia.org/wiki/Jaren_Jackson_Jr.'}, {'name': 'Jones, Tyus', 'url': 'https://en.wikipedia.org/wiki/Tyus_Jones'}, {'name': 'Konchar, John', 'url': 'https://en.wikipedia.org/wiki/John_Konchar'}, {'name': "Melton, De'Anthony", 'url': 'https://en.wikipedia.org/wiki/De%27Anthony_Melton'}, {'name': 'Morant, Ja', 'url': 'https://en.wikipedia.org/wiki/Ja_Morant'}, {'name': 'Pons, Yves(TW)', 'url': 'https://en.wikipedia.org/wiki/Yves_Pons'}, {'name': 'Terry, Tyrell(TW)', 'url': 'https://en.wikipedia.org/wiki/Tyrell_Terry'}, {'name': 'Tillie, Killian', 'url': 'https://en.wikipedia.org/wiki/Killian_Tillie'}, {'name': 'Tillman, Xavier', 'url': 'https://en.wikipedia.org/wiki/Xavier_Tillman'}, {'name': 'Williams, Ziaire', 'url': 'https://en.wikipedia.org/wiki/Ziaire_Williams'}], 'Philadelphia': [{'name': 'Bassey, Charles', 'url': 'https://en.wikipedia.org/wiki/Charles_Bassey'}, {'name': 'Brown, Charlie(TW)', 'url': 'https://en.wikipedia.org/wiki/Charlie_Brown_Jr._(basketball)'}, {'name': 'Embiid, Joel', 'url': 'https://en.wikipedia.org/wiki/Joel_Embiid'}, {'name': 'Green, Danny', 'url': 'https://en.wikipedia.org/wiki/Danny_Green_(basketball)'}, {'name': 'Harden, James', 'url': 'https://en.wikipedia.org/wiki/James_Harden'}, {'name': 'Harris, Tobias', 'url': 'https://en.wikipedia.org/wiki/Tobias_Harris'}, {'name': 'Joe, Isaiah', 'url': 'https://en.wikipedia.org/wiki/Isaiah_Joe'}, {'name': 'Jordan, DeAndre', 'url': 'https://en.wikipedia.org/wiki/DeAndre_Jordan'}, {'name': 'Korkmaz, Furkan', 'url': 'https://en.wikipedia.org/wiki/Furkan_Korkmaz'}, {'name': 'Maxey, Tyrese', 'url': 'https://en.wikipedia.org/wiki/Tyrese_Maxey'}, {'name': 'Milton, Shake', 'url': 'https://en.wikipedia.org/wiki/Shake_Milton'}, {'name': 'Millsap, Paul', 'url': 'https://en.wikipedia.org/wiki/Paul_Millsap'}, {'name': 'Niang, Georges', 'url': 'https://en.wikipedia.org/wiki/Georges_Niang'}, {'name': 'Powell, Myles(TW)', 'url': 'https://en.wikipedia.org/wiki/Myles_Powell'}, {'name': 'Reed, Paul', 'url': 'https://en.wikipedia.org/wiki/Paul_Reed_(basketball)'}, {'name': 'Springer, Jaden', 'url': 'https://en.wikipedia.org/wiki/Jaden_Springer'}, {'name': 'Thybulle, Matisse', 'url': 'https://en.wikipedia.org/wiki/Matisse_Thybulle'}], 'Boston': [{'name': 'Brown, Jaylen', 'url': 'https://en.wikipedia.org/wiki/Jaylen_Brown'}, {'name': 'Fitts, Malik', 'url': 'https://en.wikipedia.org/wiki/Malik_Fitts'}, {'name': 'Hauser, Sam', 'url': 'https://en.wikipedia.org/wiki/Sam_Hauser'}, {'name': 'Horford, Al', 'url': 'https://en.wikipedia.org/wiki/Al_Horford'}, {'name': 'Kornet, Luke', 'url': 'https://en.wikipedia.org/wiki/Luke_Kornet'}, {'name': 'Morgan, Juwan', 'url': 'https://en.wikipedia.org/wiki/Juwan_Morgan'}, {'name': 'Nesmith, Aaron', 'url': 'https://en.wikipedia.org/wiki/Aaron_Nesmith'}, {'name': 'Pritchard, Payton', 'url': 'https://en.wikipedia.org/wiki/Payton_Pritchard'}, {'name': 'Ryan, Matt(TW)', 'url': 'https://en.wikipedia.org/wiki/Matt_Ryan_(basketball)'}, {'name': 'Smart, Marcus', 'url': 'https://en.wikipedia.org/wiki/Marcus_Smart'}, {'name': 'Stauskas, Nik', 'url': 'https://en.wikipedia.org/wiki/Nik_Stauskas'}, {'name': 'Tatum, Jayson', 'url': 'https://en.wikipedia.org/wiki/Jayson_Tatum'}, {'name': 'Theis, Daniel', 'url': 'https://en.wikipedia.org/wiki/Daniel_Theis'}, {'name': 'Thomas, Brodric(TW)', 'url': 'https://en.wikipedia.org/wiki/Brodric_Thomas'}, {'name': 'White, Derrick', 'url': 'https://en.wikipedia.org/wiki/Derrick_White_(basketball)'}, {'name': 'Williams, Grant', 'url': 'https://en.wikipedia.org/wiki/Grant_Williams_(basketball)'}, {'name': 'Williams, Robert III', 'url': 'https://en.wikipedia.org/wiki/Robert_Williams_III'}], 'Miami': [{'name': 'Adebayo, Bam', 'url': 'https://en.wikipedia.org/wiki/Bam_Adebayo'}, {'name': 'Butler, Jimmy', 'url': 'https://en.wikipedia.org/wiki/Jimmy_Butler'}, {'name': 'Dedmon, Dewayne', 'url': 'https://en.wikipedia.org/wiki/Dewayne_Dedmon'}, {'name': 'Haslem, Udonis', 'url': 'https://en.wikipedia.org/wiki/Udonis_Haslem'}, {'name': 'Herro, Tyler', 'url': 'https://en.wikipedia.org/wiki/Tyler_Herro'}, {'name': 'Highsmith, Haywood', 'url': 'https://en.wikipedia.org/wiki/Haywood_Highsmith'}, {'name': 'Lowry, Kyle', 'url': 'https://en.wikipedia.org/wiki/Kyle_Lowry'}, {'name': 'Martin, Caleb', 'url': 'https://en.wikipedia.org/wiki/Caleb_Martin_(basketball)'}, {'name': 'Morris, Markieff', 'url': 'https://en.wikipedia.org/wiki/Markieff_Morris'}, {'name': 'Mulder, Mychal(TW)', 'url': 'https://en.wikipedia.org/wiki/Mychal_Mulder'}, {'name': 'Oladipo, Victor', 'url': 'https://en.wikipedia.org/wiki/Victor_Oladipo'}, {'name': 'Robinson, Duncan', 'url': 'https://en.wikipedia.org/wiki/Duncan_Robinson_(basketball)'}, {'name': 'Smart, Javonte(TW)', 'url': 'https://en.wikipedia.org/wiki/Javonte_Smart'}, {'name': 'Strus, Max', 'url': 'https://en.wikipedia.org/wiki/Max_Strus'}, {'name': 'Tucker, P. J.', 'url': 'https://en.wikipedia.org/wiki/P._J._Tucker'}, {'name': 'Vincent, Gabe', 'url': 'https://en.wikipedia.org/wiki/Gabe_Vincent'}, {'name': 'Yurtseven, Ömer', 'url': 'https://en.wikipedia.org/wiki/%C3%96mer_Yurtseven'}], 'Golden State': [{'name': 'Bjelica, Nemanja', 'url': 'https://en.wikipedia.org/wiki/Nemanja_Bjelica'}, {'name': 'Chiozza, Chris(TW)', 'url': 'https://en.wikipedia.org/wiki/Chris_Chiozza'}, {'name': 'Curry, Stephen', 'url': 'https://en.wikipedia.org/wiki/Stephen_Curry'}, {'name': 'Green, Draymond', 'url': 'https://en.wikipedia.org/wiki/Draymond_Green'}, {'name': 'Iguodala, Andre', 'url': 'https://en.wikipedia.org/wiki/Andre_Iguodala'}, {'name': 'Kuminga, Jonathan', 'url': 'https://en.wikipedia.org/wiki/Jonathan_Kuminga'}, {'name': 'Lee, Damion', 'url': 'https://en.wikipedia.org/wiki/Damion_Lee'}, {'name': 'Looney, Kevon', 'url': 'https://en.wikipedia.org/wiki/Kevon_Looney'}, {'name': 'Moody, Moses', 'url': 'https://en.wikipedia.org/wiki/Moses_Moody'}, {'name': 'Payton, Gary, II', 'url': 'https://en.wikipedia.org/wiki/Gary_Payton_II'}, {'name': 'Poole, Jordan', 'url': 'https://en.wikipedia.org/wiki/Jordan_Poole'}, {'name': 'Porter, Otto Jr.', 'url': 'https://en.wikipedia.org/wiki/Otto_Porter_Jr.'}, {'name': 'Thompson, Klay', 'url': 'https://en.wikipedia.org/wiki/Klay_Thompson'}, {'name': 'Toscano-Anderson, Juan', 'url': 'https://en.wikipedia.org/wiki/Juan_Toscano-Anderson'}, {'name': 'Weatherspoon, Quinndary(TW)', 'url': 'https://en.wikipedia.org/wiki/Quinndary_Weatherspoon'}, {'name': 'Wiggins, Andrew', 'url': 'https://en.wikipedia.org/wiki/Andrew_Wiggins'}, {'name': 'Wiseman, James', 'url': 'https://en.wikipedia.org/wiki/James_Wiseman'}]}


for team, players in all_players.items():

  for player in players:
      player_stats = get_player_stats(player["url"], team)
      player.update(player_stats)
      #print(player["points"])
  #print(sorted(players.items())
  players.sort(key=lambda x : x["points"], reverse=True)
  #print(players)


#print(all_players.get("Milwaukee")[0])
#print(all_players.get("Milwaukee")[1])
#print(all_players.get("Milwaukee")[0])
print(all_players.get("Milwaukee")[:3])

""" printer:  
[{'name': 'Antetokounmpo, Giannis', 'url': 'https://en.wikipedia.org/wiki/Giannis_Antetokounmpo', 'points': 29.9, 'assists': 5.8, 'rebounds': 11.6}, {'name': 'Middleton, Khris', 'url': 'https://en.wikipedia.org/wiki/Khris_Middleton', 'points': 20.1, 'assists': 5.4, 'rebounds': 5.4}, {'name': 'Holiday, Jrue', 'url': 'https://en.wikipedia.org/wiki/Jrue_Holiday', 'points': 18.3, 'assists': 6.8, 'rebounds': 4.5}]
"""