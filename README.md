# 🇦🇲 Armenian-AI

Building a modern Large Language Model (LLM) for the Armenian language from scratch using contemporary transformer-based architectures and Python.

## 🎯 Project Goals

- 🏗️ **Build an LLM from scratch** for Armenian language
- 🔬 **Experiment** with state-of-the-art architectures
- 📊 **Scale training** with modern distributed techniques
- 🚀 **Production-ready** model for natural language tasks
- 🌍 **Preserve language** - create tools for Armenian NLP

## 📋 Tech Stack

- **Language:** Python 3.10+
- **Framework:** PyTorch
- **Architecture:** Transformer (GPT-style)
- **Key Libraries:**
  - `transformers` (Hugging Face)
  - `accelerate` - distributed training
  - `datasets` - data handling
  - `tensorboard` - monitoring

## 📁 Project Structure

```
Armenian-AI/
├── README.md                 # Project overview
├── requirements.txt          # Python dependencies
├── setup.py                  # Package configuration
├── .gitignore               # Git ignore rules
├── .env.example             # Environment template
│
├── data/                     # Datasets
│   ├── raw/                 # Raw Armenian text
│   ├── processed/           # Processed data
│   └── README.md            # Data guide
│
├── src/                      # Main source code
│   ├── __init__.py
│   ├── config.py            # Configuration management
│   ├── data_loader.py       # Data loading and preprocessing
│   ├── tokenizer.py         # Armenian tokenizer
│   ├── model.py             # Model architecture
│   └── utils.py             # Utilities
│
├── scripts/                  # Training and inference scripts
│   ├── train.py             # Training script
│   ├── evaluate.py          # Model evaluation
│   ├── inference.py         # Text generation
│   └── prepare_data.py      # Data preparation
│
├── notebooks/               # Jupyter notebooks for experiments
│   ├── exploration.ipynb    # Data analysis
│   └── experiments.ipynb    # Prototyping
│
├── configs/                 # Training configurations
│   ├── small.yaml           # Small model (testing)
│   ├── medium.yaml          # Medium model (experiments)
│   └── large.yaml           # Large model (full training)
│
├── models/                  # Model checkpoints
│   └── .gitkeep
│
├── logs/                    # Training logs
│   └── .gitkeep
│
└── tests/                   # Unit tests
    ├── __init__.py
    └── test_tokenizer.py
```

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/aniananyan2026-dev/Armenian-AI.git
cd Armenian-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Setup Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 5. Prepare Data

```bash
python scripts/prepare_data.py --source your_data.txt --output data/processed/
```

### 6. Train Model

```bash
# Quick test with small model
python scripts/train.py --config configs/small.yaml

# Full training
python scripts/train.py --config configs/large.yaml
```

### 7. Generate Text

```bash
python scripts/inference.py --model models/checkpoint-1000 --prompt "Բարեւ"
```

## 🏗️ Model Architecture

Transformer-based GPT-style architecture:

```
[Text Input] → [Tokenizer] → [Embeddings] → [Transformer Stack] → [Output Logits]
                                                ↓
                                        (Multi-Head Attention)
                                        (Feed-forward Networks)
                                        (Layer Normalization)
```

### Model Components

- **Embedding Layer:** Convert tokens to vectors
- **Transformer Blocks:** Attention + Feed-forward layers
- **Layer Normalization:** Stabilize training
- **Output Layer:** Predict next token probabilities

## 📊 Training Configurations

Three preset configurations available:

- **Small** (`configs/small.yaml`) - Testing & debugging
- **Medium** (`configs/medium.yaml`) - Experimentation
- **Large** (`configs/large.yaml`) - Production training

Each config specifies:
- Model hyperparameters
- Training settings
- Data paths
- Logging configuration
- Device settings

## 📚 Data Requirements

For training you'll need:
- Armenian text corpus (books, articles, news, etc.)
- Preferably diverse sources
- Clean, well-formed text
- Proper Armenian encoding

### Data Format

Supported formats:
- **Plain text (.txt)** - One document per line
- **JSON Lines (.jsonl)** - `{"text": "..."}`  format
- **CSV (.csv)** - With "text" column

## 🤝 Contributing

Want to contribute? Great!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## ✉️ Contact

- **GitHub:** [@aniananyan2026-dev](https://github.com/aniananyan2026-dev)
- **Project:** Armenian-AI

---

**Status:** 🚧 In Development

Last Updated: July 2026
