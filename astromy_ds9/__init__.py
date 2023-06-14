# -*- encoding: utf-8 -*-
#                _
#      /\       | |
#     /  \   ___| |_ _ __ ___  _ __ ___  _   _
#    / /\ \ / __| __| '__/ _ \| '_ ` _ \| | | |
#   / ____ \\__ \ |_| | | (_) | | | | | | |_| |
#  /_/    \_\___/\__|_|  \___/|_| |_| |_|\__, |
#                                         __/ |
#                                        |___/
'''
@File    :   __init__.py
@Time    :   2023/06/14
@Author  :   Mingyu Li
@Contact :   lmytime@hotmail.com
'''

from .__version__ import __version__
import astropy.visualization as astrovi
import numpy as np

def v_percentile(data, pmin, pmax):
    """Quickly estimate percentiles in an array,
    using a downsampled version.
    Adapted from https://github.com/glue-viz/ds9norm

    data: array-like
    p_min: Lo percentile
    p_max: High percentile

    :rtype: Tuple of floats. Approximate values of each percentile in
            data[component]
    """

    shp = data.shape
    view = tuple([slice(None, None, max(s / 50, 1)) for s in shp])
    values = np.asarray(data)[view]
    if ~np.isfinite(values).any():
        return (0.0, 1.0)

    data = data[np.isfinite(data)]
    limits = (-np.inf, np.inf)
    vmin, vmax = np.percentile(data, [pmin, pmax])
    return vmin, vmax


def ds9_norm(vmin, vmax, bias=0.5, contrast=1, stretch='linear', stretch_param=None):
    """
    This function can be used to generate a Matplotlib Normalization
    to reproduce ds9 image inspection by dragging mouse.

    Input:
    vmin, vmax, bias, contrast, stretch.
    vmin, vmax: shown in `Scale Parameters` in ds9
    bias, contrast: shown in `Colormap Parameters` in ds9; bias is in [0, 1], contrast is in [0, +inf];
    bias=0.5, contrast=1 is the default setting.
    stretch : 
        Which stretch function to use. Defaults to 'linear'
    stretch_param: only used for 'power', 'asinh', and 'log' stretch.

    Return a Normalization class to be used with Matplotlib.
    """

    if stretch == 'linear':
        stretch = astrovi.LinearStretch()
    elif stretch == 'sqrt':
        stretch = astrovi.SqrtStretch()
    elif stretch == 'power':
        if(stretch_param is None):
            raise ValueError(
                "stretch_param must be provided for power stretch.")
        stretch = astrovi.PowerStretch(stretch_param)
    elif stretch == 'log':
        if(stretch_param is None):
            stretch_param = 1000
        stretch = astrovi.LogStretch(stretch_param)
    elif stretch == 'asinh':
        if(stretch_param is None):
            stretch_param = 0.1
        stretch = astrovi.AsinhStretch(stretch_param)
    elif stretch == 'sinh':
        if(stretch_param is None):
            stretch_param = 1./3.
        stretch = astrovi.SinhStretch(stretch_param)
    elif stretch == 'squared':
        stretch = astrovi.SquaredStretch()
    else:
        raise ValueError(f'Unknown stretch: {stretch}.')

    # Apply additional bias and contrast stretch
    stretch = astrovi.CompositeStretch(
        stretch, astrovi.ContrastBiasStretch(contrast, bias))

    norm = astrovi.ImageNormalize(
        stretch=stretch, vmin=vmin, vmax=vmax, clip=True)

    return norm


def ds9_norm_percentile(data, pmin, pmax, bias=0.5, contrast=1, stretch='linear', stretch_param=None):
    """
    This function can be used to generate a Matplotlib Normalization
    to reproduce ds9 image inspection by dragging mouse.

    Input:
    vmin, vmax, bias, contrast, stretch.
    vmin, vmax: shown in `Scale Parameters` in ds9
    bias, contrast: shown in `Colormap Parameters` in ds9; bias is in [0, 1], contrast is in [0, +inf];
    bias=0.5, contrast=1 is the default setting.
    stretch : 'linear' | 'log' | 'sqrt' | 'power' | 'squared' | 'asinh' | 'sinh
        Which stretch function to use. Defaults to 'linear'
    stretch_param: only used for 'power', 'asinh', and 'log' stretch.

    Return a Normalization class to be used with Matplotlib.
    """

    if stretch == 'linear':
        stretch = astrovi.LinearStretch()
    elif stretch == 'sqrt':
        stretch = astrovi.SqrtStretch()
    elif stretch == 'power':
        if(stretch_param is None):
            raise ValueError(
                "stretch_param must be provided for power stretch.")
        stretch = astrovi.PowerStretch(stretch_param)
    elif stretch == 'log':
        if(stretch_param is None):
            stretch_param = 1000
        stretch = astrovi.LogStretch(stretch_param)
    elif stretch == 'asinh':
        if(stretch_param is None):
            stretch_param = 0.1
        stretch = astrovi.AsinhStretch(stretch_param)
    elif stretch == 'sinh':
        if(stretch_param is None):
            stretch_param = 1./3.
        stretch = astrovi.SinhStretch(stretch_param)
    elif stretch == 'squared':
        stretch = astrovi.SquaredStretch()
    else:
        raise ValueError(f'Unknown stretch: {stretch}.')

    # Apply additional bias and contrast stretch
    stretch = astrovi.CompositeStretch(
        stretch, astrovi.ContrastBiasStretch(contrast, bias))

    vmin, vmax = v_percentile(data, pmin, pmax)
    norm = astrovi.ImageNormalize(
        stretch=stretch, vmin=vmin, vmax=vmax, clip=True)

    return norm
