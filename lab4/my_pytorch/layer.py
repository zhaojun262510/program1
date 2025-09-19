import torch
import torch.nn as nn

# 自定义简单的神经网络层
class CustomLayer(nn.Module):
    def __init__(self):
        super(CustomLayer, self).__init__()
        self.weight = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return x * self.weight

# 使用自定义层
x = torch.randn(1, 10)
layer = CustomLayer()
output = layer(x)
print(output)