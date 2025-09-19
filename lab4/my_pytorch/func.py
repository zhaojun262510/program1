import torch
import torch.nn as nn
import torch.nn.functional as F

# 创建一个简单的模型
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.linear = nn.Linear(10, 2)

    def forward(self, x):
        x = self.linear(x)
        return F.relu(x)  # 使用 torch.nn.functional 中的激活函数

# 实例化模型并使用
model = SimpleNN()
x = torch.randn(1, 10)
output = model(x)
print(output)