import torch
import math

# Check for Apple Silicon GPU (MPS)
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print("✅ Success: M1 Max GPU is Active (MPS Enabled)!")
else:
    print("❌ Error: Running on CPU. Something is wrong.")

# Simple Quant Test
import talib
import numpy as np
close = np.random.random(100)
sma = talib.SMA(close, timeperiod=30)
print(f"✅ TA-Lib is working. SMA sample: {sma[-1]:.4f}")