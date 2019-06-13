import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def stacked_bar(samples,
                series_lst,
                series_labels,
                colors,
                xlabel,
                ylabel):

    sns.set_style('darkgrid',{"axes.facecolor": ".93"})

    barWidth = 0.85

    r = range(len(samples))

    fig = plt.figure(figsize=(7, 4),dpi=300)
    ax = fig.add_subplot(1, 1, 1)

    for i in range(len(series_lst)):
        if i == 0:
            bottom = None
        elif i == 1:
            bottom = pd.Series(series_lst[0])
        else:
            bottom = pd.Series(series_lst[0])
            for s in series_lst[1:i]:
                bottom = bottom.add(pd.Series(s))

        ax.bar(
            x=r,
            height=series_lst[i],
            bottom=bottom,
            color=colors[i],
            edgecolor="white",
            width=barWidth,
            label=series_labels[i]
            )

    plt.xticks(r,
            samples,
            rotation=45,
            fontsize=10,
            ha='right'
            )

    plt.xlabel(xlabel,
                fontweight="bold",
                fontsize=12
                )
    plt.ylabel(ylabel,
                fontweight="bold",
                fontsize=12
                )

    handles, labels = ax.get_legend_handles_labels()

    ax.legend(
        handles=handles[::-1],
        labels=labels[::-1],
        loc="upper left",
        bbox_to_anchor=(1, 0.7),
        ncol=1,
    )
    return fig
