import torch

print(f"Versione PyTorch: {torch.__version__}")
print(f"GPU disponibile: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"Nome GPU: {torch.cuda.get_device_name(0)}")
    print(f"Versione CUDA di Torch: {torch.version.cuda}")