!cd yolov5 && python train.py --img 320 --batch 20 --epochs 100 --data new_dataset.yaml --weights yolov5s.pt --workers 2 --name train_without_test
df = pd.read_csv('yolov5/runs/train/train_without_test/results.csv', sep=',')  # Use '\t' as the delimiter
#cls_loss measures the accuracy of class predictions.
df.columns = df.columns.str.strip()
# Create the loss graph
epochs= df['epoch']
losses= df['train/obj_loss']
plt.plot(epochs, losses, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss per Epoch')
plt.grid(True)
plt.show()