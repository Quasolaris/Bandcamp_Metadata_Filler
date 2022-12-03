# Bandcamp_Metadata_Filler
Takes files downloaded form Bandcamp renames them to title and sets the metadata accordingly. 

#### Path as argument is in the making, at the moment only same directory fills are possible (See below)

## How to use
Place Python file inside your album folder and run it with the following command:
```
python BC_MetadataFiller.py -sameDir
```
The script will search for information in the files name and adds it to the meta data of the original file. Then it creates a folder named "Metadata_FIles" where it copies the files with then title as file name instead of the Bandcamp string.




