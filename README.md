# Image scraper for Google Images

(Contributors: Maria Isabel Saludares, JP Maulion)

## To run the script/s:
```
1. 
cd [current directory of googleImageScrape.py]
python preprocess.py -s <source file>

(example: python preprocess.py -s person_ner.csv)

2.
Part 1. will yield a .sh file. To run this:
bash <.sh file>
(example: bash out.sh)

Note: Use python or python3
```

## Parameters:
```
-s  [SOURCE]      source file; contains the names whose images ARE TO BE SCRAPED; names HAVEN'T BEEN CROSS-CHECKED with the reference file)
-m  [MASTER]      reference file; contains the names whose images HAVE BEEN SCRAPED
-o1 [OUT1]        file that contains the names whose images ARE TO BE SCRAPED; names HAVE BEEN CROSS-CHECKED with the reference file)
-o2 [OUT2]        file that contains the batch scripts
-n  [NUM]         number of keywords per batch (integer; default=20)
-l  [LIMIT]       the number of times a keyword has to be downloaded (integer; default=100)
```

## Note: keywords have been incorporated in the .py file

### For keywords:
Use quotation marks, delineated by commas, the search terms to be used to searching the images.  If you want to search several terms separately, use: -k "Leni Robredo,Donald Trump,Putin"


## Results
This automatically saves the images scraped in a folder output, where images are saved in separate folders for each search term (folder name is the search term).
