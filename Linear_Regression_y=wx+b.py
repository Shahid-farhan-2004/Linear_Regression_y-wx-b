import torch
import torch.nn as nn
X=torch.tensor([[1.0],[2.0],[3.0],[4.0]])
Y=torch.tensor([[2.0],[4.0],[6.0],[8.0]])

model=nn.Linear(in_features=1,out_features=1)
criterion=nn.MSELoss()
optimizer=torch.optim.SGD(model.parameters(),lr=0.01)

for epoch in range(1000):
    y_pred=model(X)
    loss=criterion(y_pred,Y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (epoch+1)%100==0:
        print(f'{epoch+1} : {loss.item():.4f}')
params=list(model.parameters())
print(f"learned weight:{params[0].item()}  and   learned bias:{params[1].item()}")
print("the equation is :")
print(f"Y={params[0].item():.2f}X+{params[1].item():.2f}")

num=int(input("enter the number"))
new_tensor=torch.tensor([[num]],dtype=torch.float32)
new_value=model(new_tensor)
print(new_value.item())

