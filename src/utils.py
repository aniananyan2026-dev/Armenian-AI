"""
Utility functions for Armenian-AI project.
"""

import logging
import os
import json
from pathlib import Path
from typing import Dict, Any
import yaml


def setup_logging(log_dir: str = "logs", log_name: str = "training.log") -> logging.Logger:
    """Setup logging for the project."""
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    
    logger = logging.getLogger("armenian-ai")
    logger.setLevel(logging.DEBUG)
    
    # File handler
    fh = logging.FileHandler(os.path.join(log_dir, log_name))
    fh.setLevel(logging.DEBUG)
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger


def load_yaml_config(config_path: str) -> Dict[str, Any]:
    """Load YAML configuration file."""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save dictionary to JSON file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_device_info() -> str:
    """Get device information."""
    try:
        import torch
        if torch.cuda.is_available():
            device = f"cuda:{torch.cuda.current_device()}"
            gpu_name = torch.cuda.get_device_name(0)
            return f"{device} ({gpu_name})"
        else:
            return "cpu"
    except ImportError:
        return "cpu"


def print_model_summary(model) -> None:
    """Print model summary."""
    logger = logging.getLogger("armenian-ai")
    
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    
    logger.info(f"Total parameters: {total_params:,}")
    logger.info(f"Trainable parameters: {trainable_params:,}")
    logger.info(f"Model size: {total_params * 4 / 1024**3:.2f} GB (fp32)")
