# BERT Models Explained 
1. BERTBase_Increase_DropoutRate: base model with dropout rate increased to 0.4
2. BERTBase_one_epoch: base model run on one epoch instead of our standard 3
3. BERT_replace_hashtags: hashtags replaced with '#hashtag' token. Model is trained on 1 epoch instead of the standard 3 epochs. 
4. BERTnoRTS: retweets removed and model trained on 1 epoch.
5. BERTnoatsandBERTnoall: contains two models. One model has @s removed and one has @s, links, and hashtags removed. Both were run on 3 epochs.
6. BERTnohashtags: hashtags removed. Models is trained on 3 epochs.
7. BERTnolinksandBERTnoatsorhashtags: contains two models. One has links removed and one has @s and hashtags removed. Both were run on 3 epochs. 
8. BERTreplacelinks: links replaced with "URL". Model is trained on 1 epoch.