#!/usr/bin/env python3

import sys

FILEPATH = None
OUTFILE = None

if len(sys.argv) < 2:
	print(f"Usage: {sys.argv[0]} [source] [optional arguments]")
	sys.exit(-1)

if "-f" in sys.argv:
	try:
		FILEPATH = sys.argv[sys.argv.index("-f") + 1]
	except IndexError:
		print("Please include filename after using -f")
		sys.exit(-1)
if "-o" in sys.argv:
	try:
		OUTFILE = sys.argv[sys.argv.index("-o") + 1]
	except IndexError:
		print("Please include filename for output after using -o")
		sys.exit(-1)
if "-h" in sys.argv:
	print(f"Usage: {sys.argv[0]} [source] [optional arguments]")
	print("\nOptions:\n\t-f: specify file to be obfuscated\n\t-o: specify file for output")

def parse_file(filename):
	with open(filename, "r") as f:
		file_data = f.read()
		return file_data

def obfuscate(data):
	result = "exec("
	for c in data:
		result += ("chr(" + str(ord(c)) + ")+")
	result += "'')"
	return result

def write_file(name, data):
	with open(name, "w") as f:
		f.write(data)

def main():
	global FILEPATH
	global OUTFILE
	obfuscated_data = None
	if FILEPATH is not None:
		try:
			data = parse_file(FILEPATH)
			obfuscated_data = obfuscate(data)
		except Exception as e:
			print("Error while reading file: ", e)
			sys.exit(-1)
	else:
		obfuscated_data = obfuscate(sys.argv[1])
	if OUTFILE is not None:
		write_file(OUTFILE, obfuscated_data)
	else:
		print(obfuscated_data)

if __name__ == "__main__":
	main()
