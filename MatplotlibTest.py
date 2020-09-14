import matplotlib.pyplot as plt
import numpy as np

#简单的绘图
x = np.linspace(0, 2 * np.pi, 50)

#如果没有第一个参数x，图形的x坐标默认为数组的索引
plt.plot(x, np.sin(x), 'r-o', x, np.sin(2 * x), 'g--')
x = np.random.randn(1000)
plt.hist(x,50)
plt.show()