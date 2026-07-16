"""
Armenian-AI: Building a Language Model for Armenian

Modern transformer-based LLM for the Armenian language.
"""

__version__ = "0.1.0"
__author__ = "aniananyan2026-dev"

from . import config, data_loader, model, tokenizer, utils

__all__ = [
    "config",
    "data_loader",
    "model",
    "tokenizer",
    "utils",
]
