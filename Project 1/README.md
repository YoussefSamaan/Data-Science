# COMP370_FinalProject

## Getting Taylor Swift Data from GNews and NewsAPI
- Install the gnews package : ```pip3 install gnews```
- Generate the Taylor Swift data : Run the ```data_unifier.py``` file

## Split Data CLI Tool
**How to use**: python ./scripts/split_data.py --help

### Scripts Used To Generate Splits
- python ./scripts/split_data.py ./data/unified_swift_data.json ./data --splits 200,300 --names swift_data_coding_split,swift_data_annotation_split
- python ./scripts/split_data.py ./data/swift_data_coding_split.json ./data/coding --splits 50,50,50,50
- python ./scripts/split_data.py ./data/swift_data_annotation_split.json ./data/annotation --splits 75,75,75,75

## Annotation Helper CLI Tool
**How to use**: python ./scripts/annotation_helper.py --help