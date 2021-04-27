import pandas as pd
import load_data
from importlib import reload
from sklearn.model_selection import train_test_split

def make_all_data(path_to_train, path_to_early_bird, path_to_test):
    "Returns CSVs of all data"
    def convert_binary_str_text(column):
        if column == "bot":
            return 1
        else:
            return 0
    reload(load_data)
    # reads in training data
    train_data = load_data.read_all_data(path_to_train) 
    #reads in earlybird data
    early_bird_data = load_data.read_all_data(path_to_early_bird)
    #reads in test data
    test_data = load_data.read_all_data(path_to_test)
    #converts bot column to binary
    train_data['bot'] = train_data['bot'].apply(convert_binary_str_text)
    early_bird_data['bot'] = early_bird_data['bot'].apply(convert_binary_str_text)
    test_data['bot'] = test_data['bot'].apply(convert_binary_str_text)
    y_train_base = train_data['bot']
    X_train_base = train_data['tweets']
    y_early_bird_base = early_bird_data['bot']
    X_earlybird_base = early_bird_data['tweets']
    y_test_base = test_data['bot']
    X_test_base = test_data['tweets']
    #splits into training and dev set
    X_train_base, X_dev_base, y_train_base, y_dev_base = train_test_split(X_train_base, y_train_base, test_size = 0.33, random_state = 37)
    X_train_base.to_csv('X_train.csv')
    X_dev_base.to_csv('X_dev.csv')
    y_train_base.to_csv('y_train.csv')
    y_dev_base.to_csv('y_dev.csv')
    X_earlybird_base.to_csv('X_earlybird.csv')
    y_early_bird_base.to_csv('y_earlybird.csv')
    y_test_base.to_csv('y_test.csv')
    X_test_base.to_csv('X_test.csv')

#replace with own folder
path_to_train = '/Users/daniellampert/Desktop/w266/bot_id_pan/bot_id_pan/pan_bot_id/pan19-author-profiling-training-2019-02-18/en/'
path_to_early_bird = '/Users/daniellampert/Desktop/w266/bot_id_pan/bot_id_pan/pan_bot_id/pan19-author-profiling-earlybirds-20190320/en/'
path_to_test = '/Users/daniellampert/Desktop/w266/bot_id_pan/bot_id_pan/pan_bot_id/pan19-author-profiling-test-2019-04-29/en/'
make_all_data(path_to_train, path_to_early_bird,path_to_test)