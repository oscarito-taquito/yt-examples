import os
import datetime as dt

cur_path = os.getcwd()
files = os.listdir(cur_path)
now = dt.datetime.today()


# capture file information
def file_info(cd, file_list, today):
    file_dict = {}
    for file in file_list:
        file_path = os.path.join(cd, file)

        # retrieve file times, convert from epoc to datetime
        created = os.stat(file_path)
        created = dt.datetime.fromtimestamp(created.st_birthtime)
        modified = dt.datetime.fromtimestamp(os.path.getmtime(file_path))

        # compute age in days
        since_created = int((today - created).total_seconds() / (60 * 60 * 24))
        since_mod = int((today - modified).total_seconds() / (60 * 60 * 24))

        # append list of file info into dictionary
        file_dict[file] = [file_path, file, f"{created}", f"{modified}", since_created, since_mod]

    return file_dict


dir_listing = file_info(cur_path, files, now)
print(dir_listing)

dir_listing_sort = sorted(dir_listing.items(), key=lambda x: x[1][5])

for k, v in dir_listing_sort:
    print(v[1], v[5])
    if v[5] > 250:
        # os.remove(v[0])
        print('Delete File')
    else:
        print('Keep File')

print(dict(dir_listing_sort))
