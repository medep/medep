import plotly as py
import plotly.graph_objects as go

MEASURES = ["bla", "kla"]


def create_plot(data, measures):
    fig = go.Figure()

    for column in data.columns.to_list():
        fig.add_trace(
            go.Scatter(
                x=data.index + 1,
                y=data[column],
                name=column
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

# import subprocess
# subprocess.call(r'java -cp moa.jar moa.DoTask moa.tasks.EvaluatePrequentialMultiLabel -l (rules.multilabel.AMRulesMultiLabelClassifier -g 5 -L (rules.multilabel.functions.MultiLabelNaiveBayes -l NaiveBayes) -A (OddsRatioScore -p CantellisInequality) -S MultiTargetVarianceRatio -e RelativeMeanAbsoluteDeviationMT -w UniformWeightedVoteMultiLabel -O SelectAllOutputs -I SelectAllInputs -F NoFeatureRanking) -s (MultiTargetArffFileStream -f data/hospitals.arff -c 53-58) -f 100 -d dump.txt')#,
# stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
