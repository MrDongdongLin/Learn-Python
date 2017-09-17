# Learn-Python
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

## Atom
Some packages
```
activate-power-mode
hydrogen
ctrl + enter: run a script
```
