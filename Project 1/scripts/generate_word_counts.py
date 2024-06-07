import pandas as pd
import os
import json
import argparse
import string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out_file_name", nargs=1, help="The name of the output json")
    parser.add_argument("-d", "--input_file_name", nargs=1, help="The name of the input data")

    args = parser.parse_args()
    output_file = args.out_file_name[0]
    input_file = args.input_file_name[0]
    with open(input_file) as json_data:
        input_json = json.load(json_data)
    df = pd.DataFrame.from_dict(input_json)
    df = df.dropna()
    # All lower case on purpose just in case one of us misspells
    category_array = ["slice of life", "achievement", "fan", "music", "gossip", "tour", "controversy"]
    with open('src/custom_stop.txt', encoding="utf-8") as f:
        stop = f.read().splitlines()
    df['dialog'] = df['title'] + " " + df['description']
    df['dialog'] = df['dialog'].str.lower()
    df['category'] = df['category'].str.lower()
    df['dialog'] = df['dialog'].apply(lambda x: ' '.join([word.lower() for word in x.split() if word not in (stop)]))
    df['dialog'] = df['dialog'].apply(lambda s: s.translate(str.maketrans('', '', string.punctuation)))
    category_word_count = {}

    for category in category_array:
        cat_df = df[df['category'] == category]
        cat_df = pd.Series(' '.join(cat_df['dialog']).split()).value_counts()
        cat_df = cat_df.to_frame()
        cat_df = cat_df[cat_df['count'] >= 3]
        category_word_count[category] = cat_df.to_dict()['count']

    output_dir = os.path.join('data', 'word_count')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, output_file)

    with open(output_path, "w+") as file:
        json.dump(category_word_count, file, indent=4)


if __name__ == "__main__":
    main()
