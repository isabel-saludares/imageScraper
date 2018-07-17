# Image scraper for Google Images

## Download using search terms
The script has two main parameters:
-k <KEYWORDS, search terms (delineated by commas, between quotation marks)>     
-l <LIMIT, integer less than 100>

### For keywords:
Use quotation marks, delineated by commas, the search terms to be used to searching the images.  If you want to search several terms separately, use: -k "Leni Robredo,Donald Trump,Putin"

### For limit:
Use an integer number of no more than 100.

## To run
'''
cd <current directory of the googleImageScrape.py>
python googleImageScrape.py -k "Leni Robredo,Donald Trump,Putin" -l 10
'''

## Results
This automatically saves the images scraped in a folder output, where images are saved in separate folders for each search term (folder name is the search term).
