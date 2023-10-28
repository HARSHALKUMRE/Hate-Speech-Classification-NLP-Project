import os

from datetime import datetime

# common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = "twitter-hate-speech"
ZIP_FILE_NAME = "dataset.zip"

# Data Ingestion Constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"
