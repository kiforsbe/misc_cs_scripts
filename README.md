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


**Hint:** *The tagged music is also prepared for import into your favourite music player/library, with tags like Album, Artist and Title added. You can then use the script `convert_ogg_to_mp3.py` to convert the .ogg files to .mp3, with all tags kept!*

### How to use
First install at least Python 3.9 and the following dependencies:
- mutagen
- pandas

Run "`convert_cs1-radio_to_cs2.py`" with options:
- `-i` or `--input="path"` [default=`"C:/Program Files (x86)/Steam/steamapps/common/Cities_Skylines/Files/Radio/Music/"`]
  - Path to files to operate on.
- `-o` or `--output="path"` [default=`"./out/"`]
  -  Path to output of files.
- `-v`
  - Enable verbose output.


**Note!** *The script needs the `cs1_to_cs2_mapping.csv` file in the same folder as the script to execute. This file contains the mapping of original files and the appropriate tags and output filenames. If you want to use different mappings of tags, than this is where you can change that.*

#### Example
> `convert_cs1-radio_to_cs2.py -v -i "C:\Program Files (x86)\Steam\steamapps\common\Cities_Skylines\Files\Radio\Music\"`

### Getting the music in-game
**Warning:** *Making the game unable to find the `"cache.db"` file per steps below will greatly impact your game load time. On my system, it goes from 5-10 seconds, to at least a 50-60 seconds as the cache is rebuilt every time you load the game. If you use this method, make sure you can restore the file without reinstalling the game! If using Steam, you can verify the install, on other platforms, just make sure to keep a copy of it!*

Assuming your installation folder is `"C:\Program Files (x86)\Steam\steamapps\common\Cities Skylines II"`, follow the steps below.
1. Copy the output of the script to `"C:\Program Files (x86)\Steam\steamapps\common\Cities Skylines II\Cities2_Data\StreamingAssets\Audio~\Radio"` and 
2. Rename `"C:\Program Files (x86)\Steam\steamapps\common\Cities Skylines II\Cities2_Data\StreamingAssets\cache.db"` to something else like `"cache.db.old"`.

There might be better methods to get music in-game, but so far I've not found one. Hopefully Colossal Order/Paradox will provide a better mehthod via mods or similar to include additional music content.

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

## convert_ogg_to_mp3.py
Automatically converts .ogg files to .mp3, keeping tags.

### How to use
Install at least Python 3.9. No additional dependencies.

Run "`convert_ogg_to_mp3.py`" with options:
- `-i` or `--input="path"` [default=`"*.ogg"`]
  - Path to files to operate on. Wildcards can be applied."
- `-o` or `--output="path"` [default=`"./out/"`]
  -  Path to output of files.
- `-f` or `--ffmepg="path"` [default=`%FFMPEG%`]
  - Path to where on the system the ffmpeg binaries are located.
- `-v`
  - Enable verbose output.

### Example
> `convert_ogg_to_mp3.py -v -i "out" -o "outmp3`

### Missing functionality/content
- Proper error checking etc...
