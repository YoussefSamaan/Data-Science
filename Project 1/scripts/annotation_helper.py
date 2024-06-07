import argparse
import json

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', type=str, help='Path to input json file to annotate')
    parser.add_argument('--start', type=int, default=0, help='Index of the first item to annotate')

    args = parser.parse_args()

    json_data = None
    current_categories = set()
    categories_list = []
    with open(args.input_file, 'r') as file:
        json_data = json.load(file)

        for item in json_data:
            if args.start > 0:
                args.start -= 1
                continue

            print(f'-------------------Item {json_data.index(item) + 1} of {len(json_data)}-------------------')
            # Display the current categories that have been annotated
            print(f'Current categories: {categories_list}\n')
            
            # Display the title and description of the news item
            print(f'Title: {item["title"]}')
            print(f'Description: {item["description"]}')

            # Prompt the user to enter a category
            category = input('Enter a category or index (enter "exit" to stop annotating): ')
            if category == 'exit':
                break

            if category.isdigit():
                index = int(category)
                if len(categories_list) > index >= 0:
                    category = categories_list[index]

            if not current_categories.__contains__(category):
                current_categories.add(category)
                categories_list.append(category)
            # Add the category to the set of current categories

            # Add the category to the news item
            item['category'] = category

            print()

    if json_data is None:
        print('No data to annotate')
        return
    
    # Save the annotated data
    with open(args.input_file, 'w') as file:
        json.dump(json_data, file, indent=4)

if __name__ == '__main__':
    main()