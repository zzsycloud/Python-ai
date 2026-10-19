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
epochs = 200
for epoch in range(epochs):
    logits = model(X)
    loss = criterion(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        print(f'Epoch {epoch:3d}, Loss: {loss.item():.6f}')

with torch.no_grad():
    prob = torch.sigmoid(model(X))
    pred = (prob >= 0.5).float()
    acc = (pred == y).float().mean()

print('Trained Weight:', model.weight.detach().numpy())
print('Trained Bias:', model.bias.detach().numpy())
print(f'Training Accuracy: {acc.item() * 100:.2f}%')

# ========== 3.4 模型评估：概率等高图 + 0.5 决策边界 ==========
x_min, x_max = -0.1, 1.1
y_min, y_max = -0.1, 1.1
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 300),
    np.linspace(y_min, y_max, 300)
)
grid = torch.tensor(np.c_[xx.ravel(), yy.ravel()], dtype=torch.float32)

with torch.no_grad():
    Z = torch.sigmoid(model(grid)).numpy().reshape(xx.shape)

plt.contourf(xx, yy, Z, levels=np.linspace(0, 1, 11), cmap='coolwarm', alpha=0.55)
plt.contour(xx, yy, Z, levels=[0.5], colors='black')
plt.scatter(X_np[:, 0], X_np[:, 1], c=y_np.ravel(), cmap='coolwarm')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Logistic Regression Decision Boundary')
plt.show()