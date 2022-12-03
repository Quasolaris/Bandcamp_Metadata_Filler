# Bandcamp_Metadata_Filler
This script is a work in progress.

The script goes through all files that are in the same directory as itself. It then reads out title, album, artist and track number via the Bandcamp file name. The collected informations gets added to the metadata of the files. It then creates a directory inside the current one and saves a copy of all songs named after the song.

<img title="Changes to files" alt="Image that shows changes" src="/images/before.png">

## How to use
Place Python file inside your album folder and run it with the following command:
```
python BC_MetadataFiller.py -sameDir
```





