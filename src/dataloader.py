import os
import pandas as pd


def read_qa_dataframe(path):
    data = pd.read_csv(path, sep="|", header=None)
    data.columns = ["image_id", "question", "answer"]
    return data


def read_qa_by_category(path_to_category_files):
    files = os.listdir(path_to_category_files)
    dfs = []
    for file in files:
        if file.startswith("C") and file.endswith("_train.txt"):
            category = file.split("_")[1].lower()
            category_df = read_qa_dataframe(os.path.join(path_to_category_files, file))
            category_df["category"] = category
            dfs.append(category_df)
    return pd.concat(dfs)


if __name__ == "__main__":
    print("Starting to read data")
    df = read_qa_by_category("./data/ImageClef-2019-VQA-Med-Training/QAPairsByCategory")
    print("Printing tail of the dataset:")
    print(df.tail())
