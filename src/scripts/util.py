import skimage.util as skutil
import skimage.io as skio
import tensorflow as tf
import numpy as np
import numpy.typing as npt
import pandas as pd


def read_img(path: str) -> npt.NDArray[np.float64]:
  return tf.convert_to_tensor(skutil.img_as_float64(skio.imread(path)), dtype=tf.float64)

def pd_series_to_np_img(series: pd.Series) -> npt.NDArray[np.float64]:
  vanilla_list = list(series.values)
  return np.array(vanilla_list, dtype=np.float64)

def pd_series_to_tensor(series: pd.Series) -> tf.Tensor:
    vanilla_list = list(series.values)
    return tf.convert_to_tensor(vanilla_list, dtype=tf.float64)


def tf_read_img(path):
  return tf.convert_to_tensor(tf.keras.utils.load_img(path=path, grayscale=False, color_mode="rgb"), dtype=tf.float64)

