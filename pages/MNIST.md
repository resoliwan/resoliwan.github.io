# MNIST
# Goal
Predict category of images.

# Data
- X: digit image of 28 * 28 pixels. 
  - 1-d 784 pixel vector.
- y: the value of image (0~9)
```
label,pixel0,...,pixel783
1    ,     0,...,0
```
# Plan
- Load data
  - make X to (784, m)
  - make y to (10, m) using one hot encoder.
- Create model
  - define forward model.
  - define optimize model.
    - define loss function.
- Train data.
  - optimize loss function.
- Measure performance

# Model
### Linear regression
#### Forward Model
\\( f(x) = W \cdot X + b \\)
- X: (784, m), W (1, 784), b (1, 1)

#### Loss
\\( H_{p}(q) = \sum_{x} q(x) *\log_{2} \frac{1}{\log p(x)} \\)
- Cross-Entroy: Average length of message from q(x) using code for p(x)

#### Cost
\\( cost(\theta) = \sum_{i=0}^{M}loss(x^{(i)})\\)

# Resource
- [Information theory](http://colah.github.io/posts/2015-09-Visual-Information)
- [stanford-tensorflow-tutorials](https://gitter.im/stanford-tensorflow-tutorials)


