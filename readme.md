# uxrd

A X-ray diffraction library with some usefull functions. 

## Installation

TBA

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
```

## License
 Jonas Ångström 2020
[MIT] (https://choosealicense.com/licenses/mit/)
