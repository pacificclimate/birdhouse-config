## Scripts
Helper scripts to recreate configuration files.

### `build_thredds`
Builds docker volume mount strings for `thredds` data.

#### Installation
```
python3 -m venv venv
pip install -r requirements.txt
```

#### Usage
```
python build_thredds.py /path/to/filepaths.txt ../docker-compose-extra.yml
```
