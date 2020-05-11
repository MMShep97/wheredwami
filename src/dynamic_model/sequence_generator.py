import json
import os
from random import randint

def write_data(path, data):
    if path.endswith('_data.txt'):
        data = json.dumps(data)
    with open(path, "a") as f:
        f.write(data)
        f.write("\n")

def get_location_data(path):
    all_data = dict()
    all_labels = dict()
    for fname in os.listdir(path):
        if fname.endswith(".txt"):
            print(fname)
            data = []
            with open(os.path.join(path, fname)) as f:
                for line in f:
                    data.append(json.loads(line))
            all_data[fname.replace(".txt", "")] = data
            all_labels[fname.replace(".txt", "")] = [fname.rstrip(".txt")] * len(data)
    return all_data, all_labels

def generate_sequence(initial_location):
    sequence = []
    labels = []
    current_location = initial_location
    for i in range(10):
        labels.append(current_location)
        sequence.append(all_data[current_location].pop(0))
        idx = randint(0, len(adj_dict[current_location]) - 1)
        prev_location = current_location
        current_location = adj_dict[current_location][idx]
        if current_location == prev_location:
            return [], []
    return sequence, labels


src_path = 'C:\\Users\\Daniel\\.whereami\\rnn_exp_2\\src_locations'
label_file_path = 'C:\\Users\\Daniel\\.whereami\\rnn_exp_2\\sequences\\sequence_labels.txt'
data_file_path = 'C:\\Users\\Daniel\\.whereami\\rnn_exp_2\\sequences\\sequence_data.txt'

all_data, all_labels = get_location_data(src_path)
adj_dict = {'sy':['door_sy'], 'daniel':['door_daniel'], 'door_sy':['sy', 'rail'], 'door_daniel':['daniel','rail'], 'rail':['door_sy', 'door_daniel']}

sequences = []
labels = []
for datapoint in all_data['rail']:
    sequence, label = generate_sequence('rail')
    sequences.extend(sequence)
    labels.extend(label)

for i in range(len(labels)):
    write_data(label_file_path, labels[i])
    write_data(data_file_path, sequences[i])
