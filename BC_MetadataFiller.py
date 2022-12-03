import taglib
import shutil
import re
import os

directory =  os.getcwd()
dir_list = os.listdir(directory)


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

os.mkdir("Metadata_Files")

for filename in dir_list:
	regexGroups = re.search("^([^-]+) - ([^-]+) - ([0-9]+) (.*)\.", filename)
	
	if regexGroups:
		# get file extension
		split_tup = os.path.splitext(filename)
		file_extension = split_tup[1]		
		shutil.copyfile(filename, "Metadata_Files/"+regexGroups.group(4) + file_extension)
				


