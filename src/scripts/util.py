import skimage.util as skutil
import skimage.io as skio
import tensorflow as tf

def read_img(path):
  return tf.convert_to_tensor(skutil.img_as_float64(skio.imread(path)), dtype=tf.float64)

def tf_read_img(path):
  return tf.convert_to_tensor(tf.keras.utils.load_img(path=path, grayscale=False, color_mode="rgb"), dtype=tf.float64)
  