import json
import argparse
import numpy as np
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--input_file_name", nargs=1, help="Path to input file of counts")
    parser.add_argument("-n", "--num_wrds", nargs=1, help="how many tfidf words for each category")
    parser.add_argument("-o", "--output_file_name", nargs=1, help="Name of output file of tfidf")

    args = parser.parse_args()
    input_json = args.input_file_name[0]
    num_words = int(args.num_wrds[0])

    with open(input_json) as json_data:
        input_json = json.load(json_data)

    category_array = ["slice of life", "achievement", "fan", "music", "gossip", "tour", "controversy"]
    category_dict = {}

    for category in category_array:
        category_words = input_json[category]
        tfidf_arr = []
        words = []
        for word in category_words:
            tfidf_arr.append(tf_idf(word, category, input_json))
            words.append(word)
        category_dict[category] = [x for _, x in sorted(zip(tfidf_arr, words), reverse=True)]

    for category in category_array:
        category_dict[category] = category_dict[category][0:num_words]

    output_dir = 'data/tfidf_score'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path = os.path.join(output_dir, args.output_file_name[0])

    with open(output_file_path, "w+") as file:
        json.dump(category_dict, file, indent=4)


def tf(w, category, script):
    return script[category][w]


def idf(w, script):
    return np.log(len(script) / len([i for i in script if w in script[i]]))


def tf_idf(w, category, script):
    return tf(w, category, script) * idf(w, script)


if __name__ == "__main__":
    main()
