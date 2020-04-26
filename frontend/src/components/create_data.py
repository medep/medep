import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# compute sentiments
SBI_TOP = "../../../case_studies/case4/sbitop.csv"
df = pd.read_csv(SBI_TOP)
dates = df["Date"].values
sbi = df["Close"].values
sentiment = sbi - np.mean(sbi)
d_min, d_max = min(sentiment), max(sentiment)
sentiment = (sentiment - d_min) / (d_max - d_min) - 0.5
# make smoother
sentiment2 = [0.0 for _ in range(len(sentiment))]
for i in range(len(sentiment)):
    if i == 0:
        start, end = 0, 3
    elif i == len(sentiment) - 1:
        start, end = i - 2, i + 1
    else:
        start, end = i - 1, i + 2
    sentiment2[i] = float(np.mean(sentiment[start: end]))
sentiment = sentiment2
red = "red"
green = "green"
background_colors = [green if s >= 0 else red for s in sentiment]
# print(sentiment)
# plt.plot(sentiment)
# plt.plot(sbi / max(sbi))
# plt.show()
sentiment_data = [f"{{x: moment('{d}').toDate(), y: {s:.3f}}}" for d, s in zip(dates, sentiment)]
sentiment_data_str = f"""{{
    label: 'Economic Sentiment',
    fill: false,
    backgroundColor: {background_colors},
    borderWidth: 0,
    type: 'bar',
    yAxisID: 'B',
    data: [
        {', '.join(sentiment_data)},
    ],
}}"""
print(sentiment_data_str)

# INFECTED DATA
# taken from https://htmlcolorcodes.com/
colors = {"F0": "#2ecc71", "F1": "#85c1e9", "F2": "#d2b4de", "F3": "#9b59b6", "F4": "#e74c3c", "F5": "#f5b041"}
df = pd.read_csv("../../../case_studies/case4/covid-slo.csv")
dates = df["Date"].values
phases = df["phase"].values
infected = df["current-infected"].values

background_colors = [f'{colors[phase]}' for phase in phases]
infected_curve = [f"{{x: moment('{d}').toDate(), y: {i}}}" for d, i in zip(dates, infected)]

infected_curve_str = f"""{{
label: 'Currently Infected',
backgroundColor: {background_colors},
borderColor: '#00ff00',
fill: false,
data: [
    {', '.join(infected_curve)},
],
}}"""

print(infected_curve_str)
