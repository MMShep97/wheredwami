from whereami.get_data import sample
from whereami.learn import write_data

sequence1_label_file = "sequence1_label.txt"
sequence1_data_file = "sequence1_data.txt"
sequence2_label_file = "sequence2_label.txt"
sequence2_data_file = "sequence2_data.txt"
sequence1 = ['sy', 'sy_door', 'rail', 'daniel_door', 'daniel']
sequence2 = ['daniel', 'daniel_door', 'rail', 'sy_door', 'sy']
n = 100

for i in range(n):
    for location in sequence2:
        str = "press enter to collect data at " + location
        a = input(str)
        try:
            new_sample = sample()
            if new_sample:
                write_data(sequence2_data_file, new_sample)
                write_data(sequence2_label_file, location)
        except KeyboardInterrupt:  # pragma: no cover
            break
