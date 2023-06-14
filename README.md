# Reproducing SAOImageDS9 Colormap in Python

**Check example code in [nbviewer](https://nbviewer.org/github/lmytime/Reproduce_DS9_colormap_in_Python/blob/main/norm_ds9.ipynb).**


## Installation
```sh
pip install ds9_norm
```

## Usage
```python
from astromy_ds9 import ds9norm


import astropy
import matplotlib.pyplot as plt
data = astropy.io.fits.getdata('https://github.com/glue-viz/ds9norm/raw/master/m51.fits')

norm = ds9_norm(vmin=3053.38, vmax=13513.9, bias=0.581921, contrast=0.890152, stretch='sqrt')
plt.imshow(data, norm=norm, cmap='gray', origin='lower', interpolation='None')
```

There are 5 input parameters for `ds9_norm` function.
- `vmin` and `vmax`: you can find the values in `Scale` -> `Scale Parameters` -> Below the histogram, Low is `vmin` and High is `vmax`.
- `bias` and `contrast`: you can find the values in `Color` -> `Color Parameters`
- `stretch`: you can find it in `Scale` -> see which one is marked with a check mark. Allowed values are 'linear' | 'log' | 'sqrt' | 'power' | 'squared' | 'asinh' | 'sinh'.



## Methodology
Please check the methodology in [`doc`](https://github.com/lmytime/Reproduce_DS9_colormap_in_Python/tree/main/docs). Also see [ds9norm](https://github.com/glue-viz/ds9norm) for reference.