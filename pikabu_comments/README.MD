# Pikabu Comments Corpus


> This corpus contains a collection of 6 million of publicly available comments on pikabu.ru. 


## Data Description

- 6040111 filtered comments
- 3611347 dialogue exchanges
- The database has one table, july2017, with following fields:
	- id
	- parent_id
	- comment


## Processed Data

The 605 MB .csv database file can be downloaded by running **pull\_data.sh**

```bash
./pull_data.sh
```

You can also extract all the dialogue exchanges from this .csv file as follows:

```
from A to B
from B to A
===
from C to D
from D to C
```

by running **dialogue\_extractor.py**

```bash
./dialogue_extractor.py -i <inputfile>.csv -o <outputfile>.txt
```

or download the .txt file with all the exchanges where every line contains >=7 symbols by running **pull\_qa.sh**

```bash
./pull\_qa.sh
```