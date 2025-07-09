#!/usr/bin/env python3
"""
Data download script for Finntelligence Engine
Downloads Lending Club loan data from Kaggle and prepares it for analysis.
"""

import kagglehub
import pandas as pd
import shutil
import os
from pathlib import Path

def download_lending_club_data():
    """Download Lending Club dataset from Kaggle and organize it properly."""
    
    print("🔄 Downloading Lending Club dataset from Kaggle...")
    
    # Download latest version
    path = kagglehub.dataset_download("adarshsng/lending-club-loan-data-csv")
    print(f"📁 Dataset downloaded to: {path}")
    
    # Create our data directories if they don't exist
    data_dir = Path("data")
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    # Find and copy the loan.csv file to our data/raw directory
    source_files = list(Path(path).glob("*.csv"))
    if source_files:
        for csv_file in source_files:
            destination = raw_dir / csv_file.name
            shutil.copy2(csv_file, destination)
            print(f"✅ Copied {csv_file.name} to {destination}")
    else:
        print("❌ No CSV files found in downloaded dataset")
    
    return raw_dir

if __name__ == "__main__":
    download_lending_club_data()
