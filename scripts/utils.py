def write_to_file(source_file,list_to_append):
	with open(source_file,'a') as f_source:
		for i in source_file:
			f_source.write(str(i)+'\n')

def delete_lines(f,n=1):
	with open(f, 'r') as fin: data = fin.read().splitlines(True)
	with open(f, 'w') as fout: fout.writelines(data[n:])	

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	# parser.add_argument('-k', '--keywords', help='keywords that have been scraped', type=list, required=True)
	parser.add_argument('-f', '--file', help='file', type=str, required=True)

	args = parser.parse_args()

	delete_lines(args.file)