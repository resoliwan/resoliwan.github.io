# Goal
Make linear model to predict y value.

# Data
- x: birth_rate
- y: life_expectancy
- M: 190
```
Country	Birth_rate	Life_expectancy
Vietnam	1.822	74.828243902
Vanuatu	3.869	70.819487805
Tonga	3.911	72.150658537
```

# Plan
- Load data
  - define input and target.
- Create model
  - define forward model
  - define optimize model
    - define loss function.
- Train data
  - Optimize loss function.
- Measure performance.
  - predict data.
  - Get measure cost.

# Model
- Linear regression.

\\( f(x) = w * X + b\\)

\\( loss = (y - \hat y)^2\\)

\\( cost(\theta) = \sum_{i=0}^{M}loss(x^{(i)})\\)

# Code
### Use Place holder. 
```python
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

df = pd.read_csv('./examples/data/birth_life_2010.txt', delimiter='\t')
df.describe()
df.shape[0]
input_label = 'Birthrate'
target_label = 'Lifeexpectancy'

X = tf.placeholder(tf.float32, name='X')
y = tf.placeholder(tf.float32, name='y')
W = tf.get_variable('w', initializer=tf.constant(0.0))
b = tf.get_variable('b', initializer=tf.constant(0.0))
init_variables = tf.global_variables_initializer()

y_hat = tf.multiply(W, X) + b
loss = tf.sqrt((y - y_hat)**2)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-2).minimize(loss)

with tf.Session() as sess:
    sess.run(init_variables)
    writer = tf.summary.FileWriter('./graphs/linear_reg2', sess.graph)
    for batch in range(100):
        cost = 0
        for i in range(df.shape[0]):
            _, loss_out = sess.run([optimizer, loss], feed_dict={X: df[input_label][i], y: df[target_label][i]})
            cost += loss_out
        W_out, b_out = sess.run([W, b])
        print(W_out, b_out, cost)
    writer.close()


plt.scatter(df[input_label], df[target_label])
x_min = df[input_label].min()
x_max = df[input_label].max()
plt.plot([x_min, x_max], [W_out * x_min + b_out, W_out * x_max + b_out])
plt.show()
```
### Use dataset
```python
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

df = pd.read_csv('./examples/data/birth_life_2010.txt', delimiter='\t')
df.describe()
dataset = tf.data.Dataset.from_tensor_slices((df['Birthrate'], df['Lifeexpectancy']))
iterator = dataset.make_initializable_iterator()
X, y = iterator.get_next()

# with tf.Session() as sess:
#     sess.run(iterator.initializer)
#     sess.run(iterator.get_next())

W = tf.get_variable('weights', initializer=tf.constant(0.0, dtype=tf.float64))
b = tf.get_variable('bias', initializer=tf.constant(0.0, dtype=tf.float64))
y_hat = W * X + b
loss = tf.square(y - y_hat)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-3).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(100):
        sess.run(iterator.initializer)
        cost = 0
        try:
            while True:
                _, out_loss = sess.run([optimizer, loss])
                cost += out_loss
        except:
            pass
        out_W, out_b = sess.run([W, b])
        print('epoch %d out_W %f out_b %f cost %f' % (epoch, out_W, out_b, cost))
```

# Resource
- [stanford-tensorflow-tutorials](https://gitter.im/stanford-tensorflow-tutorials)

