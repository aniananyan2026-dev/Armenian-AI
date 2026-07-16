# Data Directory

Directory for Armenian text datasets.

## Structure

```
data/
├── raw/          # Raw text files
├── processed/    # Processed data for training
└── README.md
```

## Supported Formats

- **Text (.txt)** - One document per line
- **JSON Lines (.jsonl)** - `{"text": "..."}`
- **CSV (.csv)** - With "text" column

## Data Preparation

Run the preparation script:

```bash
python scripts/prepare_data.py --input data/raw/corpus.txt --output data/processed/
```

This creates:
- `train.txt` - Training data
- `val.txt` - Validation data
- `test.txt` - Test data
- `vocab.json` - Vocabulary
- `stats.json` - Statistics
