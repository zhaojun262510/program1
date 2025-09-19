import torch
from torch.utils.data import DataLoader, TensorDataset

# 创建张量数据
x_data = torch.randn(100, 1)
y_data = 3 * x_data + 2 + torch.randn(100, 1) * 0.1

# 创建 TensorDataset 和 DataLoader
dataset = TensorDataset(x_data, y_data)
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

# 遍历数据加载器
for inputs, targets in dataloader:
    print(inputs, targets)