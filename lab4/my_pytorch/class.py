import torch
import torch.nn as nn
import torch.optim as optim

# 定义多分类模型
class MulticlassNN(nn.Module):
    def __init__(self):
        super(MulticlassNN, self).__init__()
        self.linear = nn.Linear(4, 3)

    def forward(self, x):
        return torch.softmax(self.linear(x), dim=1)

# 创建数据
x_train = torch.randn(10, 4)
y_train = torch.randint(0, 3, (10,))

# 实例化模型、损失函数和优化器
model = MulticlassNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练模型
for epoch in range(500):
    optimizer.zero_grad()
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/500], Loss: {loss.item():.4f}')