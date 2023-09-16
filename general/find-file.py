import os

# set current path
cur_path = os.getcwd()

# file to search for
file_search = 'findme'

# store search results, set level up dirs
files_found = []
levels_up = 2

# set your directory to the top most level
counter = 0
while True:
	parent_dir = os.path.dirname(cur_path)
	if parent_dir == cur_path:
		break
	else:
		cur_path = parent_dir
		counter += 1

	if counter >= levels_up:
		break

print(f"Search starting at: {parent_dir}")


# start searching
for filepath, _, files in os.walk(cur_path):
	for file in files:
		if file.__contains__(file_search):
			files_found.append(os.path.join(filepath, file))


print(files_found)

