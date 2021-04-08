import pyqrcode
import png
from pyqrcode import QRCode

def qrgen(s, name):
    url = pyqrcode.create(s)
    filename = '/tmp/' + name + '.png'
    url.png(filename, scale=6)
