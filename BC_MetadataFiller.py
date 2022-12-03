import taglib
import shutil
import re
import os
import sys


def fillMetadata(dir_list):

	print("Files found:")
	print("---------------------------------")
	for filename in dir_list:
		print(filename)

	print("---------------------------------")
	print("")
	print("Collecting and adding metadata")
	for filename in dir_list:

		# get metadata from file name
		regexGroups = re.search("^([^-]+) - ([^-]+) - ([0-9]+) (.*)\.", filename)
		if regexGroups:

			# set meta data
			song = taglib.File(filename)
			song.tags["ARTIST"] =  [regexGroups.group(1)]
			song.tags["ALBUM"] = [regexGroups.group(2)]
			song.tags["TRACKNUMBER"] = [regexGroups.group(3)]
			song.tags["TITLE"] = [regexGroups.group(4)]
			song.save()
			
			
		else:
			print("Not a music file")

	print("Metadata collected")

	os.mkdir("Metadata_Files")

	for filename in dir_list:
		regexGroups = re.search("^([^-]+) - ([^-]+) - ([0-9]+) (.*)\.", filename)
		
		if regexGroups:
			# get file extension
			split_tup = os.path.splitext(filename)
			file_extension = split_tup[1]		
			shutil.copyfile(filename, "Metadata_Files/"+regexGroups.group(4) + file_extension)			
	print("Metadata filled files saved in 'Metadata_Files' folder inside oroginal album folder")




arguments = sys.argv

if len(arguments) <= 1: 
	print("Type '-h' for help")

elif arguments[1] == "-h":
	print("============================================")
	print("Bancamp Metadata Filler")
	print("============================================")
	print("For indepth explanation see README on GitHub: https://github.com/Quasolaris/Bandcamp_Metadata_Filler")

	print("")
	print("Use python3")
	print("")
	print("To automatically go through directories of albums type '-sameDir'")
	print("This will go through all music files that are in the same directory as the script")
	print(" ")
	print("To have same function as AUTO mode but with set directory type '-manualDir \"ABSOLUTEPATH/TO/ALBUM/DIRECTORIES\"'")

elif arguments[1] == "-sameDir":
	directory =  os.getcwd()
	dir_list = os.listdir(directory)

	fillMetadata(dir_list)

elif arguments[1] == "-manualDir":
	directory =  arguments[2]
	dir_list = os.listdir(directory)
	fillMetadata(dir_list)

else:
	print("Command unknown, type '-h' for help")