import h5py
import os

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'emotion_model.h5')

try:
    with h5py.File(model_path, 'r') as f:
        print("Keys in the H5 file:", list(f.keys()))
except Exception as e:
    print(f"Error reading file: {e}")