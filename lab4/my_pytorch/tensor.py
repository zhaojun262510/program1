import torch

# 创建两个张量
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# 加法操作
c = a + b

# 逐元素乘法
d = a * b

print("a + b = \n", c)
print("a * b = \n", d)