# Pikabu Comments Corpus


> This corpus contains a collection of 18,2 million of pulicly available comments on pikabu.ru. 


## Data Description

- 
- The database has one table, July2017, with following fields:
	- id
	- parent_id
	- comment


## Processed Data

The 600 MB .csv database file can be downloaded by running **pull\_data.sh**

```bash
./pull_data.sh
```

You can also extract all the dialogue exchanges from this .csv file as follows:

from A to B
from B to A
===
from C to D
from D to C

by running **dialogue\_extractor.py**

```bash
./dialogue_extractor.py -i <inputfile>.csv -o <outputfile>.txt
```
