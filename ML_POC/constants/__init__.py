
import os
from datetime import date

DATABASE_NAME = "POC_ML_Classification" #Delete this comment, database name is the name in MongoDB which you have created . For reference check the screenshot

COLLECTION_NAME = "visa_data" #check screenshot This will also change wrt to JIRA

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")



"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data" #check screenshot This will also change wrt to JIRA
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

