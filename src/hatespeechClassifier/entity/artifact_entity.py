from dataclasses import dataclass

# Data Ingestion Artifacts
@dataclass
class DataIngestionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str

# Data Transformation Artifacts
@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str  

# Model Trainer Artifacts
@dataclass
class ModelTrainerArtifacts:
    trained_model_path: str 
    x_test_path: list
    y_test_path: list