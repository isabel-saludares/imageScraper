# PREPROCESSING SCRIPT FOR FACE DATA SCRAPING
# This script comprises three parts:
# 1. Cross-check one list to another
# 2. Generate batch lists given a source file
# 3. Connect the batch list of downloads to the scraping script

# 1. Cross-check one list to another
# ...
import argparse

def check_master(source,master,out):
    """
    Given source (source file; file that contains the names whose images ARE TO BE scraped), check if elements in source are in master (master list; list containing the names in which images are HAVE ALREADY BEEN scraped).
    If that element is not in the latter, then include it in out (list containing the names whose images NEED TO BE SCRAPED). 
    Returns an out file (default=csv)
    (Note: if an element in source is in the master list, this implies that it has been scraped.)
    
    Input/s:
    --------
    source : source file (str)
    master: master file (str)
    out: out file (str)
    """

    # check if elements in source are in master
    print('Starting cross-checking between source %s and master %s files...'%(str(source),str(master)))  
    with open(master) as f_master, open(source) as f_source:
        source = set(f_source.read().splitlines())
        master_lines = set(f_master.read().splitlines())

    with open(out,'w') as infile:
        for line in source: 
            within_file=line not in master_lines
            if within_file==True: infile.write(str(line)+'\n')
    print('1. Cross-checking complete!')



# 2. Generate batch lists given a source file
# ...
from itertools import islice
def next_n_lines(file_opened, N): return [x.strip() for x in islice(file_opened, N)]

def gen_string(lines): string=",".join(lines); string=string.replace('`',''); string=string.replace('"',''); string=string.replace("'",''); return "'"+string+"'"

def generate_batches(source,n=20):
    """
    generates batch lists given a source file.
    
    Input/s:
    source: source file (str)
    n: number of batches (int, default=20)
    """
    blist=[]
    with open(source) as f_source:
        start=next_n_lines(f_source, n); string=gen_string(start); blist.append(string)
        while start!=[]: start=next_n_lines(f_source, n); string=gen_string(start); blist.append(string)
        print('2. Generation of batches completed!')
    return blist



# 3. Connect the batch list of downloads to the scraping script
# ...
import os
def connect_batch_list(source_list,out_file,source_code='googleImageScrape.py',l=100):

    source0=set(source_list)

    with open(out_file,'w') as f_out:
        for line in source0: 
            line_content0='python ' + source_code + ' -k ' + str(line) + ' -l ' + str(l)
            line_content1='python utils.py -f ' + out_file + '\n'
            temp=os.path.splitext(out_file)[0] + '.tmp'
            ofile='"' + out_file + '"'; tmp='"' + temp + '"'
            line_content1='tail -n +2 ' + ofile + ' > ' + tmp + ' && mv ' + tmp + ' ' + ofile
            f_out.write(line_content0+' && '+ line_content1 + '\n')
    print('3. Batch lists generated!')


# ...
if __name__ == "__main__":

    # Taking command line arguments from users
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--source', help='source file (either file path or file name)', type=str, required=True)
    parser.add_argument('-m', '--master', help='master file (either file path or file name)', type=str, required=False)
    parser.add_argument('-o1', '--out1', help='out file (this file contains the names whose images should be scraped; either file path or file name)', type=str, required=False)
    parser.add_argument('-n', '--num', help='number of batches (default=20)', type=int, required=False)
    parser.add_argument('-c', '--code', help='source code (default=googleImageScrape.py)', type=str, required=False)
    parser.add_argument('-l', '--limit', help='limit re: number of images to be downloaded', type=str, required=False) 
    parser.add_argument('-o2', '--out2', help='out file (this file contains the  scripts for image scraping; either file path or file name; default file extension: .sh)', type=str, required=False)

    args = parser.parse_args()
    master='master.csv' if args.master is None else args.master
    if args.master is None:
        with open(master,'w') as f: pass # creates a blank file
    out='out-tbd.csv' if args.out1 is None else args.out1 # tbd = to be downloaded
    check_master(args.source,master,out)    

    if args.num is None: source_list=generate_batches(args.source)
    if args.num is not None: source_list=generate_batches(args.source,int(args.num))
    out_sh='out.sh' if args.out2 is None else args.out2


    if args.limit is None: connect_batch_list(source_list,out_sh)
    if args.limit is not None: connect_batch_list(source_list,out_sh,l=int(args.limit))
