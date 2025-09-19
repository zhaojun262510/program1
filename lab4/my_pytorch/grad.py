import torch

# 创建一个张量并启用自动求导
x = torch.tensor(2.0, requires_grad=True)

# 计算一个简单的函数
y = x ** 2 + 3 * x + 1

# 反向传播计算梯度
y.backward()

# 查看梯度
print(f"x的梯度: {x.grad}")