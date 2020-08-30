# ip-api-bulk-checker
Python 3 implementation for repeatedly querying the ip-api ip address geo-location API with a list of IP addresses

## !! USE BULK_CHECKER_BATCH FOR BETTER PERFORMANCE !!

### Description

Python 3 is a pre-requisite, use 'pip' to install dependencies as required

If you need to get a lot of information about an ip address such as country, zip code, proxy or organisation, 
the ip-api is a good free api for requesting this information.

This solution takes a list of ip addresses in text format and sends requests for additional info about those addresses to ip-api.

This assumes a baseline knowledge in editing and executing python code as well as command line fluency to use (duh).

It also assumes knowledge of the Python 'pickle' module: 
https://docs.python.org/3/library/pickle.html
https://www.datacamp.com/community/tutorials/pickle-python-tutorial

### How to Use

1. Clone the repo
2. Create a textfile in the local repo with all the ip addresses listed, one per line
3. Edit the IN_FILE_NAME in bulk_checker_batch.py to hold the name of the created textfile in step 2 
4. Run bulk_checker_batch.py
5. You know have a pickle of the list holding dictionaries of data about the ip addresses in 'results.pickle'
6. Unpickle and access the specific information in your own implementation as neccesary

