# Learn-Python
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/MrDongdongLin/Learn-Python)
[![Packagist](https://img.shields.io/badge/packgist-v1.1.0-orange.svg)](https://github.com/MrDongdongLin/Learn-Python/releases)
[![Powerby](https://img.shields.io/badge/powerby-DongdongLin-blue.svg)](https://github.com/MrDongdongLin)

This packages recodes come study notes of Python

## python-opencv
To use opencv in python, some packages must be installed:
```python
pip install opencv-python
pip install numpy
pip install matplotlib
```

- Read an image and show
```python
import cv2

img = cv2.imread('img.bmp')
cv2.imshow('title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
or use matplotlib
```python
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.bmp')
plt.imshow(img)
plt.show()
```

More informations can be found [here](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html).

## numpy
Ref [here](https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html) to see the difference of numpy and Matlab.

## matplotlib
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.

Q: How to remove the axes and the white margin of an image object that ploted by pyplot?
A:
```python
from matplotlib import pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial'], 'size': 8})
params = {'text.usetex': False, 'mathtext.fontset': 'stixsans'}
plt.rcParams.update(params)

fig = plt.imshow(img, 'gray')
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig('saveimg.pdf', bbox_inches='tight', pad_inches = 0)
plt.close()
```

## nolds
Nolds only consists of a single module called nolds which contains all relevant algorithms and helper functions.
[DOCUMENT](https://cschoel.github.io/nolds/nolds.html)

### Algorithms
- Lyapunov exponent (Rosenstein et al.)
```python
nolds.lyap_r(data, emb_dim=10, lag=None, min_tsep=None, tau=1, min_neighbors=20, trajectory_len=20, fit='RANSAC', debug_plot=False, debug_data=False, plot_file=None, fit_offset=0, min_vectors=None)
```
- Lyapunov exponent (Eckmann et al.)
```python
nolds.lyap_e(data, emb_dim=10, matrix_dim=4, min_nb=None, min_tsep=0, tau=1, debug_plot=False, debug_data=False, plot_file=None)
```
### mesures.py
```python
def test_lyap():
  ...
  # return Largest Lyapunov Exponent (le).
  le = lyap_e(np.array(full_data), emb_dim=6, matrix_dim=2)
  ...
```

## Atom
Some packages
```
activate-power-mode
hydrogen
ctrl + enter: run a script
```
