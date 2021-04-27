# Data 

Here is a breakdown of the files/data in this folder:
1. pan_bot_id: this is the raw PAN19 dataset. This dataset is maintained privately thus is not shown in this public repository. The data is available upon request. The data is formatted into individual XML files containing tweets for each account. The classification of each tweet as a bot or a human was provided in a separate XML file which has a file id. The data contains both English and Spanish tweets separated into different folders and we decided to just use English tweets. Though, these tweets may not be from this year, these accounts have been verified to be bots or humans.
2. all_data (not shown because this is a public repository and data is private): contains the data processed from the raw pan_bot_id dataset classified intro training, dev, earlybird, and test sets. 
3. load_data.py: this module was used to create the training, earlybird, and test sets from the pan_bot_id data. It turns these into pandas dataframes which are then used in the make_all_data script.
4. make_all_data.py: this script implements load_data.py and divides the training set into training and development sets. It also separates the tweets, X,  from their classifications, Y, into separate csv files. It also converts the classifications from "bot" or "human" to a binary variable, 1 or 0. We did this because it was too intensive to load the data in every notebook we used.

