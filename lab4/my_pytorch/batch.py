import torch
import torch.nn as nn

# 定义一个简单的网络带批归一化
class SimpleNetWithBN(nn.Module):
    def __init__(self):
        super(SimpleNetWithBN, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.bn1 = nn.BatchNorm1d(20)
        self.fc2 = nn.Linear(20, 1)

    def forward(self, x):
        x = self.bn1(self.fc1(x))
        return self.fc2(x)

# 实例化模型并使用
x = torch.randn(5, 10)
model = SimpleNetWithBN()
output = model(x)
print(output)