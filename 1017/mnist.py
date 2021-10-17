import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리 파일 가져올 수 있도록 설정
from dataset.mnist import load_mnist

(x_train, y_train), (x_test, y_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)