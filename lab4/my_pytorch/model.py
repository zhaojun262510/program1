import torch
import torch.nn as nn
import torch.optim as optim

# 定义一个简单的线性模型
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

# 实例化模型
model = LinearModel()

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
# 生成一些随机数据
x_train = torch.randn(100, 1)
y_train = 3 * x_train + 2 + torch.randn(100, 1) * 0.1
# 训练模型
for epoch in range(500):
    optimizer.zero_grad()
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/500], Loss: {loss.item():.4f}')