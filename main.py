import tensorflow as tf
from tensorflow import keras
import tensorboard as tb
import numpy as np
import pickle
import traffic_dataset

# Hyper-parameters
BATCH_SIZE=40
NUM_EPOCHS=10

# Train/test data location
traffic="data/train.pcap"
logfile="data/train_labels.json"

print(
    "               __                      __ \n"
    " .-----.-----.|  |_ ______.----.-----.|__|\n"
    " |     |  -__||   _|______|  __|__ --||  |\n"
    " |__|__|_____||____|      |____|_____||__|\n"
)

# === Attempt to load data ===

print("Attempt to load train dataset...", sep=" ")
try:
    with open("train_dataset.pkl", 'rb') as pkl:
        train_dataset = pickle.load(pkl)
    print("Done.")

except FileNotFoundError:
    print("Failed!\nCreating new dataset...", sep=" ")

    train_dumps, train_labels = traffic_dataset.load_data(traffic, logfile, 1000)
    traffic_dataset.create_traffic_dataset(train_dumps, train_labels, batch_size=BATCH_SIZE)

    print("Done.")

# print(train_dumps)