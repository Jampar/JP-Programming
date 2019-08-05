from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

class ImageHandler:

    def preprocess_and_decode(self, img_path):
        img_raw = tf.read_file(img_path)
        img_tensor = tf.image.decode_image(img_raw)

        img_final = tf.image.resize(img_tensor, [1000, 1000])
        img_final = img_final / 255.0

        return img_final