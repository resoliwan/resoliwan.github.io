# Softmax
# Goals
Input 값들을 다 합치면 1이 되는 확률값으로 변환해 주고 싶다.

그 이야기는 어떤 값이던 0 과 1 사이의 값을 리턴하는 함수를 만들고 싶다.

\\( \sigma: \mathbb {R} ^{K}\to (0,1)^{K} \\)

# Idea
예를들어 input 값이 [1,2,3] 일 경우 결과의  총합이 1이 되게 해줄려면 input을 다 더한값 6 = 1 + 2 + 3으로 모든 인풋값을 나누어 주면 된다.

\\( \sigma([1,2,3]) \to [\frac{1}{6},\frac{2}{6},\frac{3}{6}] \approx [0.16, 0.33, 0.5] \approx 1 \\)

위의 식을 정리하면 아래의 식이 된다.

\\( \sigma(\mathbf{z_{j}}) = {\frac {z_{j}}{\sum_{k=1}^{K}z_{k}}}\\)

위의 함수의 상수 z를 지수로 바꿔주자.  \\(z_j \to e^{z_j} \approx 2.71^{z_j}\\) 

\\( \sigma(\mathbf{z_{j}}) = {\frac{e^{z_{j}}}{\sum_{k=1}^{K}e^{z_{k}}}} \\)

그렇다 위의 식이 softmax 이며 우리의 예제를 계산하면

\\( \sigma([1,2,3]) \to [\frac{2.7}{30.2},\frac{7.3}{30.2},\frac{20.1}{30.2}] \approx [0.09, 0.24, 0.66] \approx 1 \\)

# Code
```py
import numpy as np
x = [1,2,3]
def softmax(x): 
    np.exp(x) / np.sum(np.exp(x))
```

