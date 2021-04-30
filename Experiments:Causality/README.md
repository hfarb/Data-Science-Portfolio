# A Purchase Intent Experiment For Plus-Size Marketing

## Summary of Experiment and Results 

We conducted an experiment to determine whether viewing plus-size models instead of size 0-4 models causes women to be more likely to purchase clothing. Our experiment contained two different versions of a survey each with various demographic and shopping behavior questions and 20 images of a particular size model, either size 0-4, or plus-size. We collected two groups of images: control and treatment. The images in the control group are pictures of clothing worn by size 0-4 models and images in the treatment group are pictures of the same clothing worn by plus-size models. We randomly assigned subjects to the treatment or control group and asked them how likely they were to purchase a certain item of clothing shown in each picture on a Likert Scale with values 1-5, where 1 is “Extremely Unlikely” and 5 is “Extremely Likely”. We then measured the difference in the average purchase intent for each set of pictures amongst those in the treatment group and those in the control group. We used Qualtrics to design our survey and deployed the survey on Mechanical Turk. 

Our experiment shows that there appears to be a negative effect of plus-size models on a woman’s purchase intent. All of our regressions showed that viewing plus-sized models decreased a woman’s intent to purchase clothing. However, the standard errors were incredibly large so the coefficients were mostly insignificant, suggesting that there could be no effect of viewing plus-size models instead of size 0-4 models on a woman’s intent to purchase clothing or there could actually be a positive effect.

We saw no evidence of heterogeneous treatment effects based on a woman’s body size or self-esteem. However, for self-esteem levels, we do see some differences in baseline purchase intent. Based on statistically significant evidence at the 0.01 cutoff, our results indicate that women with low or neutral self-esteem generally have lower purchase intent than women with high self-esteem. After separate regression analyses for self-esteem and body size, we wanted to determine whether these two covariates were associated with one another. To do so, we created a mosaic plot, and found there to be no statistically significant dependence between self-esteem and body-size.
In conclusion, most of our results were insignificant and we could not confirm a treatment effect. However, our sample size was small and thus our experiment lacked power meaning we were very unlikely to detect a treatment effect even if there were one. If we had a larger sample size,
and therefore more power, we could be more certain about our results and be more likely to detect a treatment effect if it exists. Calculations in the paper show how many survey respondents we'd need to have sufficient power to detect a treatment effect if one were to exist.

## About Repository
- See the data directory for the dataset that we created for this project. For the data that our analysis was produced from, see the file: submission_data.csv
-See the code directory for the R code used to clean and process data and create visualizations and regressions. 



