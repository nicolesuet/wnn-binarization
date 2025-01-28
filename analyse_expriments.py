import pandas as pd
import plotly.express as px
from scipy.stats import f_oneway, ttest_ind, kruskal, mannwhitneyu
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import os


# Load the CSV file
def load_data(file_path):
    return pd.read_csv(file_path)


# Calculate accuracy metrics for DWN and Wisard
def calculate_accuracy(data, model_name):
    grouped = data[data["model"] == model_name].groupby(["encoding", "dataset"])
    return grouped["accuracy"].agg(["mean", "std"]).reset_index()


# Find optimal scatter code configuration
def optimal_scatter_config(data, model_name):
    scatter_data = data[
        (data["model"] == model_name) & (data["encoding"] == "Scatter Code")
    ]
    grouped = scatter_data.groupby(["dataset", "num_dimensions", "num_slices"])
    return grouped["accuracy"].agg(["mean", "std"]).reset_index()


# Find best encoding per dataset
def best_encoding(data, model_name):
    model_data = data[data["model"] == model_name]
    grouped = model_data.groupby(["dataset", "encoding"])
    return (
        grouped["accuracy"]
        .agg(["mean", "std"])
        .reset_index()
        .sort_values(["dataset", "mean"], ascending=[True, False])
    )


# Compare delta_time per encoding
def compare_delta_time(data, model_name):
    model_data = data[data["model"] == model_name]
    grouped = model_data.groupby(["dataset", "encoding"])
    return grouped["delta_time"].agg(["mean", "std"]).reset_index()


# Generate interactive graphs for accuracy
def create_accuracy_graphs(dwn_data, wisard_data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Graph: Accuracy by Encoding and Dataset for DWN
    fig_dwn = px.bar(
        dwn_data,
        x="encoding",
        y="mean",
        color="dataset",
        error_y="std",
        barmode="group",
        title="DWN: Accuracy by Encoding and Dataset",
    )
    fig_dwn.write_html(os.path.join(output_dir, "dwn_accuracy.html"))

    # Graph: Accuracy by Encoding and Dataset for Wisard
    fig_wisard = px.bar(
        wisard_data,
        x="encoding",
        y="mean",
        color="dataset",
        error_y="std",
        barmode="group",
        title="Wisard: Accuracy by Encoding and Dataset",
    )
    fig_wisard.write_html(os.path.join(output_dir, "wisard_accuracy.html"))


# Generate interactive graph for delta time comparisons
def create_time_comparison_graph(dwn_delta_time, wisard_delta_time, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Combine DWN and Wisard delta time data for comparison
    dwn_delta_time["model"] = "DWN"
    wisard_delta_time["model"] = "Wisard"
    combined_delta_time = pd.concat([dwn_delta_time, wisard_delta_time])

    # Graph: Delta Time by Encoding and Dataset
    fig_time = px.bar(
        combined_delta_time,
        x="encoding",
        y="mean",
        color="dataset",
        error_y="std",
        barmode="group",
        facet_col="model",
        title="Delta Time by Encoding and Dataset",
    )
    fig_time.write_html(os.path.join(output_dir, "delta_time_comparison.html"))


# Generate interactive graph for scatter code configurations
def create_scatter_config_graph(dwn_scatter_config, wisard_scatter_config, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Combine DWN and Wisard scatter config data for comparison
    dwn_scatter_config["model"] = "DWN"
    wisard_scatter_config["model"] = "Wisard"
    combined_scatter_config = pd.concat([dwn_scatter_config, wisard_scatter_config])

    # Graph: Scatter Code Configurations (num_slices vs num_dimensions)
    fig_scatter = px.scatter(
        combined_scatter_config,
        x="num_slices",
        y="num_dimensions",
        color="dataset",
        size="mean",
        facet_col="model",
        title="Scatter Code Configurations: num_slices vs num_dimensions",
    )
    fig_scatter.write_html(os.path.join(output_dir, "scatter_code_config.html"))


# Write conclusions to Markdown file
def write_conclusions_to_md(
    dwn_best_encoding,
    wisard_best_encoding,
    dwn_scatter_config,
    wisard_scatter_config,
    dwn_delta_time,
    wisard_delta_time,
    output_file,
):
    with open(output_file, "w") as f:
        f.write("# Analysis Conclusions\n\n")

        # All encoding results per dataset and model
        f.write("## All Encoding Results per Dataset and Model\n\n")

        # DWN All Encoding Results
        f.write("### DWN: All Encoding Results\n\n")
        dwn_all_encodings = dwn_best_encoding[
            ["dataset", "encoding", "mean", "std"]
        ].rename(
            columns={
                "dataset": "Dataset",
                "encoding": "Encoding",
                "mean": "Mean Accuracy",
                "std": "Standard Deviation",
            }
        )
        f.write(dwn_all_encodings.to_markdown(index=False))
        f.write("\n\n")

        # Wisard All Encoding Results
        f.write("### Wisard: All Encoding Results\n\n")
        wisard_all_encodings = wisard_best_encoding[
            ["dataset", "encoding", "mean", "std"]
        ].rename(
            columns={
                "dataset": "Dataset",
                "encoding": "Encoding",
                "mean": "Mean Accuracy",
                "std": "Standard Deviation",
            }
        )
        f.write(wisard_all_encodings.to_markdown(index=False))
        f.write("\n\n")

        # Best encodings per dataset
        f.write("## Best Encodings per Dataset\n\n")

        # DWN Best Encodings
        f.write("### DWN: Best Encoding for Each Dataset\n\n")
        dwn_best_encoding_per_dataset = (
            dwn_best_encoding.groupby("dataset").first().reset_index()
        )
        f.write(
            dwn_best_encoding_per_dataset[["dataset", "encoding", "mean", "std"]]
            .rename(
                columns={
                    "dataset": "Dataset",
                    "encoding": "Best Encoding",
                    "mean": "Mean Accuracy",
                    "std": "Standard Deviation",
                }
            )
            .to_markdown(index=False)
        )
        f.write("\n\n")

        # Wisard Best Encodings
        f.write("### Wisard: Best Encoding for Each Dataset\n\n")
        wisard_best_encoding_per_dataset = (
            wisard_best_encoding.groupby("dataset").first().reset_index()
        )
        f.write(
            wisard_best_encoding_per_dataset[["dataset", "encoding", "mean", "std"]]
            .rename(
                columns={
                    "dataset": "Dataset",
                    "encoding": "Best Encoding",
                    "mean": "Mean Accuracy",
                    "std": "Standard Deviation",
                }
            )
            .to_markdown(index=False)
        )
        f.write("\n\n")

        # Optimal scatter code configurations
        f.write("## Optimal Scatter Code Configurations\n\n")
        f.write("### DWN\n\n")
        f.write(dwn_scatter_config.to_markdown(index=False))
        f.write("\n\n### Wisard\n\n")
        f.write(wisard_scatter_config.to_markdown(index=False))
        f.write("\n\n")

        # Delta time comparisons
        f.write("## Delta Time Comparisons\n\n")
        f.write("### DWN\n\n")
        f.write(dwn_delta_time.to_markdown(index=False))
        f.write("\n\n### Wisard\n\n")
        f.write(wisard_delta_time.to_markdown(index=False))
        f.write("\n")

        # Scatter Code Accuracy Tables
        f.write("## Scatter Code Accuracy by Dataset\n\n")

        # DWN Scatter Code Accuracy
        f.write(
            "### DWN: Mean Accuracy and Standard Deviation for Scatter Code Configurations\n\n"
        )
        dwn_scatter_table = dwn_scatter_config.copy()
        dwn_scatter_table["Mean Accuracy"] = dwn_scatter_table["mean"].round(
            3
        )  # Round to 3 decimal places
        dwn_scatter_table["Standard Deviation"] = dwn_scatter_table["std"].round(
            3
        )  # Round to 3 decimal places
        dwn_scatter_table = dwn_scatter_table.rename(
            columns={
                "dataset": "Dataset",
                "num_slices": "Num Slices",
                "num_dimensions": "Num Dimensions",
            }
        )
        f.write(
            dwn_scatter_table[
                [
                    "Dataset",
                    "Num Slices",
                    "Num Dimensions",
                    "Mean Accuracy",
                    "Standard Deviation",
                ]
            ].to_markdown(index=False)
        )
        f.write("\n\n")

        # Wisard Scatter Code Accuracy
        f.write(
            "### Wisard: Mean Accuracy and Standard Deviation for Scatter Code Configurations\n\n"
        )
        wisard_scatter_table = wisard_scatter_config.copy()
        wisard_scatter_table["Mean Accuracy"] = wisard_scatter_table["mean"].round(
            3
        )  # Round to 3 decimal places
        wisard_scatter_table["Standard Deviation"] = wisard_scatter_table["std"].round(
            3
        )  # Round to 3 decimal places
        wisard_scatter_table = wisard_scatter_table.rename(
            columns={
                "dataset": "Dataset",
                "num_slices": "Num Slices",
                "num_dimensions": "Num Dimensions",
            }
        )
        f.write(
            wisard_scatter_table[
                [
                    "Dataset",
                    "Num Slices",
                    "Num Dimensions",
                    "Mean Accuracy",
                    "Standard Deviation",
                ]
            ].to_markdown(index=False)
        )
        f.write("\n\n")


# Main function
def main():
    # Load data
    file_path = "merged_file.csv"  # Replace with your CSV file path
    data = load_data(file_path)

    # Metrics
    dwn_accuracy = calculate_accuracy(data, "DWN")
    wisard_accuracy = calculate_accuracy(data, "Wisard")

    dwn_scatter_config = optimal_scatter_config(data, "DWN")
    wisard_scatter_config = optimal_scatter_config(data, "Wisard")

    dwn_best_encoding = best_encoding(data, "DWN")
    wisard_best_encoding = best_encoding(data, "Wisard")

    dwn_delta_time = compare_delta_time(data, "DWN")
    wisard_delta_time = compare_delta_time(data, "Wisard")

    # Graphs and conclusions
    create_accuracy_graphs(dwn_accuracy, wisard_accuracy, "output/graphs")
    create_time_comparison_graph(dwn_delta_time, wisard_delta_time, "output/graphs")
    create_scatter_config_graph(
        dwn_scatter_config, wisard_scatter_config, "output/graphs"
    )

    # Write conclusions to Markdown
    write_conclusions_to_md(
        dwn_best_encoding,
        wisard_best_encoding,
        dwn_scatter_config,
        wisard_scatter_config,
        dwn_delta_time,
        wisard_delta_time,
        "output/conclusions.md",
    )


if __name__ == "__main__":
    main()
