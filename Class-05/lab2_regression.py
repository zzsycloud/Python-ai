import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# 固定随机种子，保证结果可复现
torch.manual_seed(42)

# ========== 1. 生成数据 ==========
x = torch.linspace(-1, 1, 100).reshape(-1, 1)          # 100个点，形状 (100, 1)
true_w, true_b = 2.5, -1.0
noise = 0.3 * torch.randn(x.size())
y = true_w * x + true_b + noise                         # y = 2.5x - 1 + 噪声

# ========== 2. 定义模型 ==========
class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)                   # 输入1维，输出1维

    def forward(self, x):
        return self.linear(x)

model = LinearRegression()

# ========== 3. 损失函数与优化器 ==========
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# ========== 4. 训练 ==========
epochs = 100
print("=" * 50)
print("线性回归训练输出")
print("=" * 50)

for epoch in range(epochs):
    # 前向传播
    y_pred = model(x)
    loss = criterion(y_pred, y)

    # 反向传播 + 更新
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1:3d}/{epochs}]  Loss: {loss.item():.6f}")

# 最终权重与偏置
w_final = model.linear.weight.item()
b_final = model.linear.bias.item()
print("-" * 50)
print(f"最终权重 w = {w_final:.4f}   (真实值: {true_w})")
print(f"最终偏置 b = {b_final:.4f}   (真实值: {true_b})")
print("=" * 50)

# ========== 5. 可视化 ==========
# 图1：散点图
plt.figure(figsize=(6, 4))
plt.scatter(x.numpy(), y.numpy(), s=12, alpha=0.6, label="Data (with noise)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression - Scatter Plot")
plt.legend()
plt.tight_layout()
plt.savefig("linear_scatter.png", dpi=150)
plt.show()

# 图2：拟合结果
plt.figure(figsize=(6, 4))
plt.scatter(x.numpy(), y.numpy(), s=12, alpha=0.4, label="Data")
x_line = torch.tensor([[-1.0], [1.0]])
y_line = model(x_line).detach()
plt.plot(x_line.numpy(), y_line.numpy(), color="red", linewidth=2, label="Fitted line")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Linear Regression Fit\nw={w_final:.3f}, b={b_final:.3f}")
plt.legend()
plt.tight_layout()
plt.savefig("linear_fit.png", dpi=150)
plt.show()