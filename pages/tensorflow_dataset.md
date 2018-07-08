# Dataset
Abstract object for data feeding.

# Iterator
```python
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import sys

df = pd.read_csv('./examples/data/birth_life_2010.txt', delimiter='\t')
df.describe()
dataset = tf.data.Dataset.from_tensor_slices((df['Birthrate'], df['Lifeexpectancy']))

one_iterator = dataset.make_one_shot_iterator()
with tf.Session() as sess:
    for i in range(100):
        sess.run(one_iterator.get_next())

iterator = dataset.make_initializable_iterator()
with tf.Session() as sess:
    for i in range(2):
        sess.run(iterator.initializer)
        try: 
            while True:
                sess.run(iterator.get_next())
        except tf.errors.OutOfRangeError:
            print("Unexpected error:", sys.exc_info()[0])
            print('error')
            pass
```

# Tag
- tensorflow
- dataset
- iterator
