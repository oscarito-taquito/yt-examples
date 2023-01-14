import os
import datetime as dt

cur_path = os.getcwd()
files = os.listdir(cur_path)
now = dt.datetime.today()


# capture file information
def file_info(cd, file_list, today):
    file_dict = {}
    for file in files:
        file_path = os.path.join(cur_path, file)

        # retrieve file times, convert from epoc to datetime
        created = dt.datetime.fromtimestamp(os.path.getctime(file_path))
        modified = dt.datetime.fromtimestamp(os.path.getctime(file_path))

        # compute age in days
        since_created = abs(int((today - created).total_seconds())) / (60 * 60 * 24)
        since_mod = abs(int((today - modified).total_seconds())) / (60 * 60 * 24)

        # append tuple of file info collected into list
        file_dict[file] = [file_path, file, f'{created}', f'{modified}', since_created, since_mod]

    return file_dict


dir_listing = file_info(cur_path, files, now)
print(dir_listing)

dir_listing_sort = sorted(dir_listing.items(), key=lambda x: x[1][4])
for k, v in dir_listing_sort:
    print(v[1], v[4])


print(dict(dir_listing_sort))