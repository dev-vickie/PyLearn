import pathlib

path = pathlib.Path.home()
cwd = pathlib.Path.cwd  # current working directory

list(path.iterdir()) # lists all paths in a dir

new_directory = path / "new_dir" # creates a path for the dir - dir is not created yet
new_directory.mkdir()  # this now creates the actual directory - raises exceptions if dir doesn't exist
new_directory.mkdir(exist_ok=True) # no exception raised
new_directory.mkdir(parents=True)  # 

new_file = path / "new_dir" / "new_file.py" # creates a path for the file - file not created yet
new_file.touch() # creates a file in a given path


