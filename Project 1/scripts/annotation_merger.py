import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('data_folders', type=str, nargs="+",
                        help='List of path to folder containing json files to merge')
    parser.add_argument('-o', '--output_file', type=str, help='Path to output json that is being merged to')

    args = parser.parse_args()

    merged_data = []
    for folder in args.data_folders:
        # For every file in the folder that ends with .json, load the data and append it to the merged data list
        for file in [f for f in os.listdir(folder) if f.endswith('.json')]:
            # Open the file and load the data
            with open(os.path.join(folder, file), 'r') as f:
                data = json.load(f)
                # Append the data to the merged data list
                merged_data.extend(data)

    # Save the merged data to the output file
    with open(args.output_file, 'w') as file:
        json.dump(merged_data, file, indent=4)

    print(f'Merged {len(merged_data)} items')


if __name__ == "__main__":
    main()
