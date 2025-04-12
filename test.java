import matpolibplot as plt
import numpy as np
np.random.seed(0)
data = np.random.randn(1000, 2)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap with Colorbar')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
