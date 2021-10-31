import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image
import numpy as np

(x_train, y_train), (x_test, y_test) = load_mnist(normalize=False, flatten=True)

img = x_train[12000]
label = y_train[12000]
print(label)

img = img.reshape(28, 28)
pil_img = Image.fromarray(np.uint8(img))
pil_img.show()