# Experimental Results

## Contents
- `icse22`: results for ICSE 2022

## Scripts
1. `md2csv.py` converts Markdown results to CSV.
```
python3 md2csv.py [file].md
```

2. `table3.py` generates Table 3 in the ICSE 2022 technical paper.
```
cd icse22/raw_csv
...               # move mutations CSV results to the same folder
vim md2csv.py     # modify the 'datasets' variable to reflect the CSV filenames
python3 md2csv.py
```
