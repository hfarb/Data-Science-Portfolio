# Machine Learning Portfolio 

## Project 1
I implement my own image recognition system for classifying digits using KNN and Naive Bayes on MNIST data. 

## Project 2 
I worked with text data from newsgroup posts on a variety of topics. I trained classifiers to distinguish posts by topics inferred from the text. 

## Project 3
In this project, I investigated properties of mushrooms. The dataset contains over 8000 examples, where each describes a mushroom by a variety of features like color, odor, etc., and the target variable is an indicator for whether the mushroom is poisonous. The feature space has been binarized. Look at the feature_names to see all 126 binary names.

I started by running PCA to reduce the dimensionality from 126 down to 2 so that I could easily visualize the data. 

Once I projected the data to 2 dimensions, I experimented with clustering using k-means and density estimation with Gaussian mixture models (GMM). Finally, I trained a classifier by fitting a GMM for the positive class and a GMM for the negative class, and performed inference by comparing the probabilities output by each model.

## Final Project 
This is the final project for W207, the introduction to machine learning class. The project is about predicting the popularity of online news articles. For our project, we scraped about 7,000 articles from Forbes from January 2020 to November 2020 and extracted article attributes such as an article's URL link, title, text, topic, time published, and number of views. We then created 65 features from these attributes. Most of these features were built and named after the features used by Kelwin Fernandes, Pedro Vinagre, and Paulo Cortez from their dataset that was used to measure the popularity of Mashable articles from 2013-2015. Instead of using shares to predict an article's popularity as was done by those who used the Mashable data set, we used views to predict an article's popularity and used linear regression to do so. 