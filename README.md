# Transistor_Database_Exchange
This is the file exchange for the [transistor database](https://github.com/upb-lea/transistordatabase). Please also refer to the README.md of this project.

## Example on how to update the local Transistordatabase.
Make sure that you have installed the latest version of the transistor database.
```
# Path for the database
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tdb_example_downloaded")

# URLS
# index_url: Points to the file with contains the URLs for every transistor which shall be downloaded
# module_manufacturers_url: Points to the file containing the module manufacturers
# housing_types_url: Points to the file containing the housing types
index_url = r"https://raw.githubusercontent.com/upb-lea/transistordatabase_File_Exchange/main/index.txt"
module_manufacturers_url = r"https://raw.githubusercontent.com/upb-lea/transistordatabase_File_Exchange/main/module_manufacturers.txt"
housing_types_url = r"https://raw.githubusercontent.com/upb-lea/transistordatabase_File_Exchange/main/housing_types.txt"

# Create instance of the DatabaseManager and set it as a json database.
db = DatabaseManager()
db.set_operation_mode_json(path)

# Update local database
db.update_from_fileexchange(index_url, True, module_manufacturers_url, housing_types_url)
```

## Share your transistors with the world
Use your local generated transistor, load it into your workspace and export it, e.g.
```
transistor_loaded = transistor_database.load_transistor("CREE_C3M0016120K")
transistor_loaded.export_json()
```
You can upload this file to this repository by generating a pull request.

## For developers
When adding new transistors to this repository please either manually add a link to the index.txt or run the script create_index.py in order to create
it automatically. If you are using new module manufacturers or housing types please add them to the files.