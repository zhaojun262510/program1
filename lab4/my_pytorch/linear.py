import torch
import torch.nn as nn
import torch.optim as optim

# 定义线性回归模型
model = nn.Linear(1, 1)

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 生成一些随机数据
x_train = torch.randn(100, 1)
y_train = 5 * x_train + 3 + torch.randn(100, 1) * 0.5

# 训练模型
for epoch in range(300):
    optimizer.zero_grad()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(f'Epoch [{epoch+1}/300], Loss: {loss.item():.4f}')