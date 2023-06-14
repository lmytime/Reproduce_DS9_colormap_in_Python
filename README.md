# Reproducing SAOImageDS9 Colormap in Python

[SAOImageDS9](https://sites.google.com/cfa.harvard.edu/saoimageds9) is an image display and visualization tool for astronomical data, which can be used for fast image processing and inspection. In DS9, we can drag the mouse on the image viewer to manipulate the colormap and then visualize data effectively and quickly. Unlike the DS9, color normalization and stretch in Python should be set manually.

Here we take notes about how to reproduce the colormap of DS9 in Python, supposing that you have already tuned the colormap parameters in DS9.


## Installation
```sh
pip install astromy_ds9
```

## Usage
```python
from astromy_ds9 import ds9_norm


import astropy
import matplotlib.pyplot as plt
data = astropy.io.fits.getdata('https://github.com/lmytime/Reproduce_DS9_colormap_in_Python/raw/main/doc/data/m51.fits')

norm = ds9_norm(vmin=3053.38, vmax=13513.9, bias=0.581921, contrast=0.890152, stretch='sqrt')
plt.imshow(data, norm=norm, cmap='gray', origin='lower', interpolation='None')
```

There are 5 input parameters for `ds9_norm` function.
- `vmin` and `vmax`: you can find the values in `Scale` -> `Scale Parameters` -> Below the histogram, Low is `vmin` and High is `vmax`.
- `bias` and `contrast`: you can find the values in `Color` -> `Color Parameters`
- `stretch`: you can find it in `Scale` -> see which one is marked with a check mark. Allowed values are 'linear' | 'log' | 'sqrt' | 'power' | 'squared' | 'asinh' | 'sinh'.

<img src="https://github.com/lmytime/Reproduce_DS9_colormap_in_Python/blob/main/doc/figs/help.png?raw=true" alt="help"/>


**Check example code in [test](https://nbviewer.org/github/lmytime/Reproduce_DS9_colormap_in_Python/blob/main/doc/test.ipynb) and [example](https://nbviewer.org/github/lmytime/Reproduce_DS9_colormap_in_Python/blob/main/doc/example.ipynb).**


## Methodology
Please check the methodology in [`doc`](https://github.com/lmytime/Reproduce_DS9_colormap_in_Python/tree/main/doc). Also see [ds9norm](https://github.com/glue-viz/ds9norm) for reference.

## Citation
If you find this useful, please acknowledge.