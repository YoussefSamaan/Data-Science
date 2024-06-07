'''
Same code that was created by daniel with some small modifications.
'''

import argparse
import json


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', type=str, help='Path to input json file to annotate')
    parser.add_argument('--start', type=int, default=0, help='Index of the first item to annotate')

    args = parser.parse_args()

    json_data = None
    Sentiment_list = ["Positive", "Negative", "Neutral"]
    with open(args.input_file, 'r') as file:
        json_data = json.load(file)

        for item in json_data:
            if args.start > 0:
                args.start -= 1
                continue

            print(f'-------------------Item {json_data.index(item) + 1} of {len(json_data)}-------------------')
            # Display the sentiments
            print(f'Sentiments: {Sentiment_list}\n')

            # Display the title and description of the news item
            print(f'Title: {item["title"]}')
            print(f'Description: {item["description"]}')

            # Prompt the user to enter a sentiment
            sentiment = input('Enter a sentiment or index (enter "exit" to stop annotating): ')
            if sentiment == 'exit':
                break

            if sentiment.isdigit():
                index = int(sentiment)
                if len(Sentiment_list) > index >= 0:
                    sentiment = Sentiment_list[index]

            # Add the category to the news item
            item['sentiment'] = sentiment

            print()

    if json_data is None:
        print('No data to annotate')
        return

    # Save the annotated data
    with open(args.input_file, 'w') as file:
        json.dump(json_data, file, indent=4)


if __name__ == '__main__':
    main()
