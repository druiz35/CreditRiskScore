# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv, dotenv_values
import gdown
import os


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # get .env values for using the paths
    env_values = dotenv_values()
    DATASET_DESCRIPTION = env_values["DATASET_DESCRIPTION"]
    DATASET_DESCRIPTION_URL = env_values["DATASET_DESCRIPTION_URL"]
    DATASET_TEST = env_values["DATASET_TEST"]
    DATASET_TEST_URL = env_values["DATASET_TEST_URL"]
    DATASET_TRAIN = env_values["DATASET_TRAIN"]
    DATASET_TRAIN_URL = env_values["DATASET_TRAIN_URL"]

    # Dowload HomeCredit_columns_descriptions.csv
    logger.info('Dowloading datasets from Google Drive: ')
    logger.info('Dowloading HomeCredit_columns_descriptions.. ')
    if not os.path.exists(DATASET_DESCRIPTION):
        gdown.download(
            DATASET_DESCRIPTION_URL, DATASET_DESCRIPTION, quiet=False
        )
    logger.info('Done!')

    # Download application_test_aai.csv
    logger.info('Dowloading application_test_aai.. ')
    if not os.path.exists(DATASET_TEST):
        gdown.download(DATASET_TEST_URL, DATASET_TEST, quiet=False)
    logger.info('Done!')

    # Download application_train_aai.csv
    logger.info('Dowloading application_train_aai.. ')
    if not os.path.exists(DATASET_TRAIN):
        gdown.download(DATASET_TRAIN_URL, DATASET_TRAIN, quiet=False)    
    logger.info('Done!')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
