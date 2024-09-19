import pathlib

path = pathlib.Path.home()
cwd = pathlib.Path.cwd  # current working directory

list(path.iterdir()) # lists all paths in a dir

new_directory = path / "new_dir" # creates a path for the dir - dir is not created yet
new_directory.mkdir()  # this now creates the actual directory - raises exceptions if dir doesn't exist
new_directory.mkdir(exist_ok=True) # no exception raised
new_directory.mkdir(parents=True)  # non-existent directories in path are created

new_file = path / "new_dir" / "new_file.py" # creates a path for the file - file not created yet
new_file.touch() # creates a file in a given path

path.exists() # checks if path exists

list(new_directory.glob("*.py")) # searches all files and directories matching pattern in a dir - only current dir,no subdir's 
list(new_directory.rglob("*.py")) # searches recursively on all files/dir's/subdir's

# Moving files
source = new_directory / "file.py"
dest = new_directory / "folder_a" / "file.py"
source.replace(dest)

