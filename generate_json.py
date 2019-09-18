import argparse
import pandas as pd
import re
import json
import zipfile
from os.path import basename

def clean(dataset):
    drop = list()
    for i, row in dataset.iterrows():
        if not isinstance(row["text"], str) or len(row["text"].split()) < 3:
            drop.append(i)
        else:
            text = row["text"]
            clean_text = re.sub(r"\"", '"', text)
            dataset.at[i, "text"] = clean_text
    dataset = dataset.drop(drop)
    return dataset

def make_json(dataset, name):
    with open(name + ".json", "w") as fi:
        for i, row in dataset.iterrows():
            entity = {
                "tid": row["Unnamed: 0"],
                "timestamp": 1542244186,
                "text": row["text"],
                "full_text": row["text"],
                "retweet": False,
                "entities": []
            }
            json.dump(entity, fi)
            fi.write("\n")
    zip_file = zipfile.ZipFile(name +  ".zip", "w")
    zip_file.write(name +  ".json", basename(name) + ".json")
    zip_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", help="One of the four sample groups, can be "
                                         "CALM, Breast_Cancer, DSE, Aging")

    args = parser.parse_args()
    name = "Data/" + args.sample + "/" + args.sample
    try:
        df = pd.read_csv(name + ".csv")
    except:
        print("Wrong sample set selected, please use --sample with correct dataset")
        exit(1)
    df = clean(df)
    df.to_csv(name +  "_cleaned.csv", index=False)
    make_json(df, name)
