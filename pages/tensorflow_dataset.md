# Goal
- Provide data abstraction.

- tf.Data.Dataset
  - Represent sequence of elements.
  - Creating from source.(tf.Tensor)
  - Creating from tf.dataset using Transformation.

- tf.data.Iterator
  - Provide main way to extract data from Dataset

# Sample data
```
l,d0,d1,d2,d3,d4
0,1,2,3,4
1,11,12,13,14
2,21,22,23,24

```

```
import pandas as pd
import tensorflow as tf
import numpy as np

df = pd.read_csv('./data/test.csv')
df.describe()

dm = df.as_matrix()
y = dm[:, 0]
x = dm[:, 1:]

max = np.max(dm[:, 0]) + 1
onehot_y = np.eye(max)[dm[:, 0]]

dataset = tf.data.Dataset.from_tensor_slices(({'x': x, 'onehot_y': onehot_y}))
iterator = dataset.make_initializable_iterator()
X, y = iterator.get_next()

with tf.Session() as sess:
    for e in range(3):
        sess.run(iterator.initializer)
        try:
            while True:
                X_out, y_out = sess.run([X, y])
                print('X_out', X_out)
                print('y_out', y_out)
        except tf.errors.OutOfRangeError:
            print('OutOfRangeError')
            pass
```


# Tag
- tensorflow
- dataset
- iterator
