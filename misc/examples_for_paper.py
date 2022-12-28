#!/usr/bin/env python3
 
import epitran
import panphon2
import torch
import sys
sys.path.append(".")
from metric_learning.rnn_metric_learning_model import RNNMetricLearner

# process data
f = panphon2.FeatureTable()
epi = epitran.Epitran("eng-Latn")

model = RNNMetricLearner(target_metric="l2")
model.load_state_dict(torch.load("models/model_pl.pt"))

for word in ["write", "cite"]:
    print(word)
    word = epi.transliterate(word)
    print(word)
    word = f.word_to_binary_vectors(word)
    print(word)
    word = model.forward([word]).detach().cpu().numpy()
    print(word)
    print()
