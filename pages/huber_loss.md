# Huber loss

# Goal
Want less sensitive function to the outliers than the square error loss.

# How to
- Use square function for small value.
- Use absolute function for large value.

### IDEA
\\(
f(a) =
\begin{cases}
a^2                     & \text{for }|a| \leq 1, \\\
|a|                     & \text{ otherwise}
\end{cases}
\\)
### Huber loss
\\(
L_{\delta}(a) =
\begin{cases}
\frac{1}{2}a^2                     & \text{for }|a| \leq \delta, \\\
\delta (|a| - \frac{1}{2} \delta), & \text{ otherwise}
\end{cases}
\\)

# Graph
![img](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Huber_loss.svg/720px-Huber_loss.svg.png)
- Huber loss is green (\\( \delta = 1 \\))
- squared error loss is blue

# Code
```python
import tensorflow as tf
import pandas as pd
import numpy as np
import math


def huber_loss(y, y_hat, delta):
    diff = math.abs(y - y_hat)
    if diff < delta:
        return 0.5 * diff**2
    else:
        return delta * diff - 0.5 * delta**2


def huber_loss(y, y_hat, delta=1.0):
    residual = tf.abs(y - y_hat)
    def square_f(): return 0.5 * tf.square(residual)
    def abs_f(): return delta * residual - 0.5 * tf.square(delta)
    return tf.cond(residual < delta, square_f, abs_f)
```

# Tag
- loss function
- ml
- huber loss
