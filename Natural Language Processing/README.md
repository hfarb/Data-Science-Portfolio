# W266-Twitter-Bot-Classification Project 
**Created By:**
Haley Farber, Daniel Lampert, Michael Yazdani

## Abstract: 
Internet bot detection is an important challenge Twitter faces, and currently there is no policy banning Twitter bots. Using machine learning models and deep learning, Twitter should be able to flag bots on a tweet level. This project explores the use of BERT and DistilBERT models to classify if tweets were written by a bot or human. We also explore the use of LIME to identify which words infer a tweet came from an internet bot. This project’s results show great promise in the use of deep learning models to detect internet bots as well as recommendations on ways to adjust these models to detect tweets written by bots with higher accuracy.

## File Breakdown of Our Repo:
1. Data: contains all of the data for our project 
2. Models: contains the models, LIME, and error analysis for our project. It is broken down into three folders:
	1. Transformers: these are our transformer models. We used BERT and DistilBERT. Each has their own folder.
	2. Baseline: these are our models we used for our baseline accuracy. We ran a CNN and an SVM. 
	3. Error Analysis/LIME: this contains LIME and our error analysis for the project. 

3. Our final report as a pdf. 
