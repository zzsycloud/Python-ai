import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

torch.manual_seed(42)

# ========== 1. 生成二分类数据 ==========
n_per_class = 100
# 类别 0：中心在 (-1.5, -1.0)
x0 = torch.randn(n_per_class, 2) * 0.7 + torch.tensor([-1.5, -1.0])
# 类别 1：中心在 (1.5, 1.0)
x1 = torch.randn(n_per_class, 2) * 0.7 + torch.tensor([1.5, 1.0])

X = torch.cat([x0, x1], dim=0)                          # (200, 2)
y = torch.cat([torch.zeros(n_per_class), torch.ones(n_per_class)]).reshape(-1, 1)  # (200, 1)

# ========== 2. 定义模型 ==========
class LogisticRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 1)                   # 输入2维，输出1维 logit

    def forward(self, x):
        return self.linear(x)                            # 返回 logit，不手动 sigmoid

model = LogisticRegression()

# ========== 3. 损失函数与优化器 ==========
criterion = nn.BCEWithLogitsLoss()                       # 自带 sigmoid，数值更稳定
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# ========== 4. 训练 ==========
epochs = 200
print("=" * 50)
print("逻辑回归训练输出")
print("=" * 50)

for epoch in range(epochs):
    logits = model(X)
    loss = criterion(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 20 == 0:
        # 计算准确率
        with torch.no_grad():
            probs = torch.sigmoid(logits)
            preds = (probs > 0.5).float()
            acc = (preds == y).float().mean().item()
        print(f"Epoch [{epoch+1:3d}/{epochs}]  Loss: {loss.item():.6f}  Acc: {acc:.4f}")

# 最终权重与偏置
w_final = model.linear.weight.detach().numpy().flatten()
b_final = model.linear.bias.item()
print("-" * 50)
print(f"最终权重 w = [{w_final[0]:.4f}, {w_final[1]:.4f}]")
print(f"最终偏置 b = {b_final:.4f}")

# 最终准确率
with torch.no_grad():
    probs = torch.sigmoid(model(X))
    preds = (probs > 0.5).float()
    final_acc = (preds == y).float().mean().item()
print(f"最终准确率 Accuracy = {final_acc:.4f}")
print("=" * 50)

# ========== 5. 可视化 ==========
# 图3：数据散点图
plt.figure(figsize=(6, 5))
plt.scatter(x0[:, 0].numpy(), x0[:, 1].numpy(), s=12, alpha=0.6, label="Class 0")
plt.scatter(x1[:, 0].numpy(), x1[:, 1].numpy(), s=12, alpha=0.6, label="Class 1")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Logistic Regression - Data Scatter")
plt.legend()
plt.tight_layout()
plt.savefig("logistic_scatter.png", dpi=150)
plt.show()

# 图4：决策边界
plt.figure(figsize=(6, 5))
plt.scatter(x0[:, 0].numpy(), x0[:, 1].numpy(), s=12, alpha=0.5, label="Class 0")
plt.scatter(x1[:, 0].numpy(), x1[:, 1].numpy(), s=12, alpha=0.5, label="Class 1")

# 决策边界：w1*x1 + w2*x2 + b = 0  =>  x2 = -(w1*x1 + b) / w2
x1_range = np.linspace(X[:, 0].min().item() - 0.5, X[:, 0].max().item() + 0.5, 100)
x2_boundary = -(w_final[0] * x1_range + b_final) / w_final[1]
plt.plot(x1_range, x2_boundary, color="red", linewidth=2, label="Decision Boundary")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title(f"Logistic Regression - Decision Boundary\nAcc={final_acc:.3f}")
plt.legend()
plt.tight_layout()
plt.savefig("logistic_boundary.png", dpi=150)
plt.show()