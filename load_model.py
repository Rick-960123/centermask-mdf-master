import torch

original = torch.load('./model_final.pth')

new = {"model": original["model"]}
torch.save(new, './weight.pth')