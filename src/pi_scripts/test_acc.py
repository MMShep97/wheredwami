from whereami.predict import predict_test_data
from whereami.pipeline import train_model
import os
from tqdm import tqdm

def evaluate_test_acc(source_files):
    predictions = []
    labels = []
    for source_file in source_files:
        p, l = predict_test_data(source_file)
        predictions.extend(p)
        labels.extend(l)
    num_correct = 0.0
    for i in tqdm(range(len(predictions))):
        print(i, predictions[i], labels[i])
        if predictions[i] == labels[i]:
            num_correct = num_correct + 1
    return num_correct/len(predictions)

exp1_source_files = ['/home/pi/.whereami/test_data/test_circle_table_west.txt', '/home/pi/.whereami/test_data/test_square_table_east.txt', '/home/pi/.whereami/test_data/test_thermo_red_square.txt', '/home/pi/.whereami/test_data/test_table_1_north_outlet.txt']
exp4_source_files = ['/home/pi/.whereami/test_data/test_near_base.txt', '/home/pi/.whereami/test_data/test_near_two.txt', '/home/pi/.whereami/test_data/test_near_one.txt']
exp3_source_files = ['/home/pi/.whereami/test_data/test_m.txt', '/home/pi/.whereami/test_data/test_ms.txt', '/home/pi/.whereami/test_data/test_mss.txt']
path = '/home/pi/.whereami/test_data'
source_files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]    
train_model(model_type='nn')
print(evaluate_test_acc(source_files)) 
