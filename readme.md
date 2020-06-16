# uxrd

A X-ray diffraction library with some usefull functions.

## Installation

clone using git and install

```bash
git clone https://github.com/jonasangstrom/uxrd.git
cd uxrd
pip install . 
```

## Usage

```python
import uxrd

brml_path = 'my_brml.brml'
data = uxrd.read_brml(brml_path) # reads brml file
dat_path = 'my_dat.dat'
uxrd.write_dat(dat_path, data) # writes datfile

uxrd.convert_all_brml_in_folder() # convert all brml in dir to dat
```

## License
[MIT](https://choosealicense.com/licenses/mit/) Jonas Ångström 2020
