import pandas as pd
import plotly.express as px
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

COL_RENAMES = {
    "dataset": "Dataset",
    "encoding": "Encoding",
    "num_dimensions": "Num Dimensions",
    "num_slices": "Num Slices",
    "mean": "Mean Accuracy",
    "std": "Standard Deviation",
}

TIME_RENAMES = {
    **COL_RENAMES,
    "mean": "Mean Delta Time (s)",
    "std": "Standard Deviation",
}

def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    data = pd.read_csv(file_path, dtype={"num_dimensions": str, "num_slices": str})
    data.loc[data["model"] == "DWN", "accuracy"] *= 100
    return data

def group_stats(data, model, metric="accuracy"):
    df = data[data["model"] == model]
    grouped = df.groupby(["dataset", "encoding", "num_dimensions", "num_slices"])
    stats = grouped[metric].agg(["mean", "std"]).reset_index()
    return stats

def best_per_dataset(stats):
    idx = stats.groupby("dataset")["mean"].idxmax()
    return stats.loc[idx].reset_index(drop=True)

def make_config_col(df):
    return df["encoding"].astype(str) + " | D:" + df["num_dimensions"] + " | S:" + df["num_slices"]

def compare_models_accuracy_graph(data, output_dir):
    """
    Creates a grouped bar chart comparing accuracy of DWN and Wisard models
    for each dataset + encoding + num_dimensions + num_slices configuration.
    """
    import plotly.express as px
    import os

    os.makedirs(output_dir, exist_ok=True)

    # Create a config label for clarity on x-axis
    data = data.copy()
    data["config"] = (
        data["dataset"].astype(str)
        + " | "
        + data["encoding"].astype(str)
        + " | D:" + data["num_dimensions"].astype(str)
        + " | S:" + data["num_slices"].astype(str)
    )

    fig = px.bar(
        data,
        x="config",
        y="accuracy",
        color="model",
        barmode="group",
        title="Accuracy Comparison: DWN vs Wisard",
        labels={
            "config": "Dataset | Encoding | Num Dimensions | Num Slices",
            "accuracy": "Accuracy",
            "model": "Model",
        },
        error_y=data["std"] if "std" in data.columns else None,
    )

    fig.update_layout(xaxis_tickangle=-45, height=600)
    output_file = os.path.join(output_dir, "accuracy_comparison_dwn_wisard.html")
    fig.write_html(output_file)
    print(f"Saved accuracy comparison graph to: {output_file}")

def plot_bar(data, model, y, y_label, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    data = data.copy()
    data["config"] = make_config_col(data)
    logging.info(f"Creating {y_label} bar chart for {model}")
    fig = px.bar(
        data,
        x="config",
        y="mean",
        color="dataset",
        error_y="std",
        barmode="group",
        title=f"{model}: {y_label} by Encoding + Config per Dataset",
        labels={"config": "Encoding | Num Dimensions | Num Slices", "mean": y_label},
    )
    fig.update_layout(xaxis_tickangle=-45, height=600)
    filename = f"{model.lower()}_encoding_config_{y}.html"
    fig.write_html(os.path.join(output_dir, filename))

def write_md_table(f, df, rename_map, title):
    f.write(f"## {title}\n\n")
    f.write(df.rename(columns=rename_map).to_markdown(index=False))
    f.write("\n\n")

def write_conclusions(dwn_acc, wisard_acc, dwn_time, wisard_time,
                      dwn_best_enc, wisard_best_enc, dwn_scatter, wisard_scatter,
                      output_file):

    with open(output_file, "w") as f:
        write_md_table(f, dwn_acc, COL_RENAMES, "DWN Accuracy per Encoding + Dataset + Num Dimensions + Num Slices")
        write_md_table(f, wisard_acc, COL_RENAMES, "Wisard Accuracy per Encoding + Dataset + Num Dimensions + Num Slices")
        
        write_md_table(f, dwn_time.round(3), TIME_RENAMES, "DWN Delta Time per Encoding + Config")
        write_md_table(f, wisard_time.round(3), TIME_RENAMES, "Wisard Delta Time per Encoding + Config")
        
        write_md_table(f, dwn_best_enc, COL_RENAMES, "DWN Best Encoding for Each Dataset")
        write_md_table(f, wisard_best_enc, COL_RENAMES, "Wisard Best Encoding for Each Dataset")

        write_md_table(f, dwn_scatter.rename(columns={**COL_RENAMES, "mean": "Mean Accuracy", "std": "Standard Deviation"}), {}, "DWN Best Scatter Code Configurations per Dataset")
        write_md_table(f, wisard_scatter.rename(columns={**COL_RENAMES, "mean": "Mean Accuracy", "std": "Standard Deviation"}), {}, "Wisard Best Scatter Code Configurations per Dataset")

def optimal_scatter(data, model):
    df = data[(data["model"] == model) & (data["encoding"] == "Scatter Code")]
    stats = df.groupby(["dataset", "num_dimensions", "num_slices"])["accuracy"].agg(["mean", "std"]).reset_index()
    return best_per_dataset(stats)

def main():
    file_path = "metrics.csv"
    data = load_data(file_path)

    dwn_acc = group_stats(data, "DWN")
    wisard_acc = group_stats(data, "Wisard")

    plot_bar(dwn_acc, "DWN", "accuracy", "Mean Accuracy", "output/graphs")
    plot_bar(wisard_acc, "Wisard", "accuracy", "Mean Accuracy", "output/graphs")

    dwn_time = group_stats(data, "DWN", metric="delta_time")
    wisard_time = group_stats(data, "Wisard", metric="delta_time")

    plot_bar(dwn_time, "DWN", "delta_time", "Mean Delta Time (s)", "output/graphs")
    plot_bar(wisard_time, "Wisard", "delta_time", "Mean Delta Time (s)", "output/graphs")

    dwn_best_enc = best_per_dataset(dwn_acc)
    wisard_best_enc = best_per_dataset(wisard_acc)

    dwn_best_scatter = optimal_scatter(data, "DWN")
    wisard_best_scatter = optimal_scatter(data, "Wisard")
    
    grouped = (
        data.groupby(["model", "dataset", "encoding", "num_dimensions", "num_slices"])
        .accuracy.agg(["mean", "std"])
        .reset_index()
        .rename(columns={"mean": "accuracy"})
    )

    compare_models_accuracy_graph(grouped, "output/graphs")

    write_conclusions(
        dwn_acc, wisard_acc, dwn_time, wisard_time,
        dwn_best_enc, wisard_best_enc, dwn_best_scatter, wisard_best_scatter,
        "output/conclusions.md",
    )

if __name__ == "__main__":
    main()
