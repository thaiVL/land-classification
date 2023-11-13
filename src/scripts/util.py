import skimage.util as skutil
import skimage.io as skio

def read_img(path):
  return skutil.img_as_float64(skio.imread(path))