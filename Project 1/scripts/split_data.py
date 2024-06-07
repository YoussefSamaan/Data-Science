import argparse
import json
import random


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', type=str,
                        help='Path to input json file that contains transformed data defined in src/data_unifier.py')
    parser.add_argument('output_dir', type=str, help='Path to output directory where the split data will be saved')
    parser.add_argument('--splits', type=str, required=True,
                        help='List of split counts to generate separated by commas (e.g. 50,50,50)')
    parser.add_argument('--names', type=str,
                        help='List of names for the split files separated by commas (e.g. file_name_for_split1,'
                             'file_name_for_split2,file_name_for_split3)')

    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        json_data = json.load(file)

        # Verify that args.splits is a valid list of integers
        str_splits = args.splits.split(',')
        splits = []
        split_sum = 0
        for split in str_splits:
            try:
                split_int = int(split)
                split_sum += split_int
                splits.append(split_int)
            except ValueError:
                print(f'Invalid split count: {split}')
                return

        if split_sum > len(json_data):
            print(f'Split count ({split_sum}) exceeds the total number of data items ({len(json_data)})')
            return

        # Sort the data from newest to oldest
        json_data.sort(key=lambda x: x['publishedAt'], reverse=True)

        # Truncate to split_sum
        json_data = json_data[:split_sum]

        # Shuffle the data
        random.shuffle(json_data)

        # Split the data based on args.splits
        split_data = []
        split_start = 0
        for split in splits:
            split_data.append(json_data[split_start:split_start + split])
            split_start += split

        filename = args.input_file.split('/')[-1].split('.')[0]

        output_filenames = [f'{filename}_split_{i}.json' for i in range(len(split_data))]
        if args.names:
            names = args.names.split(',')

            if len(names) != len(split_data):
                print(f'Number of names ({len(names)}) does not match number of splits ({len(split_data)})')
                return

            output_filenames = [f'{names[i]}.json' for i in range(len(split_data))]

        # Save split_data
        for i, split in enumerate(split_data):
            with open(f'{args.output_dir}/{output_filenames[i]}', 'w') as file:
                json.dump(split, file, indent=4)


if __name__ == '__main__':
    main()
