import subprocess
import pandas as pd
from matplotlib import pyplot as plt

# Install requirements using subprocess
subprocess.run("cd yolov5 && pip install -r requirements.txt", shell=True)

# Rest of your code
df = pd.read_csv('yolov5/runs/train/train_without_test/results.csv', sep=',')
df.columns = df.columns.str.strip()

epochs = df['epoch']
losses = df['train/obj_loss']
plt.plot(epochs, losses, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss per Epoch')
plt.grid(True)
plt.show()

