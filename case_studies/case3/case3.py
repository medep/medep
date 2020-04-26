#!/usr/bin/env python
# coding: utf-8

# ## Sharing data among hospitals
# 
# 1. More data means better models.
# 2. Problem: possibly, data must not leave the hospital that acquired them
# 
# Thus, rather than the data, a model is passed among the hospitals. By doing so,
# 
# 1. The model is trained using all available data.
# 2. No hospital has to share the data.
# 
# Models that support this learinng setting:
# 
# 1. Data streaming models, e.g., AM Rules, iSOUP trees etc.
# 2. Models learned incrementaly, e.g. neural networks
# 
# ## TODO: references, describe the data

# In[13]:


import os
import subprocess
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import warnings

warnings.filterwarnings('ignore')

STREAM_MODEL = r'java -cp moa.jar moa.DoTask moa.tasks.EvaluatePrequentialMultiLabel '                r'-l (rules.multilabel.AMRulesMultiLabelClassifier -g 5 '                r'-L (rules.multilabel.functions.MultiLabelNaiveBayes -l NaiveBayes) '                r'-A (OddsRatioScore -p CantellisInequality) -S MultiTargetVarianceRatio '                r'-e RelativeMeanAbsoluteDeviationMT -w UniformWeightedVoteMultiLabel -O SelectAllOutputs '                r'-I SelectAllInputs -F NoFeatureRanking) '                r'-s (MultiTargetArffFileStream -f {} -c 53-58) -f 100 -d {}'
MEASURES = ["Exact Match", "Accuracy", "Hamming Score", "Precision", "Recall", "F-Measure"]
# do not show accuracy since it is basically the same as Hamming
MEASURES_FOR_PLOTTING = ["Exact Match", "Hamming Score", "Precision", "Recall", "F-Measure"]


# In[2]:


def evaluate(ys_true, ys_predicted):
    exact_match = np.mean([y1 == y2 for y1, y2 in zip(ys_true, ys_predicted)])
    accuracy = np.mean([np.mean([y1[i] == y2[i] for y1, y2 in zip(ys_true, ys_predicted)])
                        for i in range(len(ys_true[0]))])
    hamming = np.mean(np.array(ys_true) == np.array(ys_predicted))
    precisions = np.array([np.mean([y1[i] == y2[i] for y1, y2 in zip(ys_true, ys_predicted) if y2[i] == 1])
                           for i in range(len(ys_true[0]))])
    recalls = np.array([np.mean([y1[i] == y2[i] for y1, y2 in zip(ys_true, ys_predicted) if y1[i] == 1])
                        for i in range(len(ys_true[0]))])
    precisions[np.isnan(precisions)] = 1.0
    recalls[np.isnan(recalls)] = 1.0
    f1s = (2 * precisions * recalls) / (precisions + recalls)
    f1s[np.isnan(f1s)] = 1.0
    return [exact_match, accuracy, hamming, np.mean(precisions), np.mean(recalls), np.mean(f1s)]


class Network:
    def __init__(self, hidden_layer_sizes=None, device='cpu',
                 epochs=100, bs=100, lr=1e-3):

        self.device = device
        self.epochs = epochs
        self.bs = bs
        self.lr = lr

        self._num_features = None
        self._num_targets = None
        self.hidden_layer_sizes = [] if hidden_layer_sizes is None else hidden_layer_sizes

    def _build_model(self):
        layers = []
        layer_sizes = [self._num_features] + self.hidden_layer_sizes
        for i in range(len(layer_sizes) - 1):
            layers.append(nn.Linear(in_features=layer_sizes[i], out_features=layer_sizes[i + 1],
                                    bias=False))
            layers.append(nn.ReLU())
            layers.append(nn.BatchNorm1d(num_features=layer_sizes[i + 1]))
        layers.append(nn.Linear(in_features=layer_sizes[-1], out_features=self._num_targets))
        self.model = nn.Sequential(*layers).double().to(self.device)

    def fit(self, features, targets, **kwargs):
        self._num_features = features.shape[1]
        self._num_targets = targets.shape[1]
        self._build_model()
        self.model.train()

        tensor_xs = torch.from_numpy(features)
        tensor_y = torch.from_numpy(targets)
        train_dataset = TensorDataset(tensor_xs, tensor_y)

        # fitting parameters
        bs = kwargs.get("bs", self.bs)
        lr = kwargs.get("lr", self.lr)
        epochs = kwargs.get("epochs", self.epochs)
        train_data_loader = DataLoader(train_dataset, batch_size=bs, shuffle=False)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        loss = nn.MSELoss()
        predictions_all = []
        for xs_batch, y_batch in train_data_loader:
            predictions_all.append(self.predict(xs_batch))
            for _ in range(epochs):
                predictions = self.model(xs_batch.to(self.device))
                error = loss(predictions, y_batch.to(self.device))
                error.backward()
                optimizer.step()
                self.model.zero_grad()
        self.model.eval()
        return predictions_all

    def predict(self, features):
        test_set = torch.tensor(features).to(self.device)
        with torch.no_grad():
            predictions = self.model(test_set).cpu().numpy()
            predictions[predictions < 0] = 0
            predictions[predictions > 1] = 1
        # round predictions
        return np.rint(predictions).tolist()

    
def create_model(is_stream, data_file='data/hospitals.arff', n_hospitals=10, batch=100):
    if is_stream:
        assert n_hospitals == 10
        assert batch == 100
        # call moa
        results_file = 'dump.txt'
        command = STREAM_MODEL.format(data_file, results_file)
        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # load measures
        data_frame = pd.read_csv(results_file)
        values = {}
        for m in MEASURES:
            values[m] = data_frame[m].values
        os.remove(results_file)
    else:
        # load data
        data = np.loadtxt(data_file, skiprows=60, delimiter=',')
        is_target = np.zeros(data.shape[1], dtype=bool)
        is_target[list(range(52, 58))] = True
        xs = data[:, ~is_target]
        ys = data[:, is_target]
        values = {m: [] for m in MEASURES}
        # simulate different hospitals
        net = Network()
        predictions = net.fit(xs, ys)
        for h in range(n_hospitals):
            ys_h = ys[h * batch: (h + 1) * batch]
            ys_h_predicted = predictions[h]
            new_values = evaluate(ys_h, ys_h_predicted)
            for m, v in zip(MEASURES, new_values):
                values[m].append(v)
        values = {m: np.array(v) for m, v in values.items()}
    return values


# Build two models:
# 
# - AM Rules
# - Neural network

# In[14]:


am_rules_curves = create_model(True)
nn_curves = create_model(False)


# In[10]:


import plotly.graph_objects as go


def create_plot(data, measures):
    fig = go.Figure()
    xs = list(range(1, len(data[measures[0]]) + 1))
    for m in measures:
        fig.add_trace(
            go.Scatter(
                x=xs,
                y=data[m],
                name=m
            )
        )

    buttons = [dict(label='All',
                    method='update',
                    args=[{'visible': [True for _ in measures]},
                          {'title': 'All',
                           'showlegend': True}]
                    )
               ]
    for m in measures:
        button = dict(label=m,
                      method='update',
                      args=[{'visible': [other == m for other in measures]},
                            {'title': m,
                             'showlegend': True}])
        buttons.append(button)

    fig.update_layout(
        updatemenus=[go.layout.Updatemenu(active=0, buttons=buttons)],
        xaxis=dict(tickmode='linear', tick0=1, dtick=1),
        xaxis_title="number of hospitals",
        yaxis_title="",
        font=dict(size=18, color="#7f7f7f", family="Courier New, monospace")
    )
    fig.show()


# In[11]:


create_plot(nn_curves, MEASURES_FOR_PLOTTING)


# In[12]:


create_plot(am_rules_curves, MEASURES_FOR_PLOTTING)

