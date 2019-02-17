# # Extract
# files = tf.data.Dataset.list_files(file_pattern)
# dataset = tf.data.TFRecordDataset(files)
# # transfer
#
# # dataset = dataset.shuffle(10000)
# # dataset = dataset.repeat(NUM_EPOCHS)
#
# dataset = dataset.apply(
#     tf.contrib.data.shuffle_and_repeat(10000, NUM_EPOCHS)
# )
#
# # dataset = dataset.map(lambda x: tf.parse_single_example(x, features))
# # dataset = dataset.batch(BATCH_SIZE)
#
# dataset = dataset.apply(
#     tf.contrib.data.map_and_batch(lambda x: ..., BATCH_SIZE)
# )
#
# dataset = dataset.apply(tf.contrib.data.prefetch_to_device("/gpu: 0"))
#
# # load
# iterator = dataset.make_one_shot_iterator()
# features = iterator.get_new()


import tensorflow as tf
from glob import glob
import numpy as np

directory = "crawling/fish"
dirs = glob(directory + "/*/")
image_list = []
label_list = []
label = 0

for dir in dirs:
    tFiles = glob(dir + '*.jpg')
    image_list.extend(tFiles)
    tLabels = np.ones(len(tFiles)) * label
    label_list.extend(tLabels)
    # print(tLabels)
    label += 1

#
# def _read_py_function(path, label):
#     image = read_image(path)
#     label = np.array(label, dtype=np.uint8)
#     return image.astype(np.int32), label
#
#
# def _resize_function(image_decoded, label):
#     image_decoded.set_shape([None, None, None])
#     image_resized = tf.image.resize_images(image_decoded, [28, 28])
#     return image_resized, label
#
#
# dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))
# # dataset = dataset.map(
# #     lambda data_list, label_list: tuple(tf.py_func(_read_py_function, [data_list, label_list], [tf.int32, tf.uint8])))
# # dataset = dataset.map(_resize_function)
#
# # dataset = dataset.repeat()
# # dataset = dataset.shuffle(buffer_size=(int(len(data_list) * 0.4) + 3 * batch_size))
# # dataset = dataset.batch(batch_size)
# iterator = dataset.make_initializable_iterator()
# image_stacked, label_stacked = iterator.get_next()
# next_element = iterator.get_next()
#
# # Image와 Label 하나 열어보기
# with tf.Session() as sess:
#     sess.run(iterator.initializer)
#     image, label = sess.run([image_stacked, label_stacked])


def img_decode_tf(path, label):
    reshaped_image = tf.image.decode_image(tf.read_file(path), channels=3)
    distorted_image = tf.random_crop(reshaped_image, [32, 32, 3])
    distorted_image = tf.image.random_flip_left_right(distorted_image)
    distorted_image = tf.image.random_brightness(distorted_image,max_delta=63)
    distorted_image = tf.image.random_contrast(distorted_image,lower=0.2, upper=1.8)
    float_image = tf.image.per_image_standardization(distorted_image)

    return float_image, label

dataset = tf.data.Dataset.from_tensor_slices((image_list, label_list))
dataset = dataset.map(img_decode_tf, num_parallel_calls=3)

imgs = dataset.make_one_shot_iterator().get_next()

with tf.Session() as sess:
    while True:
        try:
            img, label = sess.run(imgs)
        except tf.errors.OutOfRangeError:
            break