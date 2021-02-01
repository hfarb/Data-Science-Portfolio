# Machine Learning Portfolio 

## Project 1
I implement my own image recognition system for classifying digits using KNN and Naive Bayes on MNIST data. 

## Project 2 
I worked with text data from newsgroup posts on a variety of topics. I trained classifiers to distinguish posts by topics inferred from the text. 

## Project 3
In this project, I investigated properties of mushrooms. The dataset contains over 8000 examples, where each describes a mushroom by a variety of features like color, odor, etc., and the target variable is an indicator for whether the mushroom is poisonous. The feature space has been binarized. Look at the feature_names to see all 126 binary names.

I started by running PCA to reduce the dimensionality from 126 down to 2 so that I could easily visualize the data. 

Once I projected the data to 2 dimensions, I experimented with clustering using k-means and density estimation with Gaussian mixture models (GMM). Finally, I trained a classifier by fitting a GMM for the positive class and a GMM for the negative class, and performed inference by comparing the probabilities output by each model.