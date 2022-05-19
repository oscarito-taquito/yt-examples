import os
import shutil
path1 = '/Users/oscar/github/yt-examples/data/temp-upload.csv'
path2 = '/Users/oscar/github/yt-examples/general/temp-upload.csv'

os.rename(path1, path2)

shutil.move(path2, path1)