
# Duplicate link finder in csv
### Find out the duplicate links in the column of of csv file.

### How to use it?

#### Prerequisites

1. Must have python version 3
2. Install these python package (if not installed).
    1. pandas
    2. tldextract

#### Steps:

1. Clone and go to the project directory
2. Use this command ``python script.py <source_file_name> <column_index>`` **Note: Index starts from 0**
3. Example 1: `python script.py src.csv 2` **Note: This mean you have src.csv file which contains link in index 2** 
4. Additionally create `filter.txt` file which contains list of links to compare only those links
