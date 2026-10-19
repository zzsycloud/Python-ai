import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# ========== 3.1 数据准备 ==========
np.random.seed(0)
X_np = np.random.rand(100, 2).astype(np.float32)
y_np = ((X_np[:, 0] + X_np[:, 1]) > 1.0).astype(np.float32).reshape(-1, 1)

X = torch.tensor(X_np)
y = torch.tensor(y_np)

plt.scatter(X_np[:, 0], X_np[:, 1], c=y_np.ravel(), cmap='coolwarm')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Logistic Regression Data')
plt.show()

# ========== 3.2 构建模型 ==========
model = nn.Linear(2, 1)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

# ========== 3.3 训练模型 ==========
epochs = 100
for epoch in range(epochs):
    logits = model(X)
    loss = criterion(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.6f}')

# 训练结束后：Sigmoid 得到类别1概率，以0.5为阈值生成预测标签，并计算准确率
with torch.no_grad():
    logits = model(X)
    probs = torch.sigmoid(logits)
    preds = (probs > 0.5).float()
    accuracy = (preds == y).float().mean()

    print(f'Final Accuracy: {accuracy.item():.4f}')