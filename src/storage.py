import pandas as pd

def save_metrics(metrics):

    df = pd.DataFrame([metrics])

    df.to_csv(
        "metrics.csv",
        mode="a",
        header=False,
        index=False
    )