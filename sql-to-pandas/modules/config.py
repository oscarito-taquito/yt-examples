import os


def data_path():
    cur_dir = os.getcwd()
    os.chdir('..')
    cwd = os.getcwd()
    dp = os.path.join(cwd, 'data')
    os.chdir(cur_dir)
    return dp


if __name__ == "__main__":
    data_path()
