import os
import time
import datetime as dt

cur_path = os.getcwd()
files = os.listdir(cur_path)
now = dt.datetime.today()


def file_info(cd, file_list, today):
    info_list = []
    for f in files:
        file = os.path.join(cur_path, f)
        created = dt.datetime.fromtimestamp(os.path.getctime(file))
        modified = dt.datetime.fromtimestamp(os.path.getctime(file))
        since_created = abs(int((today - created).total_seconds()))
        since_mod = abs(int((today - modified).total_seconds()))
        info_list.append((file, created, modified, since_created, since_mod))

    return info_list


t = file_info(cur_path, files, now)

for fn, c, m, sc, sm in t:
    print(fn, sc)
    if sm/(60 * 60) < 1:
        print(f'Newer than an hour {fn}')
    else:
        print(f'Older than an hour {fn}')



