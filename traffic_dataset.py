from scapy.all import rdpcap, hexdump
import json
import pickle
import tensorflow as tf
import numpy as np

def load_data(traffic, logfile, items):
    """
    
    """
    # --- PCAP file contents ---

    capture_reader = rdpcap(traffic, items)
    dumps = []
    for item in capture_reader:
        processed_traffic = str(item)

        # NOTE: Try this later, to determine if hex representation works better
        # processed_traffic = str(hexdump(item, dump=True))

        dumps.append(processed_traffic)

    # print(dumps[0])

    # --- Parse Suricata JSON log ---

    logfile_reader = open(logfile, 'r')
    flagged_indices = []
    for line in logfile_reader:
        line_json = json.loads(line)
        try:
            pkt_index = line_json['pcap_cnt']
            flagged_indices.append(pkt_index)
        except KeyError:
            pass

    labels = []
    for index in range(len(dumps)):
        labels.append(index+1 in flagged_indices)

    return dumps, labels

def create_traffic_dataset(dumps, labels, batch_size=1):
    """
    Create a `tf.Dataset` containing target internet traffic and labels.\n
    `dumps`: List of pcap payloads (`str`)\n
    `labels`: List of packet labels (`bool`)
    """

    # dump_arr = np.array(dumps)
    # flag_arr = np.array(labels)

    dump_ds = tf.data.Dataset.from_tensor_slices(np.array(dumps))
    label_ds = tf.data.Dataset.from_tensor_slices(np.array(labels))

    # spit out a zipped dataset containing the baove two,
    # should return each item as a (<packet>, <label>) tuple
    return tf.data.Dataset.zip((dump_ds, label_ds))