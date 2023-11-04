# Misc Cities Skylines Scripts
Miscellaneous Cities Skylines and Cities Skylines 2 scripts and helpers.

## convert_cs1-radio_to_cs2.py
Automatically copies and tags CS1 radio for CS2, and creates radio network and channel settings files for each supported station.

### Description
Used to automatically copy, rename and tag Cities Skylines 1 Radio tracks, prepared for use in Cities Skylines 2.
Where the original artist is not clear, the default is to attribute Colossal Order.
The script automatically generates Cities Skylines 2 Radio Network and Radio Channel settings files for each channel (JSON files, type ".coc").

The script uses a mapping CSV file that contains the following Cities Skylines radio stations:
| Station | Folder | DLC | Release date |
|---------|--------|-----|--------------|
| All That Jazz | Jazz | Paid DLC | 2017-12-05 |
| Calm the Mind Radio | CalmTheMind | Paid DLC | 2022-01-25 |
| Campus Radio | CampusRadio | Paid DLC | 2019-05-21 |
| Carols, Candles and Candy | Christmas Radio | Free DLC | 2017-12-05 |
| Classics Radio, The | Classical | Base game | 2015-03-10 |
| Coast to Coast Radio | CoastToCoast | Paid DLC | 2020-03-26 |
| Concerts Radio | Concerts | Paid DLC | 2017-08-17 |
| Country Road Radio | Country | Paid DLC | 2018-05-24 |
| Deep Focus Radio | DeepFocus | Paid DLC | 2019-05-21 |
| Downtown Radio | DowntownRadio| Paid DLC | 2019-11-07 |
| Gold FM | GoldFM | Base game | 2015-03-10 |
| K-Pop Station | KPopRadio | Paid DLC | 2022-11-15 |
| Official Mars Radio | Mars | Free in Patch 1.9.2 | 2018-03-09 |
| On Air Radio | OnAir | Paid DLC | 2022-01-25 |
| Paradise Radio | ParadiseRadio | Paid DLC | 2022-09-14 |
| Rail Hawk Radio | RailHawk | Paid DLC | 2021-05-21 |
| Relaxation Station | Relaxation | Paid DLC | 2016-11-29 |
| Rock City Radio | Rock | Paid DLC | 2017-05-18 |
| Shoreline Radio | ShorelineRadio | Paid DLC | 2022-09-14 |
| Smooth Funk Radio | SmoothFunk | Base game | 2015-03-10 |
| Sunny Breeze Radio | SunnyBreeze | Paid DLC | 2021-05-21 |
| Synthetic Dawn Radio | Synthetic | Paid DLC | 2018-10-23 |

*Request: If you have the Music Pack DLCs below and are willing to provide the data (folders & filenames) for them, that would be great!*

Not supported stations (due to not having bought them yet):
| Station | Folder | DLC | Release date |
|---------|--------|-----|--------------|
| 80s Downtown Beat | ? | Paid DLC | 2022-11-15 |
| 80s Movie Tunes | ? | Paid DLC | 2023-03-22 |
| 90s Pop Radio | ? | Paid DLC | 2023-05-23 |
| African Vibes | ? | Paid DLC | 2022-12-13 |
| Jadia Radio | ? | Paid DLC | 2023-03-22 |
| Piano Tunes Radio | ? | Paid DLC | 2023-05-23 |
| Pop Punk Radio | ? | Paid DLC | 2023-03-22 |


*Hint: The tagged music is also prepared for import into your favourite music player/library, with tags like Album, Artist and Title added.*

### How to use
First install at least Python 3.9 and the following dependencies:
- mutagen
- pandas

Run "`convert_cs1-radio_to_cs2.py`" with options:
- `-i` or `--input="path"` [default=""]
  - Path to files to operate on. Wildcards can be applied e.g. -i 'C:\Program Files (x86)\Steam\steamapps\common\Cities_Skylines\Files\Radio\Music\', [default=]."
- `-o` or `--output="path"` [default="./out/"]
  -  Path to output of files [default='out\']
- `-v`
  - Enable verbose output.

### Example
> `convert_cs1-radio_to_cs2.py -v -i "C:\Program Files (x86)\Steam\steamapps\common\Cities_Skylines\Files\Radio\Music\"`

### Missing functionality/content
- A number of Music Pack DLCs (see above)
- Conversion of Cities Skylines 1 radio blurbs to Cities Skylines 2
- Conversion of Cities Skylines 1 radio talk to Cities Skylines 2
- Cities Skylines 2 radio network art/icon
- Cities Skylines 2 radio channel art/icon
- Cities Skylines 2 radio channel description
- Cities Skylines 2 radio channel playlist length
- Track numbers for each track
- Additional meta data for each tack
- Album art