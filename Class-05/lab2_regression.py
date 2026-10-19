import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# ========== 2.1 数据准备 ==========
torch.manual_seed(0)
X = torch.linspace(-1, 1, 100).reshape(-1, 1)
y = 2 * X + 0.1 * torch.randn_like(X)

plt.scatter(X.numpy(), y.numpy())
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Data')
plt.show()

# ========== 2.2 构建模型 ==========
model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# ========== 2.3 训练模型 ==========
epochs = 100
for epoch in range(epochs):
    y_pred = model(X)
    loss = criterion(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.6f}')

W = model.weight.item()
b = model.bias.item()
print(f'Trained Weight: {W:.6f}, Trained Bias: {b:.6f}')

# ========== 2.4 模型评估 ==========
with torch.no_grad():
    y_pred = model(X)

plt.scatter(X.numpy(), y.numpy(), label='Data')
plt.plot(X.numpy(), y_pred.numpy(), label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Result')
plt.legend()
plt.show()