# Transistor_Database_Exchange
This is the file exchange for the [transistor database](https://github.com/upb-lea/transistordatabase). Please also refer to the README.md of this project.

## load the transistors stored in the file exchange to your local transistor database
Make shure that you have installed the latest version of the transistor database.
```
import transistordatabase as tdb
tdb.update_from_fileexchange()
```

## Share your transistors with the world
Use your local generated transistor, load it into your workspace and export it, e.g.
```
transistor_loaded = load({'name': 'CREE_C3M0016120K'})
transistor_loaded.export_json()
```
You can upload this file to this repository by generating a pull request.
