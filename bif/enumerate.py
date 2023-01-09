import os
files = list(enumerate(os.listdir(), 1))
# print(os.listdir())
cur_dir = os.getcwd()
print(cur_dir)
print(files)
