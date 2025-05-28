import os
from typing import Tuple

import gdown
import pandas as pd
from sklearn.model_selection import train_test_split

from src import config


def get_datasets() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Download from GDrive all the needed datasets for the project.

    Returns:
        app_train : pd.DataFrame
            Training dataset

        app_test : pd.DataFrame
            Test dataset

        columns_description : pd.DataFrame
            Extra dataframe with detailed description about dataset features
    """
    # Download HomeCredit_columns_description.csv
    if not os.path.exists(config.DATASET_DESCRIPTION):
        gdown.download(
            config.DATASET_DESCRIPTION_URL, config.DATASET_DESCRIPTION, quiet=False
        )

    # Download application_test_aai.csv
    if not os.path.exists(config.DATASET_TEST):
        gdown.download(config.DATASET_TEST_URL, config.DATASET_TEST, quiet=False)

    # Download application_train_aai.csv
    if not os.path.exists(config.DATASET_TRAIN):
        gdown.download(config.DATASET_TRAIN_URL, config.DATASET_TRAIN, quiet=False)

    app_train = pd.read_csv(config.DATASET_TRAIN)
    app_test = pd.read_csv(config.DATASET_TEST)
    columns_description = pd.read_csv(config.DATASET_DESCRIPTION_URL)

    return app_train, app_test, columns_description
